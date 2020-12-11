# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class UserDeviceEnrollmentConfigurationOperations:
    """UserDeviceEnrollmentConfigurationOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_actions.models
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

    async def assign(
        self,
        user_id: str,
        device_enrollment_configuration_id: str,
        enrollment_configuration_assignments: Optional[List["models.MicrosoftGraphEnrollmentConfigurationAssignment"]] = None,
        **kwargs
    ) -> None:
        """Invoke action assign.

        Invoke action assign.

        :param user_id: key: id of user.
        :type user_id: str
        :param device_enrollment_configuration_id: key: id of deviceEnrollmentConfiguration.
        :type device_enrollment_configuration_id: str
        :param enrollment_configuration_assignments:
        :type enrollment_configuration_assignments: list[~users_actions.models.MicrosoftGraphEnrollmentConfigurationAssignment]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths1A7V22XUsersUserIdDeviceenrollmentconfigurationsDeviceenrollmentconfigurationIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema(enrollment_configuration_assignments=enrollment_configuration_assignments)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.assign.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'deviceEnrollmentConfiguration-id': self._serialize.url("device_enrollment_configuration_id", device_enrollment_configuration_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'Paths1A7V22XUsersUserIdDeviceenrollmentconfigurationsDeviceenrollmentconfigurationIdMicrosoftGraphAssignPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    assign.metadata = {'url': '/users/{user-id}/deviceEnrollmentConfigurations/{deviceEnrollmentConfiguration-id}/microsoft.graph.assign'}  # type: ignore

    async def set_priority(
        self,
        user_id: str,
        device_enrollment_configuration_id: str,
        priority: Optional[int] = None,
        **kwargs
    ) -> None:
        """Invoke action setPriority.

        Invoke action setPriority.

        :param user_id: key: id of user.
        :type user_id: str
        :param device_enrollment_configuration_id: key: id of deviceEnrollmentConfiguration.
        :type device_enrollment_configuration_id: str
        :param priority:
        :type priority: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths64E37UUsersUserIdDeviceenrollmentconfigurationsDeviceenrollmentconfigurationIdMicrosoftGraphSetpriorityPostRequestbodyContentApplicationJsonSchema(priority=priority)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.set_priority.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'deviceEnrollmentConfiguration-id': self._serialize.url("device_enrollment_configuration_id", device_enrollment_configuration_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'Paths64E37UUsersUserIdDeviceenrollmentconfigurationsDeviceenrollmentconfigurationIdMicrosoftGraphSetpriorityPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    set_priority.metadata = {'url': '/users/{user-id}/deviceEnrollmentConfigurations/{deviceEnrollmentConfiguration-id}/microsoft.graph.setPriority'}  # type: ignore

    async def has_payload_link(
        self,
        user_id: str,
        payload_ids: Optional[List[str]] = None,
        **kwargs
    ) -> List["models.MicrosoftGraphHasPayloadLinkResultItem"]:
        """Invoke action hasPayloadLinks.

        Invoke action hasPayloadLinks.

        :param user_id: key: id of user.
        :type user_id: str
        :param payload_ids:
        :type payload_ids: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphHasPayloadLinkResultItem, or the result of cls(response)
        :rtype: list[~users_actions.models.MicrosoftGraphHasPayloadLinkResultItem]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphHasPayloadLinkResultItem"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths1R7K6PzUsersUserIdDeviceenrollmentconfigurationsMicrosoftGraphHaspayloadlinksPostRequestbodyContentApplicationJsonSchema(payload_ids=payload_ids)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.has_payload_link.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
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
        body_content = self._serialize.body(_body, 'Paths1R7K6PzUsersUserIdDeviceenrollmentconfigurationsMicrosoftGraphHaspayloadlinksPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[MicrosoftGraphHasPayloadLinkResultItem]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    has_payload_link.metadata = {'url': '/users/{user-id}/deviceEnrollmentConfigurations/microsoft.graph.hasPayloadLinks'}  # type: ignore
