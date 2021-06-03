# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_people_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_people.vendored_sdks.people import People
    return get_mgmt_service_client(cli_ctx,
                                   People,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_user(cli_ctx, *_):
    return cf_people_cl(cli_ctx).users


def cf_user_insight(cli_ctx, *_):
    return cf_people_cl(cli_ctx).users_insights


def cf_user_insight_shared(cli_ctx, *_):
    return cf_people_cl(cli_ctx).users_insights_shared


def cf_user_insight_trending(cli_ctx, *_):
    return cf_people_cl(cli_ctx).users_insights_trending


def cf_user_insight_used(cli_ctx, *_):
    return cf_people_cl(cli_ctx).users_insights_used
