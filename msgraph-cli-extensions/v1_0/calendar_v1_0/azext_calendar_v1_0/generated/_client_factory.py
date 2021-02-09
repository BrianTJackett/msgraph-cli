# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_calendar_v1_0_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_calendar_v1_0.vendored_sdks.calendar import Calendar
    return get_mgmt_service_client(cli_ctx,
                                   Calendar,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_group(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).groups


def cf_group_calendar(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).groups_calendar


def cf_group_calendar_calendar_view(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).groups_calendar_calendar_view


def cf_group_calendar_event(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).groups_calendar_events


def cf_group_calendar_view(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).groups_calendar_view


def cf_group_calendar_view_calendar(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).groups_calendar_view_calendar


def cf_group_event(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).groups_events


def cf_group_event_calendar(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).groups_events_calendar


def cf_place_place(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).places_place


def cf_user(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users


def cf_user_calendar(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users_calendar


def cf_user_calendar_calendar_view(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users_calendar_calendar_view


def cf_user_calendar_event(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users_calendar_events


def cf_user_calendar_group(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users_calendar_groups


def cf_user_calendar_group_calendar(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users_calendar_groups_calendars


def cf_user_calendar_group_calendar_calendar_view(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users_calendar_groups_calendars_calendar_view


def cf_user_calendar_group_calendar_event(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users_calendar_groups_calendars_events


def cf_user_calendar(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users_calendars


def cf_user_calendar_calendar_view(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users_calendars_calendar_view


def cf_user_calendar_event(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users_calendars_events


def cf_user_calendar_view(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users_calendar_view


def cf_user_calendar_view_calendar(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users_calendar_view_calendar


def cf_user_event(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users_events


def cf_user_event_calendar(cli_ctx, *_):
    return cf_calendar_v1_0_cl(cli_ctx).users_events_calendar
