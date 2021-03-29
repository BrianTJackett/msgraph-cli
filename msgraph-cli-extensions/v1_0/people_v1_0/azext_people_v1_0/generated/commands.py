# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-statements
# pylint: disable=too-many-locals
# pylint: disable=bad-continuation
# pylint: disable=line-too-long

from msgraph.cli.core.commands import CliCommandType
from azext_people_v1_0.generated._client_factory import (
    cf_user,
    cf_user_insight,
    cf_user_insight_shared,
    cf_user_insight_trending,
    cf_user_insight_used,
)


people_v1_0_user = CliCommandType(
    operations_tmpl='azext_people_v1_0.vendored_sdks.people.operations._user_operations#UserOperations.{}',
    client_factory=cf_user,
)


people_v1_0_user_insight = CliCommandType(
    operations_tmpl=(
        'azext_people_v1_0.vendored_sdks.people.operations._user_insight_operations#UserInsightOperations.{}'
    ),
    client_factory=cf_user_insight,
)


people_v1_0_user_insight_shared = CliCommandType(
    operations_tmpl='azext_people_v1_0.vendored_sdks.people.operations._user_insight_shared_operations#UserInsightSharedOperations.{}',
    client_factory=cf_user_insight_shared,
)


people_v1_0_user_insight_trending = CliCommandType(
    operations_tmpl='azext_people_v1_0.vendored_sdks.people.operations._user_insight_trending_operations#UserInsightTrendingOperations.{}',
    client_factory=cf_user_insight_trending,
)


people_v1_0_user_insight_used = CliCommandType(
    operations_tmpl=(
        'azext_people_v1_0.vendored_sdks.people.operations._user_insight_used_operations#UserInsightUsedOperations.{}'
    ),
    client_factory=cf_user_insight_used,
)


def load_command_table(self, _):

    with self.command_group('people user', people_v1_0_user, client_factory=cf_user) as g:
        g.custom_command('create-person', 'people_user_create_person')
        g.custom_command('delete-insight', 'people_user_delete_insight')
        g.custom_command('delete-person', 'people_user_delete_person')
        g.custom_command('list-person', 'people_user_list_person')
        g.custom_command('show-insight', 'people_user_show_insight')
        g.custom_command('show-person', 'people_user_show_person')
        g.custom_command('update-insight', 'people_user_update_insight')
        g.custom_command('update-person', 'people_user_update_person')

    with self.command_group('people user-insight', people_v1_0_user_insight, client_factory=cf_user_insight) as g:
        g.custom_command('create-shared', 'people_user_insight_create_shared')
        g.custom_command('create-trending', 'people_user_insight_create_trending')
        g.custom_command('create-used', 'people_user_insight_create_used')
        g.custom_command('delete-shared', 'people_user_insight_delete_shared')
        g.custom_command('delete-trending', 'people_user_insight_delete_trending')
        g.custom_command('delete-used', 'people_user_insight_delete_used')
        g.custom_command('list-shared', 'people_user_insight_list_shared')
        g.custom_command('list-trending', 'people_user_insight_list_trending')
        g.custom_command('list-used', 'people_user_insight_list_used')
        g.custom_command('show-shared', 'people_user_insight_show_shared')
        g.custom_command('show-trending', 'people_user_insight_show_trending')
        g.custom_command('show-used', 'people_user_insight_show_used')
        g.custom_command('update-shared', 'people_user_insight_update_shared')
        g.custom_command('update-trending', 'people_user_insight_update_trending')
        g.custom_command('update-used', 'people_user_insight_update_used')

    with self.command_group(
        'people user-insight-shared', people_v1_0_user_insight_shared, client_factory=cf_user_insight_shared
    ) as g:
        g.custom_command('delete-ref-last-shared-method', 'people_user_insight_shared_delete_ref_last_shared_method')
        g.custom_command('delete-ref-resource', 'people_user_insight_shared_delete_ref_resource')
        g.custom_command('set-ref-last-shared-method', 'people_user_insight_shared_set_ref_last_shared_method')
        g.custom_command('set-ref-resource', 'people_user_insight_shared_set_ref_resource')
        g.custom_command('show-last-shared-method', 'people_user_insight_shared_show_last_shared_method')
        g.custom_command('show-ref-last-shared-method', 'people_user_insight_shared_show_ref_last_shared_method')
        g.custom_command('show-ref-resource', 'people_user_insight_shared_show_ref_resource')
        g.custom_command('show-resource', 'people_user_insight_shared_show_resource')

    with self.command_group(
        'people user-insight-trending', people_v1_0_user_insight_trending, client_factory=cf_user_insight_trending
    ) as g:
        g.custom_command('delete-ref-resource', 'people_user_insight_trending_delete_ref_resource')
        g.custom_command('set-ref-resource', 'people_user_insight_trending_set_ref_resource')
        g.custom_command('show-ref-resource', 'people_user_insight_trending_show_ref_resource')
        g.custom_command('show-resource', 'people_user_insight_trending_show_resource')

    with self.command_group(
        'people user-insight-used', people_v1_0_user_insight_used, client_factory=cf_user_insight_used
    ) as g:
        g.custom_command('delete-ref-resource', 'people_user_insight_used_delete_ref_resource')
        g.custom_command('set-ref-resource', 'people_user_insight_used_set_ref_resource')
        g.custom_command('show-ref-resource', 'people_user_insight_used_show_ref_resource')
        g.custom_command('show-resource', 'people_user_insight_used_show_resource')

    with self.command_group('people_v1_0', is_experimental=True):
        pass
