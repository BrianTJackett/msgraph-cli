# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_cloudcommunications_beta_cl(cli_ctx, *_):
    from msgraph.cli.core.commands.client_factory import get_mgmt_service_client
    from ..vendored_sdks.cloudcommunications import CloudCommunications
    return get_mgmt_service_client(cli_ctx,
                                   CloudCommunications,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_communication_cloud_communication(cli_ctx, *_):
    return cf_cloudcommunications_beta_cl(cli_ctx).communication_cloud_communication


def cf_communication(cli_ctx, *_):
    return cf_cloudcommunications_beta_cl(cli_ctx).communication


def cf_communication_call_record(cli_ctx, *_):
    return cf_cloudcommunications_beta_cl(cli_ctx).communication_call_record


def cf_communication_call_record_session(cli_ctx, *_):
    return cf_cloudcommunications_beta_cl(cli_ctx).communication_call_record_session


def cf_communication_call(cli_ctx, *_):
    return cf_cloudcommunications_beta_cl(cli_ctx).communication_call


def cf_communication_call_participant(cli_ctx, *_):
    return cf_cloudcommunications_beta_cl(cli_ctx).communication_call_participant


def cf_communication_online_meeting(cli_ctx, *_):
    return cf_cloudcommunications_beta_cl(cli_ctx).communication_online_meeting


def cf_user(cli_ctx, *_):
    return cf_cloudcommunications_beta_cl(cli_ctx).user
