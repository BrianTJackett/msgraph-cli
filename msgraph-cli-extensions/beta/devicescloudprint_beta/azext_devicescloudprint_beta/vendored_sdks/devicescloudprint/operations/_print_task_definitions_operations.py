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
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Callable, Dict, Generic, Iterable, List, Optional, TypeVar, Union

    T = TypeVar('T')
    ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class PrintTaskDefinitionsOperations(object):
    """PrintTaskDefinitionsOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~devices_cloud_print.models
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

    def list_tasks(
        self,
        print_task_definition_id,  # type: str
        orderby=None,  # type: Optional[List[Union[str, "models.Enum103"]]]
        select=None,  # type: Optional[List[Union[str, "models.Enum104"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum105"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> Iterable["models.CollectionOfPrintTask"]
        """Get tasks from print.

        Get tasks from print.

        :param print_task_definition_id: key: id of printTaskDefinition.
        :type print_task_definition_id: str
        :param orderby: Order items by property values.
        :type orderby: list[str or ~devices_cloud_print.models.Enum103]
        :param select: Select properties to be returned.
        :type select: list[str or ~devices_cloud_print.models.Enum104]
        :param expand: Expand related entities.
        :type expand: list[str or ~devices_cloud_print.models.Enum105]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either CollectionOfPrintTask or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~devices_cloud_print.models.CollectionOfPrintTask]
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.CollectionOfPrintTask"]
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
                url = self.list_tasks.metadata['url']  # type: ignore
                path_format_arguments = {
                    'printTaskDefinition-id': self._serialize.url("print_task_definition_id", print_task_definition_id, 'str'),
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
            deserialized = self._deserialize('CollectionOfPrintTask', pipeline_response)
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
    list_tasks.metadata = {'url': '/print/taskDefinitions/{printTaskDefinition-id}/tasks'}  # type: ignore

    def create_tasks(
        self,
        print_task_definition_id,  # type: str
        body,  # type: "models.MicrosoftGraphPrintTask"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPrintTask"
        """Create new navigation property to tasks for print.

        Create new navigation property to tasks for print.

        :param print_task_definition_id: key: id of printTaskDefinition.
        :type print_task_definition_id: str
        :param body: New navigation property.
        :type body: ~devices_cloud_print.models.MicrosoftGraphPrintTask
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPrintTask, or the result of cls(response)
        :rtype: ~devices_cloud_print.models.MicrosoftGraphPrintTask
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPrintTask"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self.create_tasks.metadata['url']  # type: ignore
        path_format_arguments = {
            'printTaskDefinition-id': self._serialize.url("print_task_definition_id", print_task_definition_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphPrintTask')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize(models.OdataError, response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('MicrosoftGraphPrintTask', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_tasks.metadata = {'url': '/print/taskDefinitions/{printTaskDefinition-id}/tasks'}  # type: ignore

    def get_tasks(
        self,
        print_task_definition_id,  # type: str
        print_task_id,  # type: str
        select=None,  # type: Optional[List[Union[str, "models.Enum106"]]]
        expand=None,  # type: Optional[List[Union[str, "models.Enum107"]]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.MicrosoftGraphPrintTask"
        """Get tasks from print.

        Get tasks from print.

        :param print_task_definition_id: key: id of printTaskDefinition.
        :type print_task_definition_id: str
        :param print_task_id: key: id of printTask.
        :type print_task_id: str
        :param select: Select properties to be returned.
        :type select: list[str or ~devices_cloud_print.models.Enum106]
        :param expand: Expand related entities.
        :type expand: list[str or ~devices_cloud_print.models.Enum107]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MicrosoftGraphPrintTask, or the result of cls(response)
        :rtype: ~devices_cloud_print.models.MicrosoftGraphPrintTask
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MicrosoftGraphPrintTask"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        accept = "application/json"

        # Construct URL
        url = self.get_tasks.metadata['url']  # type: ignore
        path_format_arguments = {
            'printTaskDefinition-id': self._serialize.url("print_task_definition_id", print_task_definition_id, 'str'),
            'printTask-id': self._serialize.url("print_task_id", print_task_id, 'str'),
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

        deserialized = self._deserialize('MicrosoftGraphPrintTask', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get_tasks.metadata = {'url': '/print/taskDefinitions/{printTaskDefinition-id}/tasks/{printTask-id}'}  # type: ignore

    def update_tasks(
        self,
        print_task_definition_id,  # type: str
        print_task_id,  # type: str
        body,  # type: "models.MicrosoftGraphPrintTask"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Update the navigation property tasks in print.

        Update the navigation property tasks in print.

        :param print_task_definition_id: key: id of printTaskDefinition.
        :type print_task_definition_id: str
        :param print_task_id: key: id of printTask.
        :type print_task_id: str
        :param body: New navigation property values.
        :type body: ~devices_cloud_print.models.MicrosoftGraphPrintTask
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
        url = self.update_tasks.metadata['url']  # type: ignore
        path_format_arguments = {
            'printTaskDefinition-id': self._serialize.url("print_task_definition_id", print_task_definition_id, 'str'),
            'printTask-id': self._serialize.url("print_task_id", print_task_id, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header("content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header("accept", accept, 'str')

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(body, 'MicrosoftGraphPrintTask')
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

    update_tasks.metadata = {'url': '/print/taskDefinitions/{printTaskDefinition-id}/tasks/{printTask-id}'}  # type: ignore

    def delete_tasks(
        self,
        print_task_definition_id,  # type: str
        print_task_id,  # type: str
        if_match=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete navigation property tasks for print.

        Delete navigation property tasks for print.

        :param print_task_definition_id: key: id of printTaskDefinition.
        :type print_task_definition_id: str
        :param print_task_id: key: id of printTask.
        :type print_task_id: str
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
        url = self.delete_tasks.metadata['url']  # type: ignore
        path_format_arguments = {
            'printTaskDefinition-id': self._serialize.url("print_task_definition_id", print_task_definition_id, 'str'),
            'printTask-id': self._serialize.url("print_task_id", print_task_id, 'str'),
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

    delete_tasks.metadata = {'url': '/print/taskDefinitions/{printTaskDefinition-id}/tasks/{printTask-id}'}  # type: ignore
