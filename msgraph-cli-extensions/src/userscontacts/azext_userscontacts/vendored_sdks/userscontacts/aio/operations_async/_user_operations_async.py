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

class UserOperations:
    """UserOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users_contacts.models
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

    def list_contact_folder(
        self,
        user_id: str,
        orderby: Optional[List[Union[str, "models.Get6ItemsItem"]]] = None,
        select: Optional[List[Union[str, "models.Get7ItemsItem"]]] = None,
        expand: Optional[List[Union[str, "models.Get8ItemsItem"]]] = None,
        **kwargs
    ) -> AsyncIterable["models.CollectionOfContactFolder"]:
        """Get contactFolders from users.

        Get contactFolders from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~users_contacts.models.Get6ItemsItem]
        :param select: Select properties to be returned.
        :type select: list[str or ~users_contacts.models.Get7ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str or ~users_contacts.models.Get8ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfContactFolder or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~users_contacts.models.CollectionOfContactFolder]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfContactFolder"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_contact_folder.metadata['url']  # type: ignore
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
            deserialized = self._deserialize('CollectionOfContactFolder', pipeline_response)
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
    list_contact_folder.metadata = {'url': '/users/{user-id}/contactFolders'}  # type: ignore

    async def create_contact_folder(
        self,
        user_id: str,
        id: Optional[str] = None,
        parent_folder_id: Optional[str] = None,
        display_name: Optional[str] = None,
        well_known_name: Optional[str] = None,
        single_value_extended_properties: Optional[List["models.MicrosoftGraphSingleValueLegacyExtendedProperty"]] = None,
        multi_value_extended_properties: Optional[List["models.MicrosoftGraphMultiValueLegacyExtendedProperty"]] = None,
        contacts: Optional[List["models.MicrosoftGraphContact"]] = None,
        child_folders: Optional[List["models.MicrosoftGraphContactFolder"]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphContactFolder":
        """Create new navigation property to contactFolders for users.

        Create new navigation property to contactFolders for users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param id: Read-only.
        :type id: str
        :param parent_folder_id: The ID of the folder's parent folder.
        :type parent_folder_id: str
        :param display_name: The folder's display name.
        :type display_name: str
        :param well_known_name:
        :type well_known_name: str
        :param single_value_extended_properties: The collection of single-value extended properties
         defined for the contactFolder. Read-only. Nullable.
        :type single_value_extended_properties: list[~users_contacts.models.MicrosoftGraphSingleValueLegacyExtendedProperty]
        :param multi_value_extended_properties: The collection of multi-value extended properties
         defined for the contactFolder. Read-only. Nullable.
        :type multi_value_extended_properties: list[~users_contacts.models.MicrosoftGraphMultiValueLegacyExtendedProperty]
        :param contacts: The contacts in the folder. Navigation property. Read-only. Nullable.
        :type contacts: list[~users_contacts.models.MicrosoftGraphContact]
        :param child_folders: The collection of child folders in the folder. Navigation property. Read-
         only. Nullable.
        :type child_folders: list[~users_contacts.models.MicrosoftGraphContactFolder]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphContactFolder, or the result of cls(response)
        :rtype: ~users_contacts.models.MicrosoftGraphContactFolder
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphContactFolder"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphContactFolder(id=id, parent_folder_id=parent_folder_id, display_name=display_name, well_known_name=well_known_name, single_value_extended_properties=single_value_extended_properties, multi_value_extended_properties=multi_value_extended_properties, contacts=contacts, child_folders=child_folders)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_contact_folder.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphContactFolder')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphContactFolder', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_contact_folder.metadata = {'url': '/users/{user-id}/contactFolders'}  # type: ignore

    async def get_contact_folder(
        self,
        user_id: str,
        contact_folder_id: str,
        select: Optional[List[Union[str, "models.Get2ItemsItem"]]] = None,
        expand: Optional[List[Union[str, "models.Get3ItemsItem"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphContactFolder":
        """Get contactFolders from users.

        Get contactFolders from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param contact_folder_id: key: contactFolder-id of contactFolder.
        :type contact_folder_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~users_contacts.models.Get2ItemsItem]
        :param expand: Expand related entities.
        :type expand: list[str or ~users_contacts.models.Get3ItemsItem]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphContactFolder, or the result of cls(response)
        :rtype: ~users_contacts.models.MicrosoftGraphContactFolder
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphContactFolder"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_contact_folder.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'contactFolder-id': self._serialize.url("contact_folder_id", contact_folder_id, 'str'),
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
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphContactFolder', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_contact_folder.metadata = {'url': '/users/{user-id}/contactFolders/{contactFolder-id}'}  # type: ignore

    async def update_contact_folder(
        self,
        user_id: str,
        contact_folder_id: str,
        id: Optional[str] = None,
        parent_folder_id: Optional[str] = None,
        display_name: Optional[str] = None,
        well_known_name: Optional[str] = None,
        single_value_extended_properties: Optional[List["models.MicrosoftGraphSingleValueLegacyExtendedProperty"]] = None,
        multi_value_extended_properties: Optional[List["models.MicrosoftGraphMultiValueLegacyExtendedProperty"]] = None,
        contacts: Optional[List["models.MicrosoftGraphContact"]] = None,
        child_folders: Optional[List["models.MicrosoftGraphContactFolder"]] = None,
        **kwargs
    ) -> None:
        """Update the navigation property contactFolders in users.

        Update the navigation property contactFolders in users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param contact_folder_id: key: contactFolder-id of contactFolder.
        :type contact_folder_id: str
        :param id: Read-only.
        :type id: str
        :param parent_folder_id: The ID of the folder's parent folder.
        :type parent_folder_id: str
        :param display_name: The folder's display name.
        :type display_name: str
        :param well_known_name:
        :type well_known_name: str
        :param single_value_extended_properties: The collection of single-value extended properties
         defined for the contactFolder. Read-only. Nullable.
        :type single_value_extended_properties: list[~users_contacts.models.MicrosoftGraphSingleValueLegacyExtendedProperty]
        :param multi_value_extended_properties: The collection of multi-value extended properties
         defined for the contactFolder. Read-only. Nullable.
        :type multi_value_extended_properties: list[~users_contacts.models.MicrosoftGraphMultiValueLegacyExtendedProperty]
        :param contacts: The contacts in the folder. Navigation property. Read-only. Nullable.
        :type contacts: list[~users_contacts.models.MicrosoftGraphContact]
        :param child_folders: The collection of child folders in the folder. Navigation property. Read-
         only. Nullable.
        :type child_folders: list[~users_contacts.models.MicrosoftGraphContactFolder]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphContactFolder(id=id, parent_folder_id=parent_folder_id, display_name=display_name, well_known_name=well_known_name, single_value_extended_properties=single_value_extended_properties, multi_value_extended_properties=multi_value_extended_properties, contacts=contacts, child_folders=child_folders)
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_contact_folder.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'contactFolder-id': self._serialize.url("contact_folder_id", contact_folder_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphContactFolder')
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

    update_contact_folder.metadata = {'url': '/users/{user-id}/contactFolders/{contactFolder-id}'}  # type: ignore

    def list_contact(
        self,
        user_id: str,
        orderby: Optional[List[Union[str, "models.Enum34"]]] = None,
        select: Optional[List[Union[str, "models.Enum35"]]] = None,
        expand: Optional[List[Union[str, "models.Enum36"]]] = None,
        **kwargs
    ) -> AsyncIterable["models.CollectionOfContact0"]:
        """Get contacts from users.

        Get contacts from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~users_contacts.models.Enum34]
        :param select: Select properties to be returned.
        :type select: list[str or ~users_contacts.models.Enum35]
        :param expand: Expand related entities.
        :type expand: list[str or ~users_contacts.models.Enum36]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfContact0 or the result of cls(response)
        :rtype: ~azure.core.async_paging.AsyncItemPaged[~users_contacts.models.CollectionOfContact0]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfContact0"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        def prepare_request(next_link=None):
            # Construct headers
            header_parameters = {}  # type: Dict[str, Any]
            header_parameters['Accept'] = 'application/json'

            if not next_link:
                # Construct URL
                url = self.list_contact.metadata['url']  # type: ignore
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
            deserialized = self._deserialize('CollectionOfContact0', pipeline_response)
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
    list_contact.metadata = {'url': '/users/{user-id}/contacts'}  # type: ignore

    async def create_contact(
        self,
        user_id: str,
        body: "models.MicrosoftGraphContact",
        **kwargs
    ) -> "models.MicrosoftGraphContact":
        """Create new navigation property to contacts for users.

        Create new navigation property to contacts for users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param body: New navigation property.
        :type body: ~users_contacts.models.MicrosoftGraphContact
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphContact, or the result of cls(response)
        :rtype: ~users_contacts.models.MicrosoftGraphContact
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphContact"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.create_contact.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = 'application/json'

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphContact')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphContact', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_contact.metadata = {'url': '/users/{user-id}/contacts'}  # type: ignore

    async def get_contact(
        self,
        user_id: str,
        contact_id: str,
        select: Optional[List[Union[str, "models.Enum37"]]] = None,
        expand: Optional[List[Union[str, "models.Enum38"]]] = None,
        **kwargs
    ) -> "models.MicrosoftGraphContact":
        """Get contacts from users.

        Get contacts from users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param contact_id: key: contact-id of contact.
        :type contact_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~users_contacts.models.Enum37]
        :param expand: Expand related entities.
        :type expand: list[str or ~users_contacts.models.Enum38]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphContact, or the result of cls(response)
        :rtype: ~users_contacts.models.MicrosoftGraphContact
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphContact"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        # Construct URL
        url = self.get_contact.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'contact-id': self._serialize.url("contact_id", contact_id, 'str'),
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
        header_parameters['Accept'] = 'application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphContact', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_contact.metadata = {'url': '/users/{user-id}/contacts/{contact-id}'}  # type: ignore

    async def update_contact(
        self,
        user_id: str,
        contact_id: str,
        body: "models.MicrosoftGraphContact",
        **kwargs
    ) -> None:
        """Update the navigation property contacts in users.

        Update the navigation property contacts in users.

        :param user_id: key: user-id of user.
        :type user_id: str
        :param contact_id: key: contact-id of contact.
        :type contact_id: str
        :param body: New navigation property values.
        :type body: ~users_contacts.models.MicrosoftGraphContact
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")

        # Construct URL
        url = self.update_contact.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'contact-id': self._serialize.url("contact_id", contact_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphContact')
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

    update_contact.metadata = {'url': '/users/{user-id}/contacts/{contact-id}'}  # type: ignore
