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

"""Describe instance command."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.dataproc import dataproc as dp
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.dataproc import flags
from googlecloudsdk.command_lib.dataproc import instances
from googlecloudsdk.core import log


@base.Hidden
@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Describe(base.DescribeCommand):
  """View the details of an instance."""

  detailed_help = {
      'EXAMPLES': """\
          To view the details of an instance, run:

            $ {command} my-instance --region=us-central1
          """,
  }

  @classmethod
  def Args(cls, parser):
    dataproc = dp.Dataproc(cls.ReleaseTrack())
    flags.AddInstanceResourceArg(parser, 'describe', dataproc.api_version)

  def Run(self, args):
    dataproc = dp.Dataproc(self.ReleaseTrack())

    instance_ref = args.CONCEPTS.instance.Parse()
    request = dataproc.messages.DataprocProjectsRegionsClustersGetRequest(
        projectId=instance_ref.projectId,
        region=instance_ref.region,
        clusterName=instance_ref.clusterName,
    )

    cluster = dataproc.client.projects_regions_clusters.Get(request)
    log.debug(
        'quanfeng cluster to describe "%s" .',
        cluster,
    )
    return instances.ConvertClusterToInstance(cluster)
