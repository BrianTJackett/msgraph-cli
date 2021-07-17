# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from pathlib import Path
from os import path

AUTH_RECORD_LOCATION = path.join(Path.home(), '.mg', 'record.txt')
PROFILE_LOCATION = path.join(Path.home(), '.mg', 'profile.json')
DEFAULT_CLIENT_ID = '888bce95-fde5-40f8-a7d4-2debf0f96f4c'
DEFAULT_AUTHORITY = 'https://login.microsoftonline.com'
DEFAULT_BASE_URL = 'https://graph.microsoft.com/v1.0'

GRAPH_VERSIONS = ['v1.0', 'beta']

CLI_COMMON_KWARGS = [
    'min_api', 'max_api', 'resource_type', 'operation_group', 'custom_command_type', 'command_type',
    'is_preview', 'preview_info', 'is_experimental', 'experimental_info', 'local_context_attribute'
]

CLI_COMMAND_KWARGS = [
    'transform', 'table_transformer', 'confirmation', 'exception_handler', 'client_factory',
    'operations_tmpl', 'no_wait_param', 'supports_no_wait', 'validator', 'client_arg_name',
    'doc_string_source', 'deprecate_info', 'supports_local_cache', 'model_path'
] + CLI_COMMON_KWARGS

EXCLUDED_PARAMS = [
    'self', 'raw', 'polling', 'custom_headers', 'operation_config', 'content_version', 'kwargs',
    'client', 'no_wait'
]

DEFAULT_CLOUDS = {
    'PUBLIC': {
        'name': 'PUBLIC',
        'graph_endpoint': 'https://graph.microsoft.com',
        'azure_ad_endpoint': 'https://login.microsoftonline.com'
    },
    'US_GOV_L4': {
        'name': 'US_GOV_L4',
        'graph_endpoint': 'https://graph.microsoft.us',
        'azure_ad_endpoint': 'https://login.microsoftonline.us'
    },
    'US_GOV_L5': {
        'name': 'US_GOV_L5',
        'graph_endpoint': 'https://dod-graph.microsoft.us',
        'azure_ad_endpoint': 'https://login.microsoftonline.us'
    },
    'GERMANY': {
        'name': 'GERMANY',
        'graph_endpoint': 'https://graph.microsoft.de',
        'azure_ad_endpoint': 'https://login.microsoftonline.de'
    },
    'CHINA': {
        'name': 'CHINA',
        'graph_endpoint': 'https://microsoftgraph.chinacloudapi.cn',
        'azure_ad_endpoint': 'https://login.chinacloudapi.cn'
    }
}

DEFAULT_PROFILE = {'cloud': DEFAULT_CLOUDS['PUBLIC'], 'version': 'v1.0', 'user_defined_clouds': []}
