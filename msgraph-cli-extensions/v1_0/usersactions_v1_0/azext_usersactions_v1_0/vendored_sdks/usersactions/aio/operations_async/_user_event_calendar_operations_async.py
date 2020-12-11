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

class UserEventCalendarOperations:
    """UserEventCalendarOperations async operations.

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

    async def get_schedule(
        self,
        user_id: str,
        event_id: str,
        schedules: Optional[List[str]] = None,
        end_time: Optional["models.MicrosoftGraphDateTimeZone"] = None,
        start_time: Optional["models.MicrosoftGraphDateTimeZone"] = None,
        availability_view_interval: Optional[int] = None,
        **kwargs
    ) -> List["models.MicrosoftGraphScheduleInformation"]:
        """Invoke action getSchedule.

        Invoke action getSchedule.

        :param user_id: key: id of user.
        :type user_id: str
        :param event_id: key: id of event.
        :type event_id: str
        :param schedules:
        :type schedules: list[str]
        :param end_time: dateTimeTimeZone.
        :type end_time: ~users_actions.models.MicrosoftGraphDateTimeZone
        :param start_time: dateTimeTimeZone.
        :type start_time: ~users_actions.models.MicrosoftGraphDateTimeZone
        :param availability_view_interval:
        :type availability_view_interval: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: list of MicrosoftGraphScheduleInformation, or the result of cls(response)
        :rtype: list[~users_actions.models.MicrosoftGraphScheduleInformation]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[List["models.MicrosoftGraphScheduleInformation"]]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.Paths11Iq6NwUsersUserIdEventsEventIdCalendarMicrosoftGraphGetschedulePostRequestbodyContentApplicationJsonSchema(schedules=schedules, end_time=end_time, start_time=start_time, availability_view_interval=availability_view_interval)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.get_schedule.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'event-id': self._serialize.url("event_id", event_id, 'str'),
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
        body_content = self._serialize.body(_body, 'Paths11Iq6NwUsersUserIdEventsEventIdCalendarMicrosoftGraphGetschedulePostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('[MicrosoftGraphScheduleInformation]', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_schedule.metadata = {'url': '/users/{user-id}/events/{event-id}/calendar/microsoft.graph.getSchedule'}  # type: ignore
