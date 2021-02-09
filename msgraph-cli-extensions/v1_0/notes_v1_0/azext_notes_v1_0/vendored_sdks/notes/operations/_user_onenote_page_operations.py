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

class UserOnenotePageOperations(object):
    """UserOnenotePageOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~notes.models
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

    def get_parent_notebook(
        self,
        user_id,  # type: str
        onenote_page_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum809"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum810"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphNotebook"
        """Get parentNotebook from users.

        Get parentNotebook from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~notes.models.Enum809]
        :param expand: Expand related entities.
        :type expand: list[str or ~notes.models.Enum810]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphNotebook, or the result of cls(response)
        :rtype: ~notes.models.MicrosoftGraphNotebook
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphNotebook"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_parent_notebook.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphNotebook', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_parent_notebook.metadata = {'url': '/users/{user-id}/onenote/pages/{onenotePage-id}/parentNotebook'}  # type: ignore

    def update_parent_notebook(
        self,
        user_id,  # type: str
        onenote_page_id,  # type: str
        id=None,  # type: Optional[str]
        self_parameter=None,  # type: Optional[str]
        created_date_time=None,  # type: Optional[datetime.datetime]
        display_name=None,  # type: Optional[str]
        last_modified_date_time=None,  # type: Optional[datetime.datetime]
        application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        is_default=None,  # type: Optional[bool]
        is_shared=None,  # type: Optional[bool]
        section_groups_url=None,  # type: Optional[str]
        sections_url=None,  # type: Optional[str]
        user_role=None,  # type: Optional[Union[str, "models.MicrosoftGraphOnenoteUserRole"]]
        section_groups=None,  # type: Optional[List["models.MicrosoftGraphSectionGroup"]]
        sections=None,  # type: Optional[List["models.MicrosoftGraphOnenoteSection"]]
        one_note_client_url=None,  # type: Optional["models.MicrosoftGraphExternalLink"]
        one_note_web_url=None,  # type: Optional["models.MicrosoftGraphExternalLink"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property parentNotebook in users.

        Update the navigation property parentNotebook in users.

        :param user_id: key: id of user.
        :type user_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param id: Read-only.
        :type id: str
        :param self_parameter: The endpoint where you can get details about the page. Read-only.
        :type self_parameter: str
        :param created_date_time: The date and time when the page was created. The timestamp represents
         date and time information using ISO 8601 format and is always in UTC time. For example,
         midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.
        :type created_date_time: ~datetime.datetime
        :param display_name: The name of the notebook.
        :type display_name: str
        :param last_modified_date_time: The date and time when the notebook was last modified. The
         timestamp represents date and time information using ISO 8601 format and is always in UTC time.
         For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-
         only.
        :type last_modified_date_time: ~datetime.datetime
        :param application: identity.
        :type application: ~notes.models.MicrosoftGraphIdentity
        :param device: identity.
        :type device: ~notes.models.MicrosoftGraphIdentity
        :param user: identity.
        :type user: ~notes.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_application: identity.
        :type microsoft_graph_identity_application: ~notes.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_device: identity.
        :type microsoft_graph_identity_device: ~notes.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_user: identity.
        :type microsoft_graph_identity_user: ~notes.models.MicrosoftGraphIdentity
        :param is_default: Indicates whether this is the user's default notebook. Read-only.
        :type is_default: bool
        :param is_shared: Indicates whether the notebook is shared. If true, the contents of the
         notebook can be seen by people other than the owner. Read-only.
        :type is_shared: bool
        :param section_groups_url: The URL for the sectionGroups navigation property, which returns all
         the section groups in the notebook. Read-only.
        :type section_groups_url: str
        :param sections_url: The URL for the sections navigation property, which returns all the
         sections in the notebook. Read-only.
        :type sections_url: str
        :param user_role:
        :type user_role: str or ~notes.models.MicrosoftGraphOnenoteUserRole
        :param section_groups: The section groups in the notebook. Read-only. Nullable.
        :type section_groups: list[~notes.models.MicrosoftGraphSectionGroup]
        :param sections: The sections in the notebook. Read-only. Nullable.
        :type sections: list[~notes.models.MicrosoftGraphOnenoteSection]
        :param one_note_client_url: externalLink.
        :type one_note_client_url: ~notes.models.MicrosoftGraphExternalLink
        :param one_note_web_url: externalLink.
        :type one_note_web_url: ~notes.models.MicrosoftGraphExternalLink
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphNotebook(id=id, self_property=self_parameter, created_date_time=created_date_time, display_name=display_name, last_modified_date_time=last_modified_date_time, application_last_modified_by_application=application, device_last_modified_by_device=device, user_last_modified_by_user=user, application_created_by_application=microsoft_graph_identity_application, device_created_by_device=microsoft_graph_identity_device, user_created_by_user=microsoft_graph_identity_user, is_default=is_default, is_shared=is_shared, section_groups_url=section_groups_url, sections_url=sections_url, user_role=user_role, section_groups=section_groups, sections=sections, one_note_client_url=one_note_client_url, one_note_web_url=one_note_web_url)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_parent_notebook.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphNotebook')
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

    update_parent_notebook.metadata = {'url': '/users/{user-id}/onenote/pages/{onenotePage-id}/parentNotebook'}  # type: ignore

    def delete_parent_notebook(
        self,
        user_id,  # type: str
        onenote_page_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property parentNotebook for users.

        Delete navigation property parentNotebook for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
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
        url = self.delete_parent_notebook.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
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

    delete_parent_notebook.metadata = {'url': '/users/{user-id}/onenote/pages/{onenotePage-id}/parentNotebook'}  # type: ignore

    def get_parent_section(
        self,
        user_id,  # type: str
        onenote_page_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum867"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum868"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphOnenoteSection"
        """Get parentSection from users.

        Get parentSection from users.

        :param user_id: key: id of user.
        :type user_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~notes.models.Enum867]
        :param expand: Expand related entities.
        :type expand: list[str or ~notes.models.Enum868]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOnenoteSection, or the result of cls(response)
        :rtype: ~notes.models.MicrosoftGraphOnenoteSection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOnenoteSection"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_parent_section.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphOnenoteSection', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_parent_section.metadata = {'url': '/users/{user-id}/onenote/pages/{onenotePage-id}/parentSection'}  # type: ignore

    def update_parent_section(
        self,
        user_id,  # type: str
        onenote_page_id,  # type: str
        id=None,  # type: Optional[str]
        self_parameter=None,  # type: Optional[str]
        created_date_time=None,  # type: Optional[datetime.datetime]
        display_name=None,  # type: Optional[str]
        last_modified_date_time=None,  # type: Optional[datetime.datetime]
        application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_application=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_device=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        microsoft_graph_identity_user=None,  # type: Optional["models.MicrosoftGraphIdentity"]
        is_default=None,  # type: Optional[bool]
        pages_url=None,  # type: Optional[str]
        pages=None,  # type: Optional[List["models.MicrosoftGraphOnenotePage"]]
        parent_notebook=None,  # type: Optional["models.MicrosoftGraphNotebook"]
        parent_section_group=None,  # type: Optional["models.MicrosoftGraphSectionGroup"]
        one_note_client_url=None,  # type: Optional["models.MicrosoftGraphExternalLink"]
        one_note_web_url=None,  # type: Optional["models.MicrosoftGraphExternalLink"]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property parentSection in users.

        Update the navigation property parentSection in users.

        :param user_id: key: id of user.
        :type user_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param id: Read-only.
        :type id: str
        :param self_parameter: The endpoint where you can get details about the page. Read-only.
        :type self_parameter: str
        :param created_date_time: The date and time when the page was created. The timestamp represents
         date and time information using ISO 8601 format and is always in UTC time. For example,
         midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-only.
        :type created_date_time: ~datetime.datetime
        :param display_name: The name of the notebook.
        :type display_name: str
        :param last_modified_date_time: The date and time when the notebook was last modified. The
         timestamp represents date and time information using ISO 8601 format and is always in UTC time.
         For example, midnight UTC on Jan 1, 2014 would look like this: '2014-01-01T00:00:00Z'. Read-
         only.
        :type last_modified_date_time: ~datetime.datetime
        :param application: identity.
        :type application: ~notes.models.MicrosoftGraphIdentity
        :param device: identity.
        :type device: ~notes.models.MicrosoftGraphIdentity
        :param user: identity.
        :type user: ~notes.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_application: identity.
        :type microsoft_graph_identity_application: ~notes.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_device: identity.
        :type microsoft_graph_identity_device: ~notes.models.MicrosoftGraphIdentity
        :param microsoft_graph_identity_user: identity.
        :type microsoft_graph_identity_user: ~notes.models.MicrosoftGraphIdentity
        :param is_default: Indicates whether this is the user's default section. Read-only.
        :type is_default: bool
        :param pages_url: The pages endpoint where you can get details for all the pages in the
         section. Read-only.
        :type pages_url: str
        :param pages: The collection of pages in the section.  Read-only. Nullable.
        :type pages: list[~notes.models.MicrosoftGraphOnenotePage]
        :param parent_notebook: notebook.
        :type parent_notebook: ~notes.models.MicrosoftGraphNotebook
        :param parent_section_group: sectionGroup.
        :type parent_section_group: ~notes.models.MicrosoftGraphSectionGroup
        :param one_note_client_url: externalLink.
        :type one_note_client_url: ~notes.models.MicrosoftGraphExternalLink
        :param one_note_web_url: externalLink.
        :type one_note_web_url: ~notes.models.MicrosoftGraphExternalLink
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphOnenoteSection(id=id, self_property=self_parameter, created_date_time=created_date_time, display_name=display_name, last_modified_date_time=last_modified_date_time, application_last_modified_by_application=application, device_last_modified_by_device=device, user_last_modified_by_user=user, application_created_by_application=microsoft_graph_identity_application, device_created_by_device=microsoft_graph_identity_device, user_created_by_user=microsoft_graph_identity_user, is_default=is_default, pages_url=pages_url, pages=pages, parent_notebook=parent_notebook, parent_section_group=parent_section_group, one_note_client_url=one_note_client_url, one_note_web_url=one_note_web_url)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_parent_section.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphOnenoteSection')
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

    update_parent_section.metadata = {'url': '/users/{user-id}/onenote/pages/{onenotePage-id}/parentSection'}  # type: ignore

    def delete_parent_section(
        self,
        user_id,  # type: str
        onenote_page_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property parentSection for users.

        Delete navigation property parentSection for users.

        :param user_id: key: id of user.
        :type user_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
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
        url = self.delete_parent_section.metadata['url']  # type: ignore
        path_format_arguments = {
            'user-id': self._serialize.url("user_id", user_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
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

    delete_parent_section.metadata = {'url': '/users/{user-id}/onenote/pages/{onenotePage-id}/parentSection'}  # type: ignore
