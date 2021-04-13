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
from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class UserOperations:
    """UserOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~cloud_communications.models
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

    def list_online_meeting(
        self,
        user_id: str,
        orderby: Optional[List[Union[str, "models.Get6ItemsItem"]]] = None,
        select: Optional[List[Union[str, "models.Get7ItemsItem"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> AsyncIterable["models.CollectionOfOnlineMeeting"]:
        """Get onlineMeetings from users.

        Get onlineMeetings from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~cloud_communications.models.Get6ItemsItem]
        :param select: Select properties to be returned.
        :type select: list[str or ~cloud_communications.models.Get7ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfOnlineMeeting or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~cloud_communications.models.CollectionOfOnlineMeeting]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfOnlineMeeting"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

            if not next_link:
                # Construct URL
                url = self.list_online_meeting.metadata['url']  # type: ignore
                path_format_arguments = {
                    'user-id': self._serialize.url("user_id", user_id, 'str'),
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
            deserialized = self._deserialize('CollectionOfOnlineMeeting', pipeline_response)
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
    list_online_meeting.metadata = {'url': '/users/{user-id}/onlineMeetings'}  # type: ignore

    async def create_online_meeting(
        self,
        user_id: str,
        id: Optional[str] = None,
        audio_conferencing: Optional["models.MicrosoftGraphAudioConferencing"] = None,
        chat_info: Optional["models.MicrosoftGraphChatInfo"] = None,
        creation_date_time: Optional[datetime.datetime] = None,
        end_date_time: Optional[datetime.datetime] = None,
        external_id: Optional[str] = None,
        join_information: Optional["models.MicrosoftGraphItemBody"] = None,
        join_web_url: Optional[str] = None,
        start_date_time: Optional[datetime.datetime] = None,
        subject: Optional[str] = None,
        video_teleconference_id: Optional[str] = None,
        attendees: Optional[List["models.MicrosoftGraphMeetingParticipantInfo"]] = None,
        organizer: Optional["models.MicrosoftGraphMeetingParticipantInfo"] = None,
        **kwargs
    ) -> "models.MicrosoftGraphOnlineMeeting":
        """Create new navigation property to onlineMeetings for users.

        Create new navigation property to onlineMeetings for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param id: Read-only.
        :type id: str
        :param audio_conferencing: audioConferencing.
        :type audio_conferencing: ~cloud_communications.models.MicrosoftGraphAudioConferencing
        :param chat_info: chatInfo.
        :type chat_info: ~cloud_communications.models.MicrosoftGraphChatInfo
        :param creation_date_time: The meeting creation time in UTC. Read-only.
        :type creation_date_time: ~datetime.datetime
        :param end_date_time: The meeting end time in UTC.
        :type end_date_time: ~datetime.datetime
        :param external_id:
        :type external_id: str
        :param join_information: itemBody.
        :type join_information: ~cloud_communications.models.MicrosoftGraphItemBody
        :param join_web_url: The join URL of the online meeting. Read-only.
        :type join_web_url: str
        :param start_date_time: The meeting start time in UTC.
        :type start_date_time: ~datetime.datetime
        :param subject: The subject of the online meeting.
        :type subject: str
        :param video_teleconference_id: The video teleconferencing ID. Read-only.
        :type video_teleconference_id: str
        :param attendees:
        :type attendees: list[~cloud_communications.models.MicrosoftGraphMeetingParticipantInfo]
        :param organizer: meetingParticipantInfo.
        :type organizer: ~cloud_communications.models.MicrosoftGraphMeetingParticipantInfo
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOnlineMeeting, or the result of cls(response)
        :rtype: ~cloud_communications.models.MicrosoftGraphOnlineMeeting
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOnlineMeeting"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        body = models.MicrosoftGraphOnlineMeeting(id=id, audio_conferencing=audio_conferencing, chat_info=chat_info, creation_date_time=creation_date_time, end_date_time=end_date_time, external_id=external_id, join_information=join_information, join_web_url=join_web_url, start_date_time=start_date_time, subject=subject, video_teleconference_id=video_teleconference_id, attendees=attendees, organizer=organizer)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_online_meeting.metadata['url']  # type: ignore
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

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphOnlineMeeting')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOnlineMeeting', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_online_meeting.metadata = {'url': '/users/{user-id}/onlineMeetings'}  # type: ignore

    async def get_online_meeting(
        self,
        user_id: str,
        online_meeting_id: str,
        select: Optional[List[Union[str, "models.Get2ItemsItem"]]] = None,
        expand: Optional[List[str]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphOnlineMeeting":
        """Get onlineMeetings from users.

        Get onlineMeetings from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param online_meeting_id: key: id of onlineMeeting.
        :type online_meeting_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~cloud_communications.models.Get2ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOnlineMeeting, or the result of cls(response)
        :rtype: ~cloud_communications.models.MicrosoftGraphOnlineMeeting
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOnlineMeeting"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_online_meeting.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'onlineMeeting-id': self._serialize.url("online_meeting_id", online_meeting_id, 'str'),
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
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOnlineMeeting', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_online_meeting.metadata = {'url': '/users/{user-id}/onlineMeetings/{onlineMeeting-id}'}  # type: ignore

    async def update_online_meeting(
        self,
        user_id: str,
        online_meeting_id: str,
        id: Optional[str] = None,
        audio_conferencing: Optional["models.MicrosoftGraphAudioConferencing"] = None,
        chat_info: Optional["models.MicrosoftGraphChatInfo"] = None,
        creation_date_time: Optional[datetime.datetime] = None,
        end_date_time: Optional[datetime.datetime] = None,
        external_id: Optional[str] = None,
        join_information: Optional["models.MicrosoftGraphItemBody"] = None,
        join_web_url: Optional[str] = None,
        start_date_time: Optional[datetime.datetime] = None,
        subject: Optional[str] = None,
        video_teleconference_id: Optional[str] = None,
        attendees: Optional[List["models.MicrosoftGraphMeetingParticipantInfo"]] = None,
        organizer: Optional["models.MicrosoftGraphMeetingParticipantInfo"] = None,
        **kwargs
    ) -> None:
        """Update the navigation property onlineMeetings in users.

        Update the navigation property onlineMeetings in users.

        :param user_id: key: id of user.
        :type user_id: str
        :param online_meeting_id: key: id of onlineMeeting.
        :type online_meeting_id: str
        :param id: Read-only.
        :type id: str
        :param audio_conferencing: audioConferencing.
        :type audio_conferencing: ~cloud_communications.models.MicrosoftGraphAudioConferencing
        :param chat_info: chatInfo.
        :type chat_info: ~cloud_communications.models.MicrosoftGraphChatInfo
        :param creation_date_time: The meeting creation time in UTC. Read-only.
        :type creation_date_time: ~datetime.datetime
        :param end_date_time: The meeting end time in UTC.
        :type end_date_time: ~datetime.datetime
        :param external_id:
        :type external_id: str
        :param join_information: itemBody.
        :type join_information: ~cloud_communications.models.MicrosoftGraphItemBody
        :param join_web_url: The join URL of the online meeting. Read-only.
        :type join_web_url: str
        :param start_date_time: The meeting start time in UTC.
        :type start_date_time: ~datetime.datetime
        :param subject: The subject of the online meeting.
        :type subject: str
        :param video_teleconference_id: The video teleconferencing ID. Read-only.
        :type video_teleconference_id: str
        :param attendees:
        :type attendees: list[~cloud_communications.models.MicrosoftGraphMeetingParticipantInfo]
        :param organizer: meetingParticipantInfo.
        :type organizer: ~cloud_communications.models.MicrosoftGraphMeetingParticipantInfo
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

        body = models.MicrosoftGraphOnlineMeeting(id=id, audio_conferencing=audio_conferencing, chat_info=chat_info, creation_date_time=creation_date_time, end_date_time=end_date_time, external_id=external_id, join_information=join_information, join_web_url=join_web_url, start_date_time=start_date_time, subject=subject, video_teleconference_id=video_teleconference_id, attendees=attendees, organizer=organizer)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_online_meeting.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'onlineMeeting-id': self._serialize.url("online_meeting_id", online_meeting_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphOnlineMeeting')
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

    update_online_meeting.metadata = {'url': '/users/{user-id}/onlineMeetings/{onlineMeeting-id}'}  # type: ignore

    async def delete_online_meeting(
        self,
        user_id: str,
        online_meeting_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property onlineMeetings for users.

        Delete navigation property onlineMeetings for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param online_meeting_id: key: id of onlineMeeting.
        :type online_meeting_id: str
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
        url = self.delete_online_meeting.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'onlineMeeting-id': self._serialize.url("online_meeting_id", online_meeting_id, 'str'),
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

    delete_online_meeting.metadata = {'url': '/users/{user-id}/onlineMeetings/{onlineMeeting-id}'}  # type: ignore
