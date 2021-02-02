# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, AsyncIterable, Callable, Dict, Generic, List, Optional, TypeVar, Union
import warnings

from azure.core.async_paging import AsyncItemPaged, AsyncList
from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class GroupOperations:
    """GroupOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~applications.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def list_app_role_assignment(
        self,
        group_id: str,
        orderby: Optional[List[Union[str, "models.Enum24"]]] = None,
        select: Optional[List[Union[str, "models.Enum25"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> AsyncIterable["models.CollectionOfAppRoleAssignment"]:
        """Get appRoleAssignments from groups.

        Get appRoleAssignments from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~applications.models.Enum24]
        :param select: Select properties to be returned.
        :type select: list[str or ~applications.models.Enum25]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfAppRoleAssignment or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~applications.models.CollectionOfAppRoleAssignment]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfAppRoleAssignment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_app_role_assignment.metadata['url']  # type: ignore
                path_format_arguments = {
                    'group-id': self._serialize.url("group_id", group_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
                # Construct parameters
                query_parameters = {}  # type: Dict[str, Any]
                if self._config.top is not None:
                    query_parameters['$top'] = self._serialize.query("self._config.top", self._config.top, 'int', minimum=0)
                if self._config.skip is not None:
                    query_parameters['$skip'] = self._serialize.query("self._config.skip", self._config.skip, 'int', minimum=0)
                if self._config.search is not None:
                    query_parameters['$search'] = self._serialize.query("self._config.search", self._config.search, 'str')
                if self._config.filter is not None:
                    query_parameters['$filter'] = self._serialize.query("self._config.filter", self._config.filter, 'str')
                if self._config.count is not None:
                    query_parameters['$count'] = self._serialize.query("self._config.count", self._config.count, 'bool')
                if orderby is not None:
                    query_parameters['$orderby'] = self._serialize.query("orderby", orderby, '[str]', div=',')
                if select is not None:
                    query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
                if expand is not None:
                    query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

                request = self._client.get(url, query_parameters, header_parameters)
            else:
                url = next_link
                query_parameters = {}  # type: Dict[str, Any]
                request = self._client.get(url, query_parameters, header_parameters)
            return request

        async def extract_data(pipeline_response):
            deserialized = self._deserialize('CollectionOfAppRoleAssignment', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, AsyncList(list_of_elem)

        async def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.OdataError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return AsyncItemPaged(
            get_next, extract_data
        )
    list_app_role_assignment.metadata = {'url': '/groups/{group-id}/appRoleAssignments'}  # type: ignore

    async def create_app_role_assignment(
        self,
        group_id: str,
        id: Optional[str] = None,
        deleted_date_time: Optional[datetime.datetime] = None,
        app_role_id: Optional[str] = None,
        created_date_time: Optional[datetime.datetime] = None,
        principal_display_name: Optional[str] = None,
        principal_id: Optional[str] = None,
        principal_type: Optional[str] = None,
        resource_display_name: Optional[str] = None,
        resource_id: Optional[str] = None,
        **kwargs
    ) -> "models.MicrosoftGraphAppRoleAssignment":
        """Create new navigation property to appRoleAssignments for groups.

        Create new navigation property to appRoleAssignments for groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param id: Read-only.
        :type id: str
        :param deleted_date_time:
        :type deleted_date_time: ~datetime.datetime
        :param app_role_id: The identifier (id) for the app role which is assigned to the principal.
         This app role must be exposed in the appRoles property on the resource application's service
         principal (resourceId). If the resource application has not declared any app roles, a default
         app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the
         principal is assigned to the resource app without any specific app roles. Required on create.
         Does not support $filter.
        :type app_role_id: str
        :param created_date_time:
        :type created_date_time: ~datetime.datetime
        :param principal_display_name: The display name of the user, group, or service principal that
         was granted the app role assignment. Read-only. Supports $filter (eq and startswith).
        :type principal_display_name: str
        :param principal_id: The unique identifier (id) for the user, group or service principal being
         granted the app role. Required on create. Does not support $filter.
        :type principal_id: str
        :param principal_type: The type of the assigned principal. This can either be 'User', 'Group'
         or 'ServicePrincipal'. Read-only. Does not support $filter.
        :type principal_type: str
        :param resource_display_name: The display name of the resource app's service principal to which
         the assignment is made. Does not support $filter.
        :type resource_display_name: str
        :param resource_id: The unique identifier (id) for the resource service principal for which the
         assignment is made. Required on create. Supports $filter (eq only).
        :type resource_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphAppRoleAssignment, or the result of cls(response)
        :rtype: ~applications.models.MicrosoftGraphAppRoleAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphAppRoleAssignment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphAppRoleAssignment(id=id, deleted_date_time=deleted_date_time, app_role_id=app_role_id, created_date_time=created_date_time, principal_display_name=principal_display_name, principal_id=principal_id, principal_type=principal_type, resource_display_name=resource_display_name, resource_id=resource_id)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_app_role_assignment.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphAppRoleAssignment')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphAppRoleAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_app_role_assignment.metadata = {'url': '/groups/{group-id}/appRoleAssignments'}  # type: ignore

    async def get_app_role_assignment(
        self,
        group_id: str,
        app_role_assignment_id: str,
        select: Optional[List[Union[str, "models.Enum26"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphAppRoleAssignment":
        """Get appRoleAssignments from groups.

        Get appRoleAssignments from groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param app_role_assignment_id: key: id of appRoleAssignment.
        :type app_role_assignment_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~applications.models.Enum26]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphAppRoleAssignment, or the result of cls(response)
        :rtype: ~applications.models.MicrosoftGraphAppRoleAssignment
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphAppRoleAssignment"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_app_role_assignment.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'appRoleAssignment-id': self._serialize.url("app_role_assignment_id", app_role_assignment_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        if select is not None:
            query_parameters['$select'] = self._serialize.query("select", select, '[str]', div=',')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query("expand", expand, '[str]', div=',')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphAppRoleAssignment', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_app_role_assignment.metadata = {'url': '/groups/{group-id}/appRoleAssignments/{appRoleAssignment-id}'}  # type: ignore

    async def update_app_role_assignment(
        self,
        group_id: str,
        app_role_assignment_id: str,
        id: Optional[str] = None,
        deleted_date_time: Optional[datetime.datetime] = None,
        app_role_id: Optional[str] = None,
        created_date_time: Optional[datetime.datetime] = None,
        principal_display_name: Optional[str] = None,
        principal_id: Optional[str] = None,
        principal_type: Optional[str] = None,
        resource_display_name: Optional[str] = None,
        resource_id: Optional[str] = None,
        **kwargs
    ) -> None:
        """Update the navigation property appRoleAssignments in groups.

        Update the navigation property appRoleAssignments in groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param app_role_assignment_id: key: id of appRoleAssignment.
        :type app_role_assignment_id: str
        :param id: Read-only.
        :type id: str
        :param deleted_date_time:
        :type deleted_date_time: ~datetime.datetime
        :param app_role_id: The identifier (id) for the app role which is assigned to the principal.
         This app role must be exposed in the appRoles property on the resource application's service
         principal (resourceId). If the resource application has not declared any app roles, a default
         app role ID of 00000000-0000-0000-0000-000000000000 can be specified to signal that the
         principal is assigned to the resource app without any specific app roles. Required on create.
         Does not support $filter.
        :type app_role_id: str
        :param created_date_time:
        :type created_date_time: ~datetime.datetime
        :param principal_display_name: The display name of the user, group, or service principal that
         was granted the app role assignment. Read-only. Supports $filter (eq and startswith).
        :type principal_display_name: str
        :param principal_id: The unique identifier (id) for the user, group or service principal being
         granted the app role. Required on create. Does not support $filter.
        :type principal_id: str
        :param principal_type: The type of the assigned principal. This can either be 'User', 'Group'
         or 'ServicePrincipal'. Read-only. Does not support $filter.
        :type principal_type: str
        :param resource_display_name: The display name of the resource app's service principal to which
         the assignment is made. Does not support $filter.
        :type resource_display_name: str
        :param resource_id: The unique identifier (id) for the resource service principal for which the
         assignment is made. Required on create. Supports $filter (eq only).
        :type resource_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphAppRoleAssignment(id=id, deleted_date_time=deleted_date_time, app_role_id=app_role_id, created_date_time=created_date_time, principal_display_name=principal_display_name, principal_id=principal_id, principal_type=principal_type, resource_display_name=resource_display_name, resource_id=resource_id)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_app_role_assignment.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'appRoleAssignment-id': self._serialize.url("app_role_assignment_id", app_role_assignment_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphAppRoleAssignment')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_app_role_assignment.metadata = {'url': '/groups/{group-id}/appRoleAssignments/{appRoleAssignment-id}'}  # type: ignore

    async def delete_app_role_assignment(
        self,
        group_id: str,
        app_role_assignment_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property appRoleAssignments for groups.

        Delete navigation property appRoleAssignments for groups.

        :param group_id: key: id of group.
        :type group_id: str
        :param app_role_assignment_id: key: id of appRoleAssignment.
        :type app_role_assignment_id: str
        :param if_match: ETag.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delete_app_role_assignment.metadata['url']  # type: ignore
        path_format_arguments = {
            'group-id': self._serialize.url("group_id", group_id, 'str'),
            'appRoleAssignment-id': self._serialize.url("app_role_assignment_id", app_role_assignment_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_app_role_assignment.metadata = {'url': '/groups/{group-id}/appRoleAssignments/{appRoleAssignment-id}'}  # type: ignore
