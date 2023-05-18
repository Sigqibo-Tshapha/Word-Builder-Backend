"""Generated client library for notebooks version v1beta1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.notebooks.v1beta1 import notebooks_v1beta1_messages as messages


class NotebooksV1beta1(base_api.BaseApiClient):
  """Generated client library for service notebooks version v1beta1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://notebooks.googleapis.com/'
  MTLS_BASE_URL = 'https://notebooks.mtls.googleapis.com/'

  _PACKAGE = 'notebooks'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1beta1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'NotebooksV1beta1'
  _URL_VERSION = 'v1beta1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new notebooks handle."""
    url = url or self.BASE_URL
    super(NotebooksV1beta1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_environments = self.ProjectsLocationsEnvironmentsService(self)
    self.projects_locations_instances = self.ProjectsLocationsInstancesService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsEnvironmentsService(base_api.BaseApiService):
    """Service class for the projects_locations_environments resource."""

    _NAME = 'projects_locations_environments'

    def __init__(self, client):
      super(NotebooksV1beta1.ProjectsLocationsEnvironmentsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Environment.

      Args:
        request: (NotebooksProjectsLocationsEnvironmentsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/environments',
        http_method='POST',
        method_id='notebooks.projects.locations.environments.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['environmentId'],
        relative_path='v1beta1/{+parent}/environments',
        request_field='environment',
        request_type_name='NotebooksProjectsLocationsEnvironmentsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Environment.

      Args:
        request: (NotebooksProjectsLocationsEnvironmentsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}',
        http_method='DELETE',
        method_id='notebooks.projects.locations.environments.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='NotebooksProjectsLocationsEnvironmentsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Environment.

      Args:
        request: (NotebooksProjectsLocationsEnvironmentsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Environment) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/environments/{environmentsId}',
        http_method='GET',
        method_id='notebooks.projects.locations.environments.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='NotebooksProjectsLocationsEnvironmentsGetRequest',
        response_type_name='Environment',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists environments in a project.

      Args:
        request: (NotebooksProjectsLocationsEnvironmentsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListEnvironmentsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/environments',
        http_method='GET',
        method_id='notebooks.projects.locations.environments.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1beta1/{+parent}/environments',
        request_field='',
        request_type_name='NotebooksProjectsLocationsEnvironmentsListRequest',
        response_type_name='ListEnvironmentsResponse',
        supports_download=False,
    )

  class ProjectsLocationsInstancesService(base_api.BaseApiService):
    """Service class for the projects_locations_instances resource."""

    _NAME = 'projects_locations_instances'

    def __init__(self, client):
      super(NotebooksV1beta1.ProjectsLocationsInstancesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Creates a new Instance in a given project and location.

      Args:
        request: (NotebooksProjectsLocationsInstancesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances',
        http_method='POST',
        method_id='notebooks.projects.locations.instances.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['instanceId'],
        relative_path='v1beta1/{+parent}/instances',
        request_field='instance',
        request_type_name='NotebooksProjectsLocationsInstancesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a single Instance.

      Args:
        request: (NotebooksProjectsLocationsInstancesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}',
        http_method='DELETE',
        method_id='notebooks.projects.locations.instances.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='NotebooksProjectsLocationsInstancesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets details of a single Instance.

      Args:
        request: (NotebooksProjectsLocationsInstancesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Instance) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}',
        http_method='GET',
        method_id='notebooks.projects.locations.instances.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='NotebooksProjectsLocationsInstancesGetRequest',
        response_type_name='Instance',
        supports_download=False,
    )

    def GetIamPolicy(self, request, global_params=None):
      r"""Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

      Args:
        request: (NotebooksProjectsLocationsInstancesGetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('GetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:getIamPolicy',
        http_method='GET',
        method_id='notebooks.projects.locations.instances.getIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=['options_requestedPolicyVersion'],
        relative_path='v1beta1/{+resource}:getIamPolicy',
        request_field='',
        request_type_name='NotebooksProjectsLocationsInstancesGetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def IsUpgradeable(self, request, global_params=None):
      r"""Check if a notebook instance is upgradable. Deprecated. Please consider using v1.

      Args:
        request: (NotebooksProjectsLocationsInstancesIsUpgradeableRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (IsInstanceUpgradeableResponse) The response message.
      """
      config = self.GetMethodConfig('IsUpgradeable')
      return self._RunMethod(
          config, request, global_params=global_params)

    IsUpgradeable.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:isUpgradeable',
        http_method='GET',
        method_id='notebooks.projects.locations.instances.isUpgradeable',
        ordered_params=['notebookInstance'],
        path_params=['notebookInstance'],
        query_params=[],
        relative_path='v1beta1/{+notebookInstance}:isUpgradeable',
        request_field='',
        request_type_name='NotebooksProjectsLocationsInstancesIsUpgradeableRequest',
        response_type_name='IsInstanceUpgradeableResponse',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists instances in a given project and location.

      Args:
        request: (NotebooksProjectsLocationsInstancesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListInstancesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances',
        http_method='GET',
        method_id='notebooks.projects.locations.instances.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1beta1/{+parent}/instances',
        request_field='',
        request_type_name='NotebooksProjectsLocationsInstancesListRequest',
        response_type_name='ListInstancesResponse',
        supports_download=False,
    )

    def Register(self, request, global_params=None):
      r"""Registers an existing legacy notebook instance to the Notebooks API server. Legacy instances are instances created with the legacy Compute Engine calls. They are not manageable by the Notebooks API out of the box. This call makes these instances manageable by the Notebooks API.

      Args:
        request: (NotebooksProjectsLocationsInstancesRegisterRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Register')
      return self._RunMethod(
          config, request, global_params=global_params)

    Register.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances:register',
        http_method='POST',
        method_id='notebooks.projects.locations.instances.register',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1beta1/{+parent}/instances:register',
        request_field='registerInstanceRequest',
        request_type_name='NotebooksProjectsLocationsInstancesRegisterRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Report(self, request, global_params=None):
      r"""Allows notebook instances to report their latest instance information to the Notebooks API server. The server will merge the reported information to the instance metadata store. Do not use this method directly.

      Args:
        request: (NotebooksProjectsLocationsInstancesReportRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Report')
      return self._RunMethod(
          config, request, global_params=global_params)

    Report.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:report',
        http_method='POST',
        method_id='notebooks.projects.locations.instances.report',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:report',
        request_field='reportInstanceInfoRequest',
        request_type_name='NotebooksProjectsLocationsInstancesReportRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Reset(self, request, global_params=None):
      r"""Resets a notebook instance.

      Args:
        request: (NotebooksProjectsLocationsInstancesResetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Reset')
      return self._RunMethod(
          config, request, global_params=global_params)

    Reset.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:reset',
        http_method='POST',
        method_id='notebooks.projects.locations.instances.reset',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:reset',
        request_field='resetInstanceRequest',
        request_type_name='NotebooksProjectsLocationsInstancesResetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def SetAccelerator(self, request, global_params=None):
      r"""Updates the guest accelerators of a single Instance.

      Args:
        request: (NotebooksProjectsLocationsInstancesSetAcceleratorRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('SetAccelerator')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetAccelerator.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:setAccelerator',
        http_method='PATCH',
        method_id='notebooks.projects.locations.instances.setAccelerator',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:setAccelerator',
        request_field='setInstanceAcceleratorRequest',
        request_type_name='NotebooksProjectsLocationsInstancesSetAcceleratorRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def SetIamPolicy(self, request, global_params=None):
      r"""Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

      Args:
        request: (NotebooksProjectsLocationsInstancesSetIamPolicyRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Policy) The response message.
      """
      config = self.GetMethodConfig('SetIamPolicy')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetIamPolicy.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:setIamPolicy',
        http_method='POST',
        method_id='notebooks.projects.locations.instances.setIamPolicy',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/{+resource}:setIamPolicy',
        request_field='setIamPolicyRequest',
        request_type_name='NotebooksProjectsLocationsInstancesSetIamPolicyRequest',
        response_type_name='Policy',
        supports_download=False,
    )

    def SetLabels(self, request, global_params=None):
      r"""Updates the labels of an Instance.

      Args:
        request: (NotebooksProjectsLocationsInstancesSetLabelsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('SetLabels')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetLabels.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:setLabels',
        http_method='PATCH',
        method_id='notebooks.projects.locations.instances.setLabels',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:setLabels',
        request_field='setInstanceLabelsRequest',
        request_type_name='NotebooksProjectsLocationsInstancesSetLabelsRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def SetMachineType(self, request, global_params=None):
      r"""Updates the machine type of a single Instance.

      Args:
        request: (NotebooksProjectsLocationsInstancesSetMachineTypeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('SetMachineType')
      return self._RunMethod(
          config, request, global_params=global_params)

    SetMachineType.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:setMachineType',
        http_method='PATCH',
        method_id='notebooks.projects.locations.instances.setMachineType',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:setMachineType',
        request_field='setInstanceMachineTypeRequest',
        request_type_name='NotebooksProjectsLocationsInstancesSetMachineTypeRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Start(self, request, global_params=None):
      r"""Starts a notebook instance.

      Args:
        request: (NotebooksProjectsLocationsInstancesStartRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Start')
      return self._RunMethod(
          config, request, global_params=global_params)

    Start.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:start',
        http_method='POST',
        method_id='notebooks.projects.locations.instances.start',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:start',
        request_field='startInstanceRequest',
        request_type_name='NotebooksProjectsLocationsInstancesStartRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Stop(self, request, global_params=None):
      r"""Stops a notebook instance.

      Args:
        request: (NotebooksProjectsLocationsInstancesStopRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Stop')
      return self._RunMethod(
          config, request, global_params=global_params)

    Stop.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:stop',
        http_method='POST',
        method_id='notebooks.projects.locations.instances.stop',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:stop',
        request_field='stopInstanceRequest',
        request_type_name='NotebooksProjectsLocationsInstancesStopRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def TestIamPermissions(self, request, global_params=None):
      r"""Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

      Args:
        request: (NotebooksProjectsLocationsInstancesTestIamPermissionsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (TestIamPermissionsResponse) The response message.
      """
      config = self.GetMethodConfig('TestIamPermissions')
      return self._RunMethod(
          config, request, global_params=global_params)

    TestIamPermissions.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:testIamPermissions',
        http_method='POST',
        method_id='notebooks.projects.locations.instances.testIamPermissions',
        ordered_params=['resource'],
        path_params=['resource'],
        query_params=[],
        relative_path='v1beta1/{+resource}:testIamPermissions',
        request_field='testIamPermissionsRequest',
        request_type_name='NotebooksProjectsLocationsInstancesTestIamPermissionsRequest',
        response_type_name='TestIamPermissionsResponse',
        supports_download=False,
    )

    def Upgrade(self, request, global_params=None):
      r"""Upgrades a notebook instance to the latest version. Deprecated. Please consider using v1.

      Args:
        request: (NotebooksProjectsLocationsInstancesUpgradeRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Upgrade')
      return self._RunMethod(
          config, request, global_params=global_params)

    Upgrade.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:upgrade',
        http_method='POST',
        method_id='notebooks.projects.locations.instances.upgrade',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:upgrade',
        request_field='upgradeInstanceRequest',
        request_type_name='NotebooksProjectsLocationsInstancesUpgradeRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def UpgradeInternal(self, request, global_params=None):
      r"""Allows notebook instances to call this endpoint to upgrade themselves. Do not use this method directly. Deprecated. Please consider using v1.

      Args:
        request: (NotebooksProjectsLocationsInstancesUpgradeInternalRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('UpgradeInternal')
      return self._RunMethod(
          config, request, global_params=global_params)

    UpgradeInternal.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/instances/{instancesId}:upgradeInternal',
        http_method='POST',
        method_id='notebooks.projects.locations.instances.upgradeInternal',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:upgradeInternal',
        request_field='upgradeInstanceInternalRequest',
        request_type_name='NotebooksProjectsLocationsInstancesUpgradeInternalRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(NotebooksV1beta1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (NotebooksProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='notebooks.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='NotebooksProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (NotebooksProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='notebooks.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='NotebooksProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (NotebooksProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='notebooks.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='NotebooksProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

      Args:
        request: (NotebooksProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='notebooks.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta1/{+name}/operations',
        request_field='',
        request_type_name='NotebooksProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(NotebooksV1beta1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (NotebooksProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='notebooks.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1beta1/{+name}',
        request_field='',
        request_type_name='NotebooksProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (NotebooksProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1beta1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='notebooks.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1beta1/{+name}/locations',
        request_field='',
        request_type_name='NotebooksProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(NotebooksV1beta1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
