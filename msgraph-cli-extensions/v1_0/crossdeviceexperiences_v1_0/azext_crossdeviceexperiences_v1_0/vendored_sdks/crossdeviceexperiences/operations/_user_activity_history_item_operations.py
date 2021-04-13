# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class UserActivityHistoryItemOperations(object):
    """UserActivityHistoryItemOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~cross_device_experiences.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_activity(
        self,
        user_id,  # type: str
        user_activity_id,  # type: str
        activity_history_item_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum11"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum12"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphUserActivity"
        """Get activity from users.

        Get activity from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param user_activity_id: key: id of userActivity.
        :type user_activity_id: str
        :param activity_history_item_id: key: id of activityHistoryItem.
        :type activity_history_item_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~cross_device_experiences.models.Enum11]
        :param expand: Expand related entities.
        :type expand: list[str or ~cross_device_experiences.models.Enum12]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphUserActivity, or the result of cls(response)
        :rtype: ~cross_device_experiences.models.MicrosoftGraphUserActivity
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphUserActivity"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_activity.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'userActivity-id': self._serialize.url("user_activity_id", user_activity_id, 'str'),
            'activityHistoryItem-id': self._serialize.url("activity_history_item_id", activity_history_item_id, 'str'),
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

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphUserActivity', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_activity.metadata = {'url': '/users/{user-id}/activities/{userActivity-id}/historyItems/{activityHistoryItem-id}/activity'}  # type: ignore

    def get_ref_activity(
        self,
        user_id,  # type: str
        user_activity_id,  # type: str
        activity_history_item_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> str
        """Get ref of activity from users.

        Get ref of activity from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param user_activity_id: key: id of userActivity.
        :type user_activity_id: str
        :param activity_history_item_id: key: id of activityHistoryItem.
        :type activity_history_item_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: str, or the result of cls(response)
        :rtype: str
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[str]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_ref_activity.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'userActivity-id': self._serialize.url("user_activity_id", user_activity_id, 'str'),
            'activityHistoryItem-id': self._serialize.url("activity_history_item_id", activity_history_item_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('str', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_ref_activity.metadata = {'url': '/users/{user-id}/activities/{userActivity-id}/historyItems/{activityHistoryItem-id}/activity/$ref'}  # type: ignore

    def set_ref_activity(
        self,
        user_id,  # type: str
        user_activity_id,  # type: str
        activity_history_item_id,  # type: str
        body,  # type: Dict[str, object]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the ref of navigation property activity in users.

        Update the ref of navigation property activity in users.

        :param user_id: key: id of user.
        :type user_id: str
        :param user_activity_id: key: id of userActivity.
        :type user_activity_id: str
        :param activity_history_item_id: key: id of activityHistoryItem.
        :type activity_history_item_id: str
        :param body: New navigation property ref values.
        :type body: dict[str, object]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.set_ref_activity.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'userActivity-id': self._serialize.url("user_activity_id", user_activity_id, 'str'),
            'activityHistoryItem-id': self._serialize.url("activity_history_item_id", activity_history_item_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, '{object}')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    set_ref_activity.metadata = {'url': '/users/{user-id}/activities/{userActivity-id}/historyItems/{activityHistoryItem-id}/activity/$ref'}  # type: ignore

    def delete_ref_activity(
        self,
        user_id,  # type: str
        user_activity_id,  # type: str
        activity_history_item_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete ref of navigation property activity for users.

        Delete ref of navigation property activity for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param user_activity_id: key: id of userActivity.
        :type user_activity_id: str
        :param activity_history_item_id: key: id of activityHistoryItem.
        :type activity_history_item_id: str
        :param if_match: ETag.
        :type if_match: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.delete_ref_activity.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'userActivity-id': self._serialize.url("user_activity_id", user_activity_id, 'str'),
            'activityHistoryItem-id': self._serialize.url("activity_history_item_id", activity_history_item_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete_ref_activity.metadata = {'url': '/users/{user-id}/activities/{userActivity-id}/historyItems/{activityHistoryItem-id}/activity/$ref'}  # type: ignore
