# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_crossdeviceexperiences_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_crossdeviceexperiences.vendored_sdks.crossdeviceexperiences import CrossDeviceExperiences
    return get_mgmt_service_client(cli_ctx,
                                   CrossDeviceExperiences,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_user(cli_ctx, *_):
    return cf_crossdeviceexperiences_cl(cli_ctx).users


def cf_user_activity(cli_ctx, *_):
    return cf_crossdeviceexperiences_cl(cli_ctx).users_activities


def cf_user_activity_history_item(cli_ctx, *_):
    return cf_crossdeviceexperiences_cl(cli_ctx).users_activities_history_items
