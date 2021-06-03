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
    from typing import Any, Callable, Dict, Generic, Optional, TypeVar

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SitesOnenoteSectionGroupsSectionsPagesOperations(object):
    """SitesOnenoteSectionGroupsSectionsPagesOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~sites.models
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

    def copy_to_section(
        self,
        site_id,  # type: str
        section_group_id,  # type: str
        onenote_section_id,  # type: str
        onenote_page_id,  # type: str
        body,  # type: "models.Paths169Srg3SitesSiteIdOnenoteSectiongroupsSectiongroupIdSectionsOnenotesectionIdPagesOnenotepageIdMicrosoftGraphCopytosectionPostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphOnenoteOperation"
        """Invoke action copyToSection.

        Invoke action copyToSection.

        :param site_id: key: id of site.
        :type site_id: str
        :param section_group_id: key: id of sectionGroup.
        :type section_group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param body: Action parameters.
        :type body: ~sites.models.Paths169Srg3SitesSiteIdOnenoteSectiongroupsSectiongroupIdSectionsOnenotesectionIdPagesOnenotepageIdMicrosoftGraphCopytosectionPostRequestbodyContentApplicationJsonSchema
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOnenoteOperation, or the result of cls(response)
        :rtype: ~sites.models.MicrosoftGraphOnenoteOperation
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOnenoteOperation"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.copy_to_section.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'sectionGroup-id': self._serialize.url("section_group_id", section_group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
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
        body_content = self._serialize.body(body, 'Paths169Srg3SitesSiteIdOnenoteSectiongroupsSectiongroupIdSectionsOnenotesectionIdPagesOnenotepageIdMicrosoftGraphCopytosectionPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphOnenoteOperation', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    copy_to_section.metadata = {'url': '/sites/{site-id}/onenote/sectionGroups/{sectionGroup-id}/sections/{onenoteSection-id}/pages/{onenotePage-id}/microsoft.graph.copyToSection'}  # type: ignore

    def onenote_patch_content(
        self,
        site_id,  # type: str
        section_group_id,  # type: str
        onenote_section_id,  # type: str
        onenote_page_id,  # type: str
        body,  # type: "models.Paths7M7NkoSitesSiteIdOnenoteSectiongroupsSectiongroupIdSectionsOnenotesectionIdPagesOnenotepageIdMicrosoftGraphOnenotepatchcontentPostRequestbodyContentApplicationJsonSchema"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Invoke action onenotePatchContent.

        Invoke action onenotePatchContent.

        :param site_id: key: id of site.
        :type site_id: str
        :param section_group_id: key: id of sectionGroup.
        :type section_group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :param body: Action parameters.
        :type body: ~sites.models.Paths7M7NkoSitesSiteIdOnenoteSectiongroupsSectiongroupIdSectionsOnenotesectionIdPagesOnenotepageIdMicrosoftGraphOnenotepatchcontentPostRequestbodyContentApplicationJsonSchema
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
        url = self.onenote_patch_content.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'sectionGroup-id': self._serialize.url("section_group_id", section_group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
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
        body_content = self._serialize.body(body, 'Paths7M7NkoSitesSiteIdOnenoteSectiongroupsSectiongroupIdSectionsOnenotesectionIdPagesOnenotepageIdMicrosoftGraphOnenotepatchcontentPostRequestbodyContentApplicationJsonSchema')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    onenote_patch_content.metadata = {'url': '/sites/{site-id}/onenote/sectionGroups/{sectionGroup-id}/sections/{onenoteSection-id}/pages/{onenotePage-id}/microsoft.graph.onenotePatchContent'}  # type: ignore

    def preview(
        self,
        site_id,  # type: str
        section_group_id,  # type: str
        onenote_section_id,  # type: str
        onenote_page_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphOnenotePagePreview"
        """Invoke function preview.

        Invoke function preview.

        :param site_id: key: id of site.
        :type site_id: str
        :param section_group_id: key: id of sectionGroup.
        :type section_group_id: str
        :param onenote_section_id: key: id of onenoteSection.
        :type onenote_section_id: str
        :param onenote_page_id: key: id of onenotePage.
        :type onenote_page_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphOnenotePagePreview, or the result of cls(response)
        :rtype: ~sites.models.MicrosoftGraphOnenotePagePreview
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphOnenotePagePreview"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.preview.metadata['url']  # type: ignore
        path_format_arguments = {
            'site-id': self._serialize.url("site_id", site_id, 'str'),
            'sectionGroup-id': self._serialize.url("section_group_id", section_group_id, 'str'),
            'onenoteSection-id': self._serialize.url("onenote_section_id", onenote_section_id, 'str'),
            'onenotePage-id': self._serialize.url("onenote_page_id", onenote_page_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphOnenotePagePreview', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    preview.metadata = {'url': '/sites/{site-id}/onenote/sectionGroups/{sectionGroup-id}/sections/{onenoteSection-id}/pages/{onenotePage-id}/microsoft.graph.preview()'}  # type: ignore
