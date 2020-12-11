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
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, IO, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class FinancialCompanySaleQuoteSaleQuoteLineItemOperations(object):
    """FinancialCompanySaleQuoteSaleQuoteLineItemOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~financials.models
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

    def get_item_category(
        self,
        company_id,  # type: str
        sales_quote_id,  # type: str
        sales_quote_line_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum329"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphItemCategory"
        """Get itemCategory from financials.

        Get itemCategory from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_quote_id: key: id of salesQuote.
        :type sales_quote_id: str
        :param sales_quote_line_id: key: id of salesQuoteLine.
        :type sales_quote_line_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum329]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphItemCategory, or the result of cls(response)
        :rtype: ~financials.models.MicrosoftGraphItemCategory
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphItemCategory"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_item_category.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesQuote-id': self._serialize.url("sales_quote_id", sales_quote_id, 'str'),
            'salesQuoteLine-id': self._serialize.url("sales_quote_line_id", sales_quote_line_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphItemCategory', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_item_category.metadata = {'url': '/financials/companies/{company-id}/salesQuotes/{salesQuote-id}/salesQuoteLines/{salesQuoteLine-id}/item/itemCategory'}  # type: ignore

    def update_item_category(
        self,
        company_id,  # type: str
        sales_quote_id,  # type: str
        sales_quote_line_id,  # type: str
        id=None,  # type: Optional[str]
        code=None,  # type: Optional[str]
        display_name=None,  # type: Optional[str]
        last_modified_date_time=None,  # type: Optional[datetime.datetime]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property itemCategory in financials.

        Update the navigation property itemCategory in financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_quote_id: key: id of salesQuote.
        :type sales_quote_id: str
        :param sales_quote_line_id: key: id of salesQuoteLine.
        :type sales_quote_line_id: str
        :param id: Read-only.
        :type id: str
        :param code:
        :type code: str
        :param display_name:
        :type display_name: str
        :param last_modified_date_time:
        :type last_modified_date_time: ~datetime.datetime
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphItemCategory(id=id, code=code, display_name=display_name, last_modified_date_time=last_modified_date_time)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_item_category.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesQuote-id': self._serialize.url("sales_quote_id", sales_quote_id, 'str'),
            'salesQuoteLine-id': self._serialize.url("sales_quote_line_id", sales_quote_line_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphItemCategory')
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

    update_item_category.metadata = {'url': '/financials/companies/{company-id}/salesQuotes/{salesQuote-id}/salesQuoteLines/{salesQuoteLine-id}/item/itemCategory'}  # type: ignore

    def delete_item_category(
        self,
        company_id,  # type: str
        sales_quote_id,  # type: str
        sales_quote_line_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property itemCategory for financials.

        Delete navigation property itemCategory for financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_quote_id: key: id of salesQuote.
        :type sales_quote_id: str
        :param sales_quote_line_id: key: id of salesQuoteLine.
        :type sales_quote_line_id: str
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
        url = self.delete_item_category.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesQuote-id': self._serialize.url("sales_quote_id", sales_quote_id, 'str'),
            'salesQuoteLine-id': self._serialize.url("sales_quote_line_id", sales_quote_line_id, 'str'),
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

    delete_item_category.metadata = {'url': '/financials/companies/{company-id}/salesQuotes/{salesQuote-id}/salesQuoteLines/{salesQuoteLine-id}/item/itemCategory'}  # type: ignore

    def list_picture(
        self,
        company_id,  # type: str
        sales_quote_id,  # type: str
        sales_quote_line_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum330"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum331"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfPicture19"]
        """Get picture from financials.

        Get picture from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_quote_id: key: id of salesQuote.
        :type sales_quote_id: str
        :param sales_quote_line_id: key: id of salesQuoteLine.
        :type sales_quote_line_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~financials.models.Enum330]
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum331]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfPicture19 or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~financials.models.CollectionOfPicture19]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfPicture19"]
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
                url = self.list_picture.metadata['url']  # type: ignore
                path_format_arguments = {
                    'company-id': self._serialize.url("company_id", company_id, 'str'),
                    'salesQuote-id': self._serialize.url("sales_quote_id", sales_quote_id, 'str'),
                    'salesQuoteLine-id': self._serialize.url("sales_quote_line_id", sales_quote_line_id, 'str'),
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

        def extract_data(pipeline_response):
            deserialized = self._deserialize('CollectionOfPicture19', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.odata_next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                error = self._deserialize(models.OdataError, response)
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_picture.metadata = {'url': '/financials/companies/{company-id}/salesQuotes/{salesQuote-id}/salesQuoteLines/{salesQuoteLine-id}/item/picture'}  # type: ignore

    def create_picture(
        self,
        company_id,  # type: str
        sales_quote_id,  # type: str
        sales_quote_line_id,  # type: str
        id=None,  # type: Optional[str]
        content=None,  # type: Optional[bytes]
        content_type_parameter=None,  # type: Optional[str]
        height=None,  # type: Optional[int]
        width=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPicture"
        """Create new navigation property to picture for financials.

        Create new navigation property to picture for financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_quote_id: key: id of salesQuote.
        :type sales_quote_id: str
        :param sales_quote_line_id: key: id of salesQuoteLine.
        :type sales_quote_line_id: str
        :param id: Read-only.
        :type id: str
        :param content:
        :type content: bytes
        :param content_type_parameter:
        :type content_type_parameter: str
        :param height:
        :type height: int
        :param width:
        :type width: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPicture, or the result of cls(response)
        :rtype: ~financials.models.MicrosoftGraphPicture
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPicture"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPicture(id=id, content=content, content_type=content_type_parameter, height=height, width=width)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_picture.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesQuote-id': self._serialize.url("sales_quote_id", sales_quote_id, 'str'),
            'salesQuoteLine-id': self._serialize.url("sales_quote_line_id", sales_quote_line_id, 'str'),
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
        body_content = self._serialize.body(_body, 'MicrosoftGraphPicture')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPicture', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_picture.metadata = {'url': '/financials/companies/{company-id}/salesQuotes/{salesQuote-id}/salesQuoteLines/{salesQuoteLine-id}/item/picture'}  # type: ignore

    def get_picture(
        self,
        company_id,  # type: str
        sales_quote_id,  # type: str
        sales_quote_line_id,  # type: str
        picture_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum332"]]]
        expand=None,  # type: Optional[List[str]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPicture"
        """Get picture from financials.

        Get picture from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_quote_id: key: id of salesQuote.
        :type sales_quote_id: str
        :param sales_quote_line_id: key: id of salesQuoteLine.
        :type sales_quote_line_id: str
        :param picture_id: key: id of picture.
        :type picture_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~financials.models.Enum332]
        :param expand: Expand related entities.
        :type expand: list[str]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPicture, or the result of cls(response)
        :rtype: ~financials.models.MicrosoftGraphPicture
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPicture"]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_picture.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesQuote-id': self._serialize.url("sales_quote_id", sales_quote_id, 'str'),
            'salesQuoteLine-id': self._serialize.url("sales_quote_line_id", sales_quote_line_id, 'str'),
            'picture-id': self._serialize.url("picture_id", picture_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphPicture', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_picture.metadata = {'url': '/financials/companies/{company-id}/salesQuotes/{salesQuote-id}/salesQuoteLines/{salesQuoteLine-id}/item/picture/{picture-id}'}  # type: ignore

    def update_picture(
        self,
        company_id,  # type: str
        sales_quote_id,  # type: str
        sales_quote_line_id,  # type: str
        picture_id,  # type: str
        id=None,  # type: Optional[str]
        content=None,  # type: Optional[bytes]
        content_type_parameter=None,  # type: Optional[str]
        height=None,  # type: Optional[int]
        width=None,  # type: Optional[int]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property picture in financials.

        Update the navigation property picture in financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_quote_id: key: id of salesQuote.
        :type sales_quote_id: str
        :param sales_quote_line_id: key: id of salesQuoteLine.
        :type sales_quote_line_id: str
        :param picture_id: key: id of picture.
        :type picture_id: str
        :param id: Read-only.
        :type id: str
        :param content:
        :type content: bytes
        :param content_type_parameter:
        :type content_type_parameter: str
        :param height:
        :type height: int
        :param width:
        :type width: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))

        _body = models.MicrosoftGraphPicture(id=id, content=content, content_type=content_type_parameter, height=height, width=width)
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.update_picture.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesQuote-id': self._serialize.url("sales_quote_id", sales_quote_id, 'str'),
            'salesQuoteLine-id': self._serialize.url("sales_quote_line_id", sales_quote_line_id, 'str'),
            'picture-id': self._serialize.url("picture_id", picture_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MicrosoftGraphPicture')
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

    update_picture.metadata = {'url': '/financials/companies/{company-id}/salesQuotes/{salesQuote-id}/salesQuoteLines/{salesQuoteLine-id}/item/picture/{picture-id}'}  # type: ignore

    def delete_picture(
        self,
        company_id,  # type: str
        sales_quote_id,  # type: str
        sales_quote_line_id,  # type: str
        picture_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property picture for financials.

        Delete navigation property picture for financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_quote_id: key: id of salesQuote.
        :type sales_quote_id: str
        :param sales_quote_line_id: key: id of salesQuoteLine.
        :type sales_quote_line_id: str
        :param picture_id: key: id of picture.
        :type picture_id: str
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
        url = self.delete_picture.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesQuote-id': self._serialize.url("sales_quote_id", sales_quote_id, 'str'),
            'salesQuoteLine-id': self._serialize.url("sales_quote_line_id", sales_quote_line_id, 'str'),
            'picture-id': self._serialize.url("picture_id", picture_id, 'str'),
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

    delete_picture.metadata = {'url': '/financials/companies/{company-id}/salesQuotes/{salesQuote-id}/salesQuoteLines/{salesQuoteLine-id}/item/picture/{picture-id}'}  # type: ignore

    def get_picture_content(
        self,
        company_id,  # type: str
        sales_quote_id,  # type: str
        sales_quote_line_id,  # type: str
        picture_id,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """Get media content for the navigation property picture from financials.

        Get media content for the navigation property picture from financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_quote_id: key: id of salesQuote.
        :type sales_quote_id: str
        :param sales_quote_line_id: key: id of salesQuoteLine.
        :type sales_quote_line_id: str
        :param picture_id: key: id of picture.
        :type picture_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[IO]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/octet-stream, application/json"

        # Construct URL
        url = self.get_picture_content.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesQuote-id': self._serialize.url("sales_quote_id", sales_quote_id, 'str'),
            'salesQuoteLine-id': self._serialize.url("sales_quote_line_id", sales_quote_line_id, 'str'),
            'picture-id': self._serialize.url("picture_id", picture_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')
        header_parameters['Accept'] = 'application/octet-stream, application/json'

        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=True, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = response.stream_download(self._client._pipeline)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_picture_content.metadata = {'url': '/financials/companies/{company-id}/salesQuotes/{salesQuote-id}/salesQuoteLines/{salesQuoteLine-id}/item/picture/{picture-id}/content'}  # type: ignore

    def set_picture_content(
        self,
        company_id,  # type: str
        sales_quote_id,  # type: str
        sales_quote_line_id,  # type: str
        picture_id,  # type: str
        data,  # type: IO
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update media content for the navigation property picture in financials.

        Update media content for the navigation property picture in financials.

        :param company_id: key: id of company.
        :type company_id: str
        :param sales_quote_id: key: id of salesQuote.
        :type sales_quote_id: str
        :param sales_quote_line_id: key: id of salesQuoteLine.
        :type sales_quote_line_id: str
        :param picture_id: key: id of picture.
        :type picture_id: str
        :param data: New media content.
        :type data: IO
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {404: ResourceNotFoundError, 409: ResourceExistsError}
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/octet-stream")
        accept = "application/json"

        # Construct URL
        url = self.set_picture_content.metadata['url']  # type: ignore
        path_format_arguments = {
            'company-id': self._serialize.url("company_id", company_id, 'str'),
            'salesQuote-id': self._serialize.url("sales_quote_id", sales_quote_id, 'str'),
            'salesQuoteLine-id': self._serialize.url("sales_quote_line_id", sales_quote_line_id, 'str'),
            'picture-id': self._serialize.url("picture_id", picture_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content_kwargs['stream_content'] = data
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    set_picture_content.metadata = {'url': '/financials/companies/{company-id}/salesQuotes/{salesQuote-id}/salesQuoteLines/{salesQuoteLine-id}/item/picture/{picture-id}/content'}  # type: ignore
