# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
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

class UserCalendarGroupOperations:
    """UserCalendarGroupOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~calendar.models
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

    def list_calendar(
        self,
        user_id: str,
        calendar_group_id: str,
        orderby: Optional[List[Union[str, "models.Enum248"]]] = None,
        select: Optional[List[Union[str, "models.Enum249"]]] = None,
        expand: Optional[List[Union[str, "models.Enum250"]]] = None,
        **kwargs
    ) -> AsyncIterable["models.CollectionOfCalendar"]:
        """Get calendars from users.

        Get calendars from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param calendar_group_id: key: id of calendarGroup.
        :type calendar_group_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~calendar.models.Enum248]
        :param select: Select properties to be returned.
        :type select: list[str or ~calendar.models.Enum249]
        :param expand: Expand related entities.
        :type expand: list[str or ~calendar.models.Enum250]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfCalendar or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~calendar.models.CollectionOfCalendar]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfCalendar"]
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
                url = self.list_calendar.metadata['url']  # type: ignore
                path_format_arguments = {
                    'user-id': self._serialize.url("user_id", user_id, 'str'),
                    'calendarGroup-id': self._serialize.url("calendar_group_id", calendar_group_id, 'str'),
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
            deserialized = self._deserialize('CollectionOfCalendar', pipeline_response)
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
    list_calendar.metadata = {'url': '/users/{user-id}/calendarGroups/{calendarGroup-id}/calendars'}  # type: ignore

    async def create_calendar(
        self,
        user_id: str,
        calendar_group_id: str,
        id: Optional[str] = None,
        allowed_online_meeting_providers: Optional[List[Union[str, "models.MicrosoftGraphOnlineMeetingProviderType"]]] = None,
        microsoft_graph_calendar_group_id_calendar_group_id: Optional[str] = None,
        can_edit: Optional[bool] = None,
        can_share: Optional[bool] = None,
        can_view_private_items: Optional[bool] = None,
        change_key: Optional[str] = None,
        color: Optional[Union[str, "models.MicrosoftGraphCalendarColor"]] = None,
        default_online_meeting_provider: Optional[Union[str, "models.MicrosoftGraphOnlineMeetingProviderType"]] = None,
        hex_color: Optional[str] = None,
        is_default_calendar: Optional[bool] = None,
        is_removable: Optional[bool] = None,
        is_shared: Optional[bool] = None,
        is_shared_with_me: Optional[bool] = None,
        is_tallying_responses: Optional[bool] = None,
        name: Optional[str] = None,
        owner: Optional["models.MicrosoftGraphEmailAddress"] = None,
        calendar_permissions: Optional[List["models.MicrosoftGraphCalendarPermission"]] = None,
        calendar_view: Optional[List["models.MicrosoftGraphEvent"]] = None,
        events: Optional[List["models.MicrosoftGraphEvent"]] = None,
        multi_value_extended_properties: Optional[List["models.MicrosoftGraphMultiValueLegacyExtendedProperty"]] = None,
        single_value_extended_properties: Optional[List["models.MicrosoftGraphSingleValueLegacyExtendedProperty"]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphCalendar":
        """Create new navigation property to calendars for users.

        Create new navigation property to calendars for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param calendar_group_id: key: id of calendarGroup.
        :type calendar_group_id: str
        :param id: Read-only.
        :type id: str
        :param allowed_online_meeting_providers: Represent the online meeting service providers that
         can be used to create online meetings in this calendar. Possible values are: unknown,
         skypeForBusiness, skypeForConsumer, teamsForBusiness.
        :type allowed_online_meeting_providers: list[str or ~calendar.models.MicrosoftGraphOnlineMeetingProviderType]
        :param microsoft_graph_calendar_group_id_calendar_group_id:
        :type microsoft_graph_calendar_group_id_calendar_group_id: str
        :param can_edit: True if the user can write to the calendar, false otherwise. This property is
         true for the user who created the calendar. This property is also true for a user who has been
         shared a calendar and granted write access.
        :type can_edit: bool
        :param can_share: True if the user has the permission to share the calendar, false otherwise.
         Only the user who created the calendar can share it.
        :type can_share: bool
        :param can_view_private_items: True if the user can read calendar items that have been marked
         private, false otherwise.
        :type can_view_private_items: bool
        :param change_key: Identifies the version of the calendar object. Every time the calendar is
         changed, changeKey changes as well. This allows Exchange to apply changes to the correct
         version of the object. Read-only.
        :type change_key: str
        :param color:
        :type color: str or ~calendar.models.MicrosoftGraphCalendarColor
        :param default_online_meeting_provider:
        :type default_online_meeting_provider: str or ~calendar.models.MicrosoftGraphOnlineMeetingProviderType
        :param hex_color:
        :type hex_color: str
        :param is_default_calendar:
        :type is_default_calendar: bool
        :param is_removable: Indicates whether this user calendar can be deleted from the user mailbox.
        :type is_removable: bool
        :param is_shared:
        :type is_shared: bool
        :param is_shared_with_me:
        :type is_shared_with_me: bool
        :param is_tallying_responses: Indicates whether this user calendar supports tracking of meeting
         responses. Only meeting invites sent from users' primary calendars support tracking of meeting
         responses.
        :type is_tallying_responses: bool
        :param name: The calendar name.
        :type name: str
        :param owner: emailAddress.
        :type owner: ~calendar.models.MicrosoftGraphEmailAddress
        :param calendar_permissions: The permissions of the users with whom the calendar is shared.
        :type calendar_permissions: list[~calendar.models.MicrosoftGraphCalendarPermission]
        :param calendar_view: The calendar view for the calendar. Navigation property. Read-only.
        :type calendar_view: list[~calendar.models.MicrosoftGraphEvent]
        :param events: The events in the calendar. Navigation property. Read-only.
        :type events: list[~calendar.models.MicrosoftGraphEvent]
        :param multi_value_extended_properties: The collection of multi-value extended properties
         defined for the calendar. Read-only. Nullable.
        :type multi_value_extended_properties: list[~calendar.models.MicrosoftGraphMultiValueLegacyExtendedProperty]
        :param single_value_extended_properties: The collection of single-value extended properties
         defined for the calendar. Read-only. Nullable.
        :type single_value_extended_properties: list[~calendar.models.MicrosoftGraphSingleValueLegacyExtendedProperty]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphCalendar, or the result of cls(response)
        :rtype: ~calendar.models.MicrosoftGraphCalendar
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphCalendar"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphCalendar(id=id, allowed_online_meeting_providers=allowed_online_meeting_providers, calendar_group_id=microsoft_graph_calendar_group_id_calendar_group_id, can_edit=can_edit, can_share=can_share, can_view_private_items=can_view_private_items, change_key=change_key, color=color, default_online_meeting_provider=default_online_meeting_provider, hex_color=hex_color, is_default_calendar=is_default_calendar, is_removable=is_removable, is_shared=is_shared, is_shared_with_me=is_shared_with_me, is_tallying_responses=is_tallying_responses, name=name, owner=owner, calendar_permissions=calendar_permissions, calendar_view=calendar_view, events=events, multi_value_extended_properties=multi_value_extended_properties, single_value_extended_properties=single_value_extended_properties)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_calendar.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'calendarGroup-id': self._serialize.url("calendar_group_id", calendar_group_id, 'str'),
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
        body_content = self._serialize.body(_body, 'MicrosoftGraphCalendar')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphCalendar', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_calendar.metadata = {'url': '/users/{user-id}/calendarGroups/{calendarGroup-id}/calendars'}  # type: ignore

    async def get_calendar(
        self,
        user_id: str,
        calendar_group_id: str,
        calendar_id: str,
        select: Optional[List[Union[str, "models.Enum251"]]] = None,
        expand: Optional[List[Union[str, "models.Enum252"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphCalendar":
        """Get calendars from users.

        Get calendars from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param calendar_group_id: key: id of calendarGroup.
        :type calendar_group_id: str
        :param calendar_id: key: id of calendar.
        :type calendar_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~calendar.models.Enum251]
        :param expand: Expand related entities.
        :type expand: list[str or ~calendar.models.Enum252]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphCalendar, or the result of cls(response)
        :rtype: ~calendar.models.MicrosoftGraphCalendar
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphCalendar"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_calendar.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'calendarGroup-id': self._serialize.url("calendar_group_id", calendar_group_id, 'str'),
            'calendar-id': self._serialize.url("calendar_id", calendar_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphCalendar', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_calendar.metadata = {'url': '/users/{user-id}/calendarGroups/{calendarGroup-id}/calendars/{calendar-id}'}  # type: ignore

    async def update_calendar(
        self,
        user_id: str,
        calendar_group_id: str,
        calendar_id: str,
        id: Optional[str] = None,
        allowed_online_meeting_providers: Optional[List[Union[str, "models.MicrosoftGraphOnlineMeetingProviderType"]]] = None,
        microsoft_graph_calendar_group_id_calendar_group_id: Optional[str] = None,
        can_edit: Optional[bool] = None,
        can_share: Optional[bool] = None,
        can_view_private_items: Optional[bool] = None,
        change_key: Optional[str] = None,
        color: Optional[Union[str, "models.MicrosoftGraphCalendarColor"]] = None,
        default_online_meeting_provider: Optional[Union[str, "models.MicrosoftGraphOnlineMeetingProviderType"]] = None,
        hex_color: Optional[str] = None,
        is_default_calendar: Optional[bool] = None,
        is_removable: Optional[bool] = None,
        is_shared: Optional[bool] = None,
        is_shared_with_me: Optional[bool] = None,
        is_tallying_responses: Optional[bool] = None,
        name: Optional[str] = None,
        owner: Optional["models.MicrosoftGraphEmailAddress"] = None,
        calendar_permissions: Optional[List["models.MicrosoftGraphCalendarPermission"]] = None,
        calendar_view: Optional[List["models.MicrosoftGraphEvent"]] = None,
        events: Optional[List["models.MicrosoftGraphEvent"]] = None,
        multi_value_extended_properties: Optional[List["models.MicrosoftGraphMultiValueLegacyExtendedProperty"]] = None,
        single_value_extended_properties: Optional[List["models.MicrosoftGraphSingleValueLegacyExtendedProperty"]] = None,
        **kwargs
    ) -> None:
        """Update the navigation property calendars in users.

        Update the navigation property calendars in users.

        :param user_id: key: id of user.
        :type user_id: str
        :param calendar_group_id: key: id of calendarGroup.
        :type calendar_group_id: str
        :param calendar_id: key: id of calendar.
        :type calendar_id: str
        :param id: Read-only.
        :type id: str
        :param allowed_online_meeting_providers: Represent the online meeting service providers that
         can be used to create online meetings in this calendar. Possible values are: unknown,
         skypeForBusiness, skypeForConsumer, teamsForBusiness.
        :type allowed_online_meeting_providers: list[str or ~calendar.models.MicrosoftGraphOnlineMeetingProviderType]
        :param microsoft_graph_calendar_group_id_calendar_group_id:
        :type microsoft_graph_calendar_group_id_calendar_group_id: str
        :param can_edit: True if the user can write to the calendar, false otherwise. This property is
         true for the user who created the calendar. This property is also true for a user who has been
         shared a calendar and granted write access.
        :type can_edit: bool
        :param can_share: True if the user has the permission to share the calendar, false otherwise.
         Only the user who created the calendar can share it.
        :type can_share: bool
        :param can_view_private_items: True if the user can read calendar items that have been marked
         private, false otherwise.
        :type can_view_private_items: bool
        :param change_key: Identifies the version of the calendar object. Every time the calendar is
         changed, changeKey changes as well. This allows Exchange to apply changes to the correct
         version of the object. Read-only.
        :type change_key: str
        :param color:
        :type color: str or ~calendar.models.MicrosoftGraphCalendarColor
        :param default_online_meeting_provider:
        :type default_online_meeting_provider: str or ~calendar.models.MicrosoftGraphOnlineMeetingProviderType
        :param hex_color:
        :type hex_color: str
        :param is_default_calendar:
        :type is_default_calendar: bool
        :param is_removable: Indicates whether this user calendar can be deleted from the user mailbox.
        :type is_removable: bool
        :param is_shared:
        :type is_shared: bool
        :param is_shared_with_me:
        :type is_shared_with_me: bool
        :param is_tallying_responses: Indicates whether this user calendar supports tracking of meeting
         responses. Only meeting invites sent from users' primary calendars support tracking of meeting
         responses.
        :type is_tallying_responses: bool
        :param name: The calendar name.
        :type name: str
        :param owner: emailAddress.
        :type owner: ~calendar.models.MicrosoftGraphEmailAddress
        :param calendar_permissions: The permissions of the users with whom the calendar is shared.
        :type calendar_permissions: list[~calendar.models.MicrosoftGraphCalendarPermission]
        :param calendar_view: The calendar view for the calendar. Navigation property. Read-only.
        :type calendar_view: list[~calendar.models.MicrosoftGraphEvent]
        :param events: The events in the calendar. Navigation property. Read-only.
        :type events: list[~calendar.models.MicrosoftGraphEvent]
        :param multi_value_extended_properties: The collection of multi-value extended properties
         defined for the calendar. Read-only. Nullable.
        :type multi_value_extended_properties: list[~calendar.models.MicrosoftGraphMultiValueLegacyExtendedProperty]
        :param single_value_extended_properties: The collection of single-value extended properties
         defined for the calendar. Read-only. Nullable.
        :type single_value_extended_properties: list[~calendar.models.MicrosoftGraphSingleValueLegacyExtendedProperty]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphCalendar(id=id, allowed_online_meeting_providers=allowed_online_meeting_providers, calendar_group_id=microsoft_graph_calendar_group_id_calendar_group_id, can_edit=can_edit, can_share=can_share, can_view_private_items=can_view_private_items, change_key=change_key, color=color, default_online_meeting_provider=default_online_meeting_provider, hex_color=hex_color, is_default_calendar=is_default_calendar, is_removable=is_removable, is_shared=is_shared, is_shared_with_me=is_shared_with_me, is_tallying_responses=is_tallying_responses, name=name, owner=owner, calendar_permissions=calendar_permissions, calendar_view=calendar_view, events=events, multi_value_extended_properties=multi_value_extended_properties, single_value_extended_properties=single_value_extended_properties)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_calendar.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'calendarGroup-id': self._serialize.url("calendar_group_id", calendar_group_id, 'str'),
            'calendar-id': self._serialize.url("calendar_id", calendar_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphCalendar')
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

    update_calendar.metadata = {'url': '/users/{user-id}/calendarGroups/{calendarGroup-id}/calendars/{calendar-id}'}  # type: ignore

    async def delete_calendar(
        self,
        user_id: str,
        calendar_group_id: str,
        calendar_id: str,
        if_match: Optional[str] = None,
        **kwargs
    ) -> None:
        """Delete navigation property calendars for users.

        Delete navigation property calendars for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param calendar_group_id: key: id of calendarGroup.
        :type calendar_group_id: str
        :param calendar_id: key: id of calendar.
        :type calendar_id: str
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
        url = self.delete_calendar.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'calendarGroup-id': self._serialize.url("calendar_group_id", calendar_group_id, 'str'),
            'calendar-id': self._serialize.url("calendar_id", calendar_id, 'str'),
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

    delete_calendar.metadata = {'url': '/users/{user-id}/calendarGroups/{calendarGroup-id}/calendars/{calendar-id}'}  # type: ignore
