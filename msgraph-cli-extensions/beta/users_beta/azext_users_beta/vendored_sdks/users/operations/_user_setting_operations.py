# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class UserSettingOperations(object):
    """UserSettingOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~users.models
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

    def get_regional_and_language_setting(
        self,
        user_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum230"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphRegionalAndLanguageSettings"
        """Get regionalAndLanguageSettings from users.

        Get regionalAndLanguageSettings from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~users.models.Enum230]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphRegionalAndLanguageSettings, or the result of cls(response)
        :rtype: ~users.models.MicrosoftGraphRegionalAndLanguageSettings
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphRegionalAndLanguageSettings"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_regional_and_language_setting.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphRegionalAndLanguageSettings', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_regional_and_language_setting.metadata = {'url': '/users/{user-id}/settings/regionalAndLanguageSettings'}  # type: ignore

    def update_regional_and_language_setting(
        self,
        user_id,  # type: str
        id=None,  # type: Optional[str]
        authoring_languages=None,  # type: Optional[List["models.MicrosoftGraphLocaleInfo"]]
        default_display_language=None,  # type: Optional["models.MicrosoftGraphLocaleInfo"]
        default_regional_format=None,  # type: Optional["models.MicrosoftGraphLocaleInfo"]
        default_speech_input_language=None,  # type: Optional["models.MicrosoftGraphLocaleInfo"]
        default_translation_language=None,  # type: Optional["models.MicrosoftGraphLocaleInfo"]
        regional_format_overrides=None,  # type: Optional["models.MicrosoftGraphRegionalFormatOverrides"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property regionalAndLanguageSettings in users.

        Update the navigation property regionalAndLanguageSettings in users.

        :param user_id: key: id of user.
        :type user_id: str
        :param id: Read-only.
        :type id: str
        :param authoring_languages:
        :type authoring_languages: list[~users.models.MicrosoftGraphLocaleInfo]
        :param default_display_language: localeInfo.
        :type default_display_language: ~users.models.MicrosoftGraphLocaleInfo
        :param default_regional_format: localeInfo.
        :type default_regional_format: ~users.models.MicrosoftGraphLocaleInfo
        :param default_speech_input_language: localeInfo.
        :type default_speech_input_language: ~users.models.MicrosoftGraphLocaleInfo
        :param default_translation_language: localeInfo.
        :type default_translation_language: ~users.models.MicrosoftGraphLocaleInfo
        :param regional_format_overrides: regionalFormatOverrides.
        :type regional_format_overrides: ~users.models.MicrosoftGraphRegionalFormatOverrides
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphRegionalAndLanguageSettings(id=id, authoring_languages=authoring_languages, default_display_language=default_display_language, default_regional_format=default_regional_format, default_speech_input_language=default_speech_input_language, default_translation_language=default_translation_language, regional_format_overrides=regional_format_overrides)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_regional_and_language_setting.metadata['url']  # type: ignore
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
        body_content = self._serialize.body(_body, 'MicrosoftGraphRegionalAndLanguageSettings')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_regional_and_language_setting.metadata = {'url': '/users/{user-id}/settings/regionalAndLanguageSettings'}  # type: ignore

    def delete_regional_and_language_setting(
        self,
        user_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property regionalAndLanguageSettings for users.

        Delete navigation property regionalAndLanguageSettings for users.

        :param user_id: key: id of user.
        :type user_id: str
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
        url = self.delete_regional_and_language_setting.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
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

    delete_regional_and_language_setting.metadata = {'url': '/users/{user-id}/settings/regionalAndLanguageSettings'}  # type: ignore

    def get_shift_preference(
        self,
        user_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum231"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphShiftPreferences"
        """Get shiftPreferences from users.

        Get shiftPreferences from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~users.models.Enum231]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphShiftPreferences, or the result of cls(response)
        :rtype: ~users.models.MicrosoftGraphShiftPreferences
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphShiftPreferences"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_shift_preference.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
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
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphShiftPreferences', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_shift_preference.metadata = {'url': '/users/{user-id}/settings/shiftPreferences'}  # type: ignore

    def update_shift_preference(
        self,
        user_id,  # type: str
        id=None,  # type: Optional[str]
        created_date_time=None,  # type: Optional[datetime.datetime]
        last_modified_date_time=None,  # type: Optional[datetime.datetime]
        application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        availability=None,  # type: Optional[List["models.MicrosoftGraphShiftAvailability"]]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property shiftPreferences in users.

        Update the navigation property shiftPreferences in users.

        :param user_id: key: id of user.
        :type user_id: str
        :param id: Read-only.
        :type id: str
        :param created_date_time: The Timestamp type represents date and time information using ISO
         8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like
         this: '2014-01-01T00:00:00Z'.
        :type created_date_time: ~datetime.datetime
        :param last_modified_date_time: The Timestamp type represents date and time information using
         ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look
         like this: '2014-01-01T00:00:00Z'.
        :type last_modified_date_time: ~datetime.datetime
        :param application: identity.
        :type application: ~users.models.MicrosoftGraphIdentity
        :param device: identity.
        :type device: ~users.models.MicrosoftGraphIdentity
        :param user: identity.
        :type user: ~users.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_application: identity.
        :type microsoft_graph_identity_application: ~users.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_device: identity.
        :type microsoft_graph_identity_device: ~users.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_user: identity.
        :type microsoft_graph_identity_user: ~users.models.MicrosoftGraphIdentity
        :param availability: Availability of the user to be scheduled for work and its recurrence
         pattern.
        :type availability: list[~users.models.MicrosoftGraphShiftAvailability]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphShiftPreferences(id=id, created_date_time=created_date_time, last_modified_date_time=last_modified_date_time, application_last_modified_by_application=application, device_last_modified_by_device=device, user_last_modified_by_user=user, application_created_by_application=microsoft_graph_identity_application, device_created_by_device=microsoft_graph_identity_device, user_created_by_user=microsoft_graph_identity_user, availability=availability)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_shift_preference.metadata['url']  # type: ignore
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
        body_content = self._serialize.body(_body, 'MicrosoftGraphShiftPreferences')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    update_shift_preference.metadata = {'url': '/users/{user-id}/settings/shiftPreferences'}  # type: ignore

    def delete_shift_preference(
        self,
        user_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property shiftPreferences for users.

        Delete navigation property shiftPreferences for users.

        :param user_id: key: id of user.
        :type user_id: str
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
        url = self.delete_shift_preference.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
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

    delete_shift_preference.metadata = {'url': '/users/{user-id}/settings/shiftPreferences'}  # type: ignore
