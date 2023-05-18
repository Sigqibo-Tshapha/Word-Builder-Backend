# -*- coding: utf-8 -*- #
# Copyright 2023 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Generic functions for listing commands."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import abc
import enum

from googlecloudsdk.api_lib.storage import cloud_api
from googlecloudsdk.command_lib.storage import errors
from googlecloudsdk.command_lib.storage import plurality_checkable_iterator
from googlecloudsdk.command_lib.storage import wildcard_iterator
from googlecloudsdk.command_lib.storage.resources import resource_reference
from googlecloudsdk.command_lib.storage.resources import shim_format_util

import six


def check_and_convert_to_readable_sizes(
    size, readable_sizes=False, use_gsutil_style=False
):
  if readable_sizes and size is not None:
    return shim_format_util.get_human_readable_byte_value(
        size, use_gsutil_style=use_gsutil_style
    )
  else:
    # Also handles None values.
    return six.text_type(size)


class DisplayDetail(enum.Enum):
  """Level of detail to display about items being printed."""

  SHORT = 1
  LONG = 2
  FULL = 3
  JSON = 4


def _translate_display_detail_to_fields_scope(
    display_detail, is_bucket_listing
):
  """Translates display details to fields scope equivalent.

  Args:
    display_detail (DisplayDetail): Argument to translate.
    is_bucket_listing (bool): Buckets require special handling.

  Returns:
    cloud_api.FieldsScope appropriate for the resources and display detail.
  """
  # Long listing is the same as normal listing for buckets.
  if display_detail == DisplayDetail.LONG and is_bucket_listing:
    return cloud_api.FieldsScope.SHORT

  display_detail_to_fields_scope = {
      DisplayDetail.SHORT: cloud_api.FieldsScope.SHORT,
      DisplayDetail.LONG: cloud_api.FieldsScope.NO_ACL,
      DisplayDetail.FULL: cloud_api.FieldsScope.FULL,
      DisplayDetail.JSON: cloud_api.FieldsScope.FULL,
  }
  return display_detail_to_fields_scope[display_detail]


class BaseFormatWrapper(six.with_metaclass(abc.ABCMeta)):
  """For formatting how items are printed when listed.

  Attributes:
    resource (resource_reference.Resource): Item to be formatted for printing.
  """

  def __init__(
      self,
      resource,
      all_versions=False,
      display_detail=DisplayDetail.SHORT,
      full_formatter=None,
      include_etag=None,
      readable_sizes=False,
      use_gsutil_style=False,
  ):
    """Initializes wrapper instance.

    Args:
      resource (resource_reference.Resource): Item to be formatted for printing.
      all_versions (bool): Determine whether or not to return all versions of
        listed objects.
      display_detail (DisplayDetail): Level of metadata detail for printing.
      full_formatter (base.FullResourceFormatter): Printing formatter used witch
        FULL DisplayDetail.
      include_etag (bool): Display etag string of resource.
      readable_sizes (bool): Convert bytes to a more human readable format for
        long lising. For example, print 1024B as 1KiB.
      use_gsutil_style (bool): Outputs closer to the style of the gsutil CLI.
    """
    self.resource = resource
    self._all_versions = all_versions
    self._display_detail = display_detail
    self._full_formatter = full_formatter
    self._include_etag = include_etag
    self._readable_sizes = readable_sizes
    self._use_gsutil_style = use_gsutil_style

  def _check_and_handles_all_versions(self):
    if self._all_versions:
      url_string = self.resource.storage_url.url_string
      metageneration_string = '  metageneration={}'.format(
          six.text_type(self.resource.metageneration)
      )
    else:
      url_string = self.resource.storage_url.versionless_url_string
      metageneration_string = ''
    return (url_string, metageneration_string)


class NullFormatWrapper(BaseFormatWrapper):
  """For formatting how containers are printed as headers when listed."""

  def __init__(
      self,
      resource,
      all_versions=None,
      container_size=None,
      display_detail=None,
      full_formatter=None,
      include_etag=None,
      readable_sizes=None,
      use_gsutil_style=None,
  ):
    super(NullFormatWrapper, self).__init__(resource)
    del (
        all_versions,
        container_size,
        display_detail,
        full_formatter,
        include_etag,
        readable_sizes,
        use_gsutil_style,
    )

  def __str__(self):
    return ''


class BaseListExecutor(six.with_metaclass(abc.ABCMeta)):
  """Abstract base class for list executors (e.g. for ls and du)."""

  def __init__(
      self,
      cloud_urls,
      all_versions=False,
      buckets_flag=False,
      display_detail=DisplayDetail.SHORT,
      fetch_encrypted_object_hashes=False,
      include_etag=False,
      readable_sizes=False,
      recursion_flag=False,
      total=False,
      use_gsutil_style=False,
      zero_terminator=False,
  ):
    """Initializes task.

    Args:
      cloud_urls ([storage_url.CloudUrl]): List of non-local filesystem URLs.
      all_versions (bool): Determine whether or not to return all versions of
        listed objects.
      buckets_flag (bool): If given a bucket URL, only return matching buckets
        ignoring normal recursion rules.
      display_detail (DisplayDetail): Determines level of metadata printed.
      fetch_encrypted_object_hashes (bool): Fall back to GET requests for
        encrypted objects in order to fetch their hash values.
      include_etag (bool): Print etag string of resource, depending on other
        settings.
      readable_sizes (bool): Convert bytes to a more human readable format for
        long lising. For example, print 1024B as 1KiB.
      recursion_flag (bool): Recurse through all containers and format all
        container headers.
      total (bool): Add up the total size of all input sources.
      use_gsutil_style (bool): Outputs closer to the style of the gsutil CLI.
      zero_terminator (bool): Use null byte instead of newline as line
        terminator.
    """

    self._cloud_urls = cloud_urls
    self._all_versions = all_versions
    self._buckets_flag = buckets_flag
    self._display_detail = display_detail
    self._fetch_encrypted_object_hashes = fetch_encrypted_object_hashes
    self._include_etag = include_etag
    self._readable_sizes = readable_sizes
    self._recursion_flag = recursion_flag
    self._total = total
    self._use_gsutil_style = use_gsutil_style
    self._zero_terminator = zero_terminator

    self._full_formatter = None
    # Null wrappers print nothing
    self._header_wrapper = NullFormatWrapper
    self._container_summary_wrapper = NullFormatWrapper
    self._object_wrapper = NullFormatWrapper

  def _get_container_iterator(self, container_cloud_url, recursion_level):
    """For recursing into and retrieving the contents of a container.

    Args:
      container_cloud_url (storage_url.CloudUrl): Container URL for recursing
        into.
      recursion_level (int): Determines if iterator should keep recursing.

    Returns:
      BaseFormatWrapper generator.
    """
    # End URL with '/*', so WildcardIterator won't filter out its contents.
    new_cloud_url = container_cloud_url.join('*')
    fields_scope = _translate_display_detail_to_fields_scope(
        self._display_detail, is_bucket_listing=False
    )
    iterator = wildcard_iterator.CloudWildcardIterator(
        new_cloud_url,
        all_versions=self._all_versions,
        error_on_missing_key=False,
        fetch_encrypted_object_hashes=self._fetch_encrypted_object_hashes,
        fields_scope=fields_scope,
    )
    return self._recursion_helper(iterator, recursion_level)

  def _recursion_helper(
      self, iterator, recursion_level, print_top_level_container=True
  ):
    """For retrieving resources from URLs that potentially contain wildcards.

    Args:
      iterator (Iterable[resource_reference.Resource]): For recursing through.
      recursion_level (int): Integer controlling how deep the listing recursion
        goes. "1" is the default, mimicking the actual OS ls, which lists the
        contents of the first level of matching subdirectories. Call with
        "float('inf')" for listing everything available.
      print_top_level_container (bool): Used by `du` to skip printing the top
        level bucket

    Yields:
      BaseFormatWrapper generator.
    """
    for resource in iterator:
      # Check if we need to display contents of a container.
      if (
          resource_reference.is_container_or_has_container_url(resource)
          and recursion_level > 0
      ):
        if self._header_wrapper != NullFormatWrapper:
          yield self._header_wrapper(
              resource,
              all_versions=self._all_versions,
              display_detail=self._display_detail,
              include_etag=self._include_etag,
              readable_sizes=self._readable_sizes,
              full_formatter=self._full_formatter,
              use_gsutil_style=self._use_gsutil_style,
          )

        container_size = 0
        # Get container contents by adding wildcard to URL.
        nested_iterator = self._get_container_iterator(
            resource.storage_url, recursion_level - 1
        )
        for nested_resource in nested_iterator:
          if (
              self._container_summary_wrapper != NullFormatWrapper
              and print_top_level_container
          ):
            container_size += getattr(nested_resource.resource, 'size', 0)
          yield nested_resource
        # Print directories after objects for `du` command
        if (
            self._container_summary_wrapper != NullFormatWrapper
            and print_top_level_container
        ):
          yield self._container_summary_wrapper(
              resource=resource,
              all_versions=self._all_versions,
              container_size=container_size,
              readable_sizes=self._readable_sizes,
          )

      else:
        # Resource wasn't a container we can recurse into, so just yield it.
        yield self._object_wrapper(
            resource,
            all_versions=self._all_versions,
            display_detail=self._display_detail,
            include_etag=self._include_etag,
            readable_sizes=self._readable_sizes,
            full_formatter=self._full_formatter,
            use_gsutil_style=self._use_gsutil_style,
        )

  def _print_summary_for_top_level_url(
      self, resource_url, only_display_buckets, object_count, total_bytes
  ):
    del self, resource_url, only_display_buckets, object_count, total_bytes

  def _print_row_list(
      self, resource_wrappers, resource_url, only_display_buckets
  ):
    """Prints ResourceWrapper objects in list with custom row formatting."""
    object_count = total_bytes = 0
    terminator = '\0' if self._zero_terminator else '\n'
    for i, resource_wrapper in enumerate(resource_wrappers):
      resource_wrapper_string = six.text_type(resource_wrapper)
      if isinstance(
          resource_wrapper.resource, resource_reference.ObjectResource
      ):
        # For printing long listing data summary.
        object_count += 1
        total_bytes += resource_wrapper.resource.size or 0
      if not resource_wrapper_string:
        continue
      if i == 0 and resource_wrapper and resource_wrapper_string[0] == '\n':
        # First print should not begin with a line break, which can happen
        # for headers.
        print(resource_wrapper_string[1:], end=terminator)
      else:
        print(resource_wrapper_string, end=terminator)

    self._print_summary_for_top_level_url(
        resource_url=resource_url,
        only_display_buckets=only_display_buckets,
        object_count=object_count,
        total_bytes=total_bytes,
    )

    return total_bytes

  def _list_url(self, raw_cloud_url):
    """Recursively create wildcard iterators to print all relevant items."""
    only_display_buckets = raw_cloud_url.is_provider() or (
        self._buckets_flag and raw_cloud_url.is_bucket()
    )

    fields_scope = _translate_display_detail_to_fields_scope(
        self._display_detail, is_bucket_listing=raw_cloud_url.is_provider()
    )
    resources = plurality_checkable_iterator.PluralityCheckableIterator(
        wildcard_iterator.CloudWildcardIterator(
            raw_cloud_url,
            all_versions=self._all_versions,
            error_on_missing_key=False,
            fetch_encrypted_object_hashes=self._fetch_encrypted_object_hashes,
            fields_scope=fields_scope,
            get_bucket_metadata=self._buckets_flag,
        )
    )

    if resources.is_empty():
      raise errors.InvalidUrlError('One or more URLs matched no objects.')
    if only_display_buckets:
      # Received a provider URL ("gs://") -> List all buckets.
      # Received buckets flag and bucket URL -> List matching buckets, ignoring
      #   recursion.
      resources_wrappers = self._recursion_helper(resources, recursion_level=0)
    elif self._recursion_flag and '**' not in raw_cloud_url.url_string:
      # "**" overrides recursive flag.
      print_top_level_container = True
      if raw_cloud_url.is_bucket():
        print_top_level_container = False
      resources_wrappers = self._recursion_helper(
          resources, float('inf'), print_top_level_container
      )
    elif not resources.is_plural() and (
        resource_reference.is_container_or_has_container_url(resources.peek())
    ):
      # One container was returned by the query, in which case we show
      # its contents.
      resources_wrappers = self._get_container_iterator(
          resources.peek().storage_url, recursion_level=0
      )
    else:
      resources_wrappers = self._recursion_helper(resources, recursion_level=1)

    size_in_bytes = 0
    if self._display_detail == DisplayDetail.JSON:
      self._print_json_list(resources_wrappers)
    else:
      size_in_bytes = self._print_row_list(
          resources_wrappers, raw_cloud_url, only_display_buckets
      )
    return size_in_bytes

  def _print_total(self, all_sources_total_bytes):
    del all_sources_total_bytes

  def list_urls(self):
    all_sources_total_bytes = 0
    for url in self._cloud_urls:
      if self._total:
        all_sources_total_bytes += self._list_url(url)
      else:
        self._list_url(url)

    if self._total:
      self._print_total(all_sources_total_bytes)
