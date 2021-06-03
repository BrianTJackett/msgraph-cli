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

from azure.cli.core.commands import CliCommandType
from azext_planner.generated._client_factory import (
    cf_group,
    cf_group_planner,
    cf_group_planner_plan,
    cf_group_planner_plan_bucket,
    cf_group_planner_plan_bucket_task,
    cf_group_planner_plan_task,
    cf_planner_planner,
    cf_planner,
    cf_planner_bucket,
    cf_planner_bucket_task,
    cf_planner_plan,
    cf_planner_plan_bucket,
    cf_planner_plan_bucket_task,
    cf_planner_plan_task,
    cf_planner_task,
    cf_user,
    cf_user_planner,
    cf_user_planner_plan,
    cf_user_planner_plan_bucket,
    cf_user_planner_plan_bucket_task,
    cf_user_planner_plan_task,
    cf_user_planner_task,
)


planner_group = CliCommandType(
    operations_tmpl='azext_planner.vendored_sdks.planner.operations._groups_operations#GroupsOperations.{}',
    client_factory=cf_group,
)


planner_group_planner = CliCommandType(
    operations_tmpl=(
        'azext_planner.vendored_sdks.planner.operations._groups_planner_operations#GroupsPlannerOperations.{}'
    ),
    client_factory=cf_group_planner,
)


planner_group_planner_plan = CliCommandType(
    operations_tmpl='azext_planner.vendored_sdks.planner.operations._groups_planner_plans_operations#GroupsPlannerPlansOperations.{}',
    client_factory=cf_group_planner_plan,
)


planner_group_planner_plan_bucket = CliCommandType(
    operations_tmpl='azext_planner.vendored_sdks.planner.operations._groups_planner_plans_buckets_operations#GroupsPlannerPlansBucketsOperations.{}',
    client_factory=cf_group_planner_plan_bucket,
)


planner_group_planner_plan_bucket_task = CliCommandType(
    operations_tmpl='azext_planner.vendored_sdks.planner.operations._groups_planner_plans_buckets_tasks_operations#GroupsPlannerPlansBucketsTasksOperations.{}',
    client_factory=cf_group_planner_plan_bucket_task,
)


planner_group_planner_plan_task = CliCommandType(
    operations_tmpl='azext_planner.vendored_sdks.planner.operations._groups_planner_plans_tasks_operations#GroupsPlannerPlansTasksOperations.{}',
    client_factory=cf_group_planner_plan_task,
)


planner_planner_planner = CliCommandType(
    operations_tmpl=(
        'azext_planner.vendored_sdks.planner.operations._planner_planner_operations#PlannerPlannerOperations.{}'
    ),
    client_factory=cf_planner_planner,
)


planner_planner = CliCommandType(
    operations_tmpl='azext_planner.vendored_sdks.planner.operations._planner_operations#PlannerOperations.{}',
    client_factory=cf_planner,
)


planner_planner_bucket = CliCommandType(
    operations_tmpl=(
        'azext_planner.vendored_sdks.planner.operations._planner_buckets_operations#PlannerBucketsOperations.{}'
    ),
    client_factory=cf_planner_bucket,
)


planner_planner_bucket_task = CliCommandType(
    operations_tmpl='azext_planner.vendored_sdks.planner.operations._planner_buckets_tasks_operations#PlannerBucketsTasksOperations.{}',
    client_factory=cf_planner_bucket_task,
)


planner_planner_plan = CliCommandType(
    operations_tmpl=(
        'azext_planner.vendored_sdks.planner.operations._planner_plans_operations#PlannerPlansOperations.{}'
    ),
    client_factory=cf_planner_plan,
)


planner_planner_plan_bucket = CliCommandType(
    operations_tmpl='azext_planner.vendored_sdks.planner.operations._planner_plans_buckets_operations#PlannerPlansBucketsOperations.{}',
    client_factory=cf_planner_plan_bucket,
)


planner_planner_plan_bucket_task = CliCommandType(
    operations_tmpl='azext_planner.vendored_sdks.planner.operations._planner_plans_buckets_tasks_operations#PlannerPlansBucketsTasksOperations.{}',
    client_factory=cf_planner_plan_bucket_task,
)


planner_planner_plan_task = CliCommandType(
    operations_tmpl=(
        'azext_planner.vendored_sdks.planner.operations._planner_plans_tasks_operations#PlannerPlansTasksOperations.{}'
    ),
    client_factory=cf_planner_plan_task,
)


planner_planner_task = CliCommandType(
    operations_tmpl=(
        'azext_planner.vendored_sdks.planner.operations._planner_tasks_operations#PlannerTasksOperations.{}'
    ),
    client_factory=cf_planner_task,
)


planner_user = CliCommandType(
    operations_tmpl='azext_planner.vendored_sdks.planner.operations._users_operations#UsersOperations.{}',
    client_factory=cf_user,
)


planner_user_planner = CliCommandType(
    operations_tmpl=(
        'azext_planner.vendored_sdks.planner.operations._users_planner_operations#UsersPlannerOperations.{}'
    ),
    client_factory=cf_user_planner,
)


planner_user_planner_plan = CliCommandType(
    operations_tmpl=(
        'azext_planner.vendored_sdks.planner.operations._users_planner_plans_operations#UsersPlannerPlansOperations.{}'
    ),
    client_factory=cf_user_planner_plan,
)


planner_user_planner_plan_bucket = CliCommandType(
    operations_tmpl='azext_planner.vendored_sdks.planner.operations._users_planner_plans_buckets_operations#UsersPlannerPlansBucketsOperations.{}',
    client_factory=cf_user_planner_plan_bucket,
)


planner_user_planner_plan_bucket_task = CliCommandType(
    operations_tmpl='azext_planner.vendored_sdks.planner.operations._users_planner_plans_buckets_tasks_operations#UsersPlannerPlansBucketsTasksOperations.{}',
    client_factory=cf_user_planner_plan_bucket_task,
)


planner_user_planner_plan_task = CliCommandType(
    operations_tmpl='azext_planner.vendored_sdks.planner.operations._users_planner_plans_tasks_operations#UsersPlannerPlansTasksOperations.{}',
    client_factory=cf_user_planner_plan_task,
)


planner_user_planner_task = CliCommandType(
    operations_tmpl=(
        'azext_planner.vendored_sdks.planner.operations._users_planner_tasks_operations#UsersPlannerTasksOperations.{}'
    ),
    client_factory=cf_user_planner_task,
)


def load_command_table(self, _):

    with self.command_group('planner group', planner_group, client_factory=cf_group) as g:
        g.custom_command('delete-planner', 'planner_group_delete_planner')
        g.custom_command('show-planner', 'planner_group_show_planner')
        g.custom_command('update-planner', 'planner_group_update_planner')

    with self.command_group('planner group-planner', planner_group_planner, client_factory=cf_group_planner) as g:
        g.custom_command('create-plan', 'planner_group_planner_create_plan')
        g.custom_command('delete-plan', 'planner_group_planner_delete_plan')
        g.custom_command('list-plan', 'planner_group_planner_list_plan')
        g.custom_command('show-plan', 'planner_group_planner_show_plan')
        g.custom_command('update-plan', 'planner_group_planner_update_plan')

    with self.command_group(
        'planner group-planner-plan', planner_group_planner_plan, client_factory=cf_group_planner_plan
    ) as g:
        g.custom_command('create-bucket', 'planner_group_planner_plan_create_bucket')
        g.custom_command('create-task', 'planner_group_planner_plan_create_task')
        g.custom_command('delete-bucket', 'planner_group_planner_plan_delete_bucket')
        g.custom_command('delete-detail', 'planner_group_planner_plan_delete_detail')
        g.custom_command('delete-task', 'planner_group_planner_plan_delete_task')
        g.custom_command('list-bucket', 'planner_group_planner_plan_list_bucket')
        g.custom_command('list-task', 'planner_group_planner_plan_list_task')
        g.custom_command('show-bucket', 'planner_group_planner_plan_show_bucket')
        g.custom_command('show-detail', 'planner_group_planner_plan_show_detail')
        g.custom_command('show-task', 'planner_group_planner_plan_show_task')
        g.custom_command('update-bucket', 'planner_group_planner_plan_update_bucket')
        g.custom_command('update-detail', 'planner_group_planner_plan_update_detail')
        g.custom_command('update-task', 'planner_group_planner_plan_update_task')

    with self.command_group(
        'planner group-planner-plan-bucket',
        planner_group_planner_plan_bucket,
        client_factory=cf_group_planner_plan_bucket,
    ) as g:
        g.custom_command('create-task', 'planner_group_planner_plan_bucket_create_task')
        g.custom_command('delete-task', 'planner_group_planner_plan_bucket_delete_task')
        g.custom_command('list-task', 'planner_group_planner_plan_bucket_list_task')
        g.custom_command('show-task', 'planner_group_planner_plan_bucket_show_task')
        g.custom_command('update-task', 'planner_group_planner_plan_bucket_update_task')

    with self.command_group(
        'planner group-planner-plan-bucket-task',
        planner_group_planner_plan_bucket_task,
        client_factory=cf_group_planner_plan_bucket_task,
    ) as g:
        g.custom_command(
            'delete-assigned-to-task-board-format',
            'planner_group_planner_plan_bucket_task_delete_assigned_to_task_board_format',
        )
        g.custom_command(
            'delete-bucket-task-board-format', 'planner_group_planner_plan_bucket_task_delete_bucket_task_board_format'
        )
        g.custom_command('delete-detail', 'planner_group_planner_plan_bucket_task_delete_detail')
        g.custom_command(
            'delete-progress-task-board-format',
            'planner_group_planner_plan_bucket_task_delete_progress_task_board_format',
        )
        g.custom_command(
            'show-assigned-to-task-board-format',
            'planner_group_planner_plan_bucket_task_show_assigned_to_task_board_format',
        )
        g.custom_command(
            'show-bucket-task-board-format', 'planner_group_planner_plan_bucket_task_show_bucket_task_board_format'
        )
        g.custom_command('show-detail', 'planner_group_planner_plan_bucket_task_show_detail')
        g.custom_command(
            'show-progress-task-board-format', 'planner_group_planner_plan_bucket_task_show_progress_task_board_format'
        )
        g.custom_command(
            'update-assigned-to-task-board-format',
            'planner_group_planner_plan_bucket_task_update_assigned_to_task_board_format',
        )
        g.custom_command(
            'update-bucket-task-board-format', 'planner_group_planner_plan_bucket_task_update_bucket_task_board_format'
        )
        g.custom_command('update-detail', 'planner_group_planner_plan_bucket_task_update_detail')
        g.custom_command(
            'update-progress-task-board-format',
            'planner_group_planner_plan_bucket_task_update_progress_task_board_format',
        )

    with self.command_group(
        'planner group-planner-plan-task', planner_group_planner_plan_task, client_factory=cf_group_planner_plan_task
    ) as g:
        g.custom_command(
            'delete-assigned-to-task-board-format',
            'planner_group_planner_plan_task_delete_assigned_to_task_board_format',
        )
        g.custom_command(
            'delete-bucket-task-board-format', 'planner_group_planner_plan_task_delete_bucket_task_board_format'
        )
        g.custom_command('delete-detail', 'planner_group_planner_plan_task_delete_detail')
        g.custom_command(
            'delete-progress-task-board-format', 'planner_group_planner_plan_task_delete_progress_task_board_format'
        )
        g.custom_command(
            'show-assigned-to-task-board-format', 'planner_group_planner_plan_task_show_assigned_to_task_board_format'
        )
        g.custom_command(
            'show-bucket-task-board-format', 'planner_group_planner_plan_task_show_bucket_task_board_format'
        )
        g.custom_command('show-detail', 'planner_group_planner_plan_task_show_detail')
        g.custom_command(
            'show-progress-task-board-format', 'planner_group_planner_plan_task_show_progress_task_board_format'
        )
        g.custom_command(
            'update-assigned-to-task-board-format',
            'planner_group_planner_plan_task_update_assigned_to_task_board_format',
        )
        g.custom_command(
            'update-bucket-task-board-format', 'planner_group_planner_plan_task_update_bucket_task_board_format'
        )
        g.custom_command('update-detail', 'planner_group_planner_plan_task_update_detail')
        g.custom_command(
            'update-progress-task-board-format', 'planner_group_planner_plan_task_update_progress_task_board_format'
        )

    with self.command_group('planner planner', planner_planner_planner, client_factory=cf_planner_planner) as g:
        g.custom_command('create', 'planner_planner_create')
        g.custom_command('show-planner', 'planner_planner_show_planner')

    with self.command_group('planner', planner_planner, client_factory=cf_planner, is_experimental=True) as g:
        g.custom_command('create-bucket', 'planner_create_bucket')
        g.custom_command('create-plan', 'planner_create_plan')
        g.custom_command('create-task', 'planner_create_task')
        g.custom_command('delete-bucket', 'planner_delete_bucket')
        g.custom_command('delete-plan', 'planner_delete_plan')
        g.custom_command('delete-task', 'planner_delete_task')
        g.custom_command('list-bucket', 'planner_list_bucket')
        g.custom_command('list-plan', 'planner_list_plan')
        g.custom_command('list-task', 'planner_list_task')
        g.custom_command('show-bucket', 'planner_show_bucket')
        g.custom_command('show-plan', 'planner_show_plan')
        g.custom_command('show-task', 'planner_show_task')
        g.custom_command('update-bucket', 'planner_update_bucket')
        g.custom_command('update-plan', 'planner_update_plan')
        g.custom_command('update-task', 'planner_update_task')

    with self.command_group('planner planner-bucket', planner_planner_bucket, client_factory=cf_planner_bucket) as g:
        g.custom_command('create-task', 'planner_planner_bucket_create_task')
        g.custom_command('delete-task', 'planner_planner_bucket_delete_task')
        g.custom_command('list-task', 'planner_planner_bucket_list_task')
        g.custom_command('show-task', 'planner_planner_bucket_show_task')
        g.custom_command('update-task', 'planner_planner_bucket_update_task')

    with self.command_group(
        'planner planner-bucket-task', planner_planner_bucket_task, client_factory=cf_planner_bucket_task
    ) as g:
        g.custom_command(
            'delete-assigned-to-task-board-format', 'planner_planner_bucket_task_delete_assigned_to_task_board_format'
        )
        g.custom_command(
            'delete-bucket-task-board-format', 'planner_planner_bucket_task_delete_bucket_task_board_format'
        )
        g.custom_command('delete-detail', 'planner_planner_bucket_task_delete_detail')
        g.custom_command(
            'delete-progress-task-board-format', 'planner_planner_bucket_task_delete_progress_task_board_format'
        )
        g.custom_command(
            'show-assigned-to-task-board-format', 'planner_planner_bucket_task_show_assigned_to_task_board_format'
        )
        g.custom_command('show-bucket-task-board-format', 'planner_planner_bucket_task_show_bucket_task_board_format')
        g.custom_command('show-detail', 'planner_planner_bucket_task_show_detail')
        g.custom_command(
            'show-progress-task-board-format', 'planner_planner_bucket_task_show_progress_task_board_format'
        )
        g.custom_command(
            'update-assigned-to-task-board-format', 'planner_planner_bucket_task_update_assigned_to_task_board_format'
        )
        g.custom_command(
            'update-bucket-task-board-format', 'planner_planner_bucket_task_update_bucket_task_board_format'
        )
        g.custom_command('update-detail', 'planner_planner_bucket_task_update_detail')
        g.custom_command(
            'update-progress-task-board-format', 'planner_planner_bucket_task_update_progress_task_board_format'
        )

    with self.command_group('planner planner-plan', planner_planner_plan, client_factory=cf_planner_plan) as g:
        g.custom_command('create-bucket', 'planner_planner_plan_create_bucket')
        g.custom_command('create-task', 'planner_planner_plan_create_task')
        g.custom_command('delete-bucket', 'planner_planner_plan_delete_bucket')
        g.custom_command('delete-detail', 'planner_planner_plan_delete_detail')
        g.custom_command('delete-task', 'planner_planner_plan_delete_task')
        g.custom_command('list-bucket', 'planner_planner_plan_list_bucket')
        g.custom_command('list-task', 'planner_planner_plan_list_task')
        g.custom_command('show-bucket', 'planner_planner_plan_show_bucket')
        g.custom_command('show-detail', 'planner_planner_plan_show_detail')
        g.custom_command('show-task', 'planner_planner_plan_show_task')
        g.custom_command('update-bucket', 'planner_planner_plan_update_bucket')
        g.custom_command('update-detail', 'planner_planner_plan_update_detail')
        g.custom_command('update-task', 'planner_planner_plan_update_task')

    with self.command_group(
        'planner planner-plan-bucket', planner_planner_plan_bucket, client_factory=cf_planner_plan_bucket
    ) as g:
        g.custom_command('create-task', 'planner_planner_plan_bucket_create_task')
        g.custom_command('delete-task', 'planner_planner_plan_bucket_delete_task')
        g.custom_command('list-task', 'planner_planner_plan_bucket_list_task')
        g.custom_command('show-task', 'planner_planner_plan_bucket_show_task')
        g.custom_command('update-task', 'planner_planner_plan_bucket_update_task')

    with self.command_group(
        'planner planner-plan-bucket-task', planner_planner_plan_bucket_task, client_factory=cf_planner_plan_bucket_task
    ) as g:
        g.custom_command(
            'delete-assigned-to-task-board-format',
            'planner_planner_plan_bucket_task_delete_assigned_to_task_board_format',
        )
        g.custom_command(
            'delete-bucket-task-board-format', 'planner_planner_plan_bucket_task_delete_bucket_task_board_format'
        )
        g.custom_command('delete-detail', 'planner_planner_plan_bucket_task_delete_detail')
        g.custom_command(
            'delete-progress-task-board-format', 'planner_planner_plan_bucket_task_delete_progress_task_board_format'
        )
        g.custom_command(
            'show-assigned-to-task-board-format', 'planner_planner_plan_bucket_task_show_assigned_to_task_board_format'
        )
        g.custom_command(
            'show-bucket-task-board-format', 'planner_planner_plan_bucket_task_show_bucket_task_board_format'
        )
        g.custom_command('show-detail', 'planner_planner_plan_bucket_task_show_detail')
        g.custom_command(
            'show-progress-task-board-format', 'planner_planner_plan_bucket_task_show_progress_task_board_format'
        )
        g.custom_command(
            'update-assigned-to-task-board-format',
            'planner_planner_plan_bucket_task_update_assigned_to_task_board_format',
        )
        g.custom_command(
            'update-bucket-task-board-format', 'planner_planner_plan_bucket_task_update_bucket_task_board_format'
        )
        g.custom_command('update-detail', 'planner_planner_plan_bucket_task_update_detail')
        g.custom_command(
            'update-progress-task-board-format', 'planner_planner_plan_bucket_task_update_progress_task_board_format'
        )

    with self.command_group(
        'planner planner-plan-task', planner_planner_plan_task, client_factory=cf_planner_plan_task
    ) as g:
        g.custom_command(
            'delete-assigned-to-task-board-format', 'planner_planner_plan_task_delete_assigned_to_task_board_format'
        )
        g.custom_command('delete-bucket-task-board-format', 'planner_planner_plan_task_delete_bucket_task_board_format')
        g.custom_command('delete-detail', 'planner_planner_plan_task_delete_detail')
        g.custom_command(
            'delete-progress-task-board-format', 'planner_planner_plan_task_delete_progress_task_board_format'
        )
        g.custom_command(
            'show-assigned-to-task-board-format', 'planner_planner_plan_task_show_assigned_to_task_board_format'
        )
        g.custom_command('show-bucket-task-board-format', 'planner_planner_plan_task_show_bucket_task_board_format')
        g.custom_command('show-detail', 'planner_planner_plan_task_show_detail')
        g.custom_command('show-progress-task-board-format', 'planner_planner_plan_task_show_progress_task_board_format')
        g.custom_command(
            'update-assigned-to-task-board-format', 'planner_planner_plan_task_update_assigned_to_task_board_format'
        )
        g.custom_command('update-bucket-task-board-format', 'planner_planner_plan_task_update_bucket_task_board_format')
        g.custom_command('update-detail', 'planner_planner_plan_task_update_detail')
        g.custom_command(
            'update-progress-task-board-format', 'planner_planner_plan_task_update_progress_task_board_format'
        )

    with self.command_group('planner planner-task', planner_planner_task, client_factory=cf_planner_task) as g:
        g.custom_command(
            'delete-assigned-to-task-board-format', 'planner_planner_task_delete_assigned_to_task_board_format'
        )
        g.custom_command('delete-bucket-task-board-format', 'planner_planner_task_delete_bucket_task_board_format')
        g.custom_command('delete-detail', 'planner_planner_task_delete_detail')
        g.custom_command('delete-progress-task-board-format', 'planner_planner_task_delete_progress_task_board_format')
        g.custom_command(
            'show-assigned-to-task-board-format', 'planner_planner_task_show_assigned_to_task_board_format'
        )
        g.custom_command('show-bucket-task-board-format', 'planner_planner_task_show_bucket_task_board_format')
        g.custom_command('show-detail', 'planner_planner_task_show_detail')
        g.custom_command('show-progress-task-board-format', 'planner_planner_task_show_progress_task_board_format')
        g.custom_command(
            'update-assigned-to-task-board-format', 'planner_planner_task_update_assigned_to_task_board_format'
        )
        g.custom_command('update-bucket-task-board-format', 'planner_planner_task_update_bucket_task_board_format')
        g.custom_command('update-detail', 'planner_planner_task_update_detail')
        g.custom_command('update-progress-task-board-format', 'planner_planner_task_update_progress_task_board_format')

    with self.command_group('planner user', planner_user, client_factory=cf_user) as g:
        g.custom_command('delete-planner', 'planner_user_delete_planner')
        g.custom_command('show-planner', 'planner_user_show_planner')
        g.custom_command('update-planner', 'planner_user_update_planner')

    with self.command_group('planner user-planner', planner_user_planner, client_factory=cf_user_planner) as g:
        g.custom_command('create-plan', 'planner_user_planner_create_plan')
        g.custom_command('create-task', 'planner_user_planner_create_task')
        g.custom_command('delete-plan', 'planner_user_planner_delete_plan')
        g.custom_command('delete-task', 'planner_user_planner_delete_task')
        g.custom_command('list-plan', 'planner_user_planner_list_plan')
        g.custom_command('list-task', 'planner_user_planner_list_task')
        g.custom_command('show-plan', 'planner_user_planner_show_plan')
        g.custom_command('show-task', 'planner_user_planner_show_task')
        g.custom_command('update-plan', 'planner_user_planner_update_plan')
        g.custom_command('update-task', 'planner_user_planner_update_task')

    with self.command_group(
        'planner user-planner-plan', planner_user_planner_plan, client_factory=cf_user_planner_plan
    ) as g:
        g.custom_command('create-bucket', 'planner_user_planner_plan_create_bucket')
        g.custom_command('create-task', 'planner_user_planner_plan_create_task')
        g.custom_command('delete-bucket', 'planner_user_planner_plan_delete_bucket')
        g.custom_command('delete-detail', 'planner_user_planner_plan_delete_detail')
        g.custom_command('delete-task', 'planner_user_planner_plan_delete_task')
        g.custom_command('list-bucket', 'planner_user_planner_plan_list_bucket')
        g.custom_command('list-task', 'planner_user_planner_plan_list_task')
        g.custom_command('show-bucket', 'planner_user_planner_plan_show_bucket')
        g.custom_command('show-detail', 'planner_user_planner_plan_show_detail')
        g.custom_command('show-task', 'planner_user_planner_plan_show_task')
        g.custom_command('update-bucket', 'planner_user_planner_plan_update_bucket')
        g.custom_command('update-detail', 'planner_user_planner_plan_update_detail')
        g.custom_command('update-task', 'planner_user_planner_plan_update_task')

    with self.command_group(
        'planner user-planner-plan-bucket', planner_user_planner_plan_bucket, client_factory=cf_user_planner_plan_bucket
    ) as g:
        g.custom_command('create-task', 'planner_user_planner_plan_bucket_create_task')
        g.custom_command('delete-task', 'planner_user_planner_plan_bucket_delete_task')
        g.custom_command('list-task', 'planner_user_planner_plan_bucket_list_task')
        g.custom_command('show-task', 'planner_user_planner_plan_bucket_show_task')
        g.custom_command('update-task', 'planner_user_planner_plan_bucket_update_task')

    with self.command_group(
        'planner user-planner-plan-bucket-task',
        planner_user_planner_plan_bucket_task,
        client_factory=cf_user_planner_plan_bucket_task,
    ) as g:
        g.custom_command(
            'delete-assigned-to-task-board-format',
            'planner_user_planner_plan_bucket_task_delete_assigned_to_task_board_format',
        )
        g.custom_command(
            'delete-bucket-task-board-format', 'planner_user_planner_plan_bucket_task_delete_bucket_task_board_format'
        )
        g.custom_command('delete-detail', 'planner_user_planner_plan_bucket_task_delete_detail')
        g.custom_command(
            'delete-progress-task-board-format',
            'planner_user_planner_plan_bucket_task_delete_progress_task_board_format',
        )
        g.custom_command(
            'show-assigned-to-task-board-format',
            'planner_user_planner_plan_bucket_task_show_assigned_to_task_board_format',
        )
        g.custom_command(
            'show-bucket-task-board-format', 'planner_user_planner_plan_bucket_task_show_bucket_task_board_format'
        )
        g.custom_command('show-detail', 'planner_user_planner_plan_bucket_task_show_detail')
        g.custom_command(
            'show-progress-task-board-format', 'planner_user_planner_plan_bucket_task_show_progress_task_board_format'
        )
        g.custom_command(
            'update-assigned-to-task-board-format',
            'planner_user_planner_plan_bucket_task_update_assigned_to_task_board_format',
        )
        g.custom_command(
            'update-bucket-task-board-format', 'planner_user_planner_plan_bucket_task_update_bucket_task_board_format'
        )
        g.custom_command('update-detail', 'planner_user_planner_plan_bucket_task_update_detail')
        g.custom_command(
            'update-progress-task-board-format',
            'planner_user_planner_plan_bucket_task_update_progress_task_board_format',
        )

    with self.command_group(
        'planner user-planner-plan-task', planner_user_planner_plan_task, client_factory=cf_user_planner_plan_task
    ) as g:
        g.custom_command(
            'delete-assigned-to-task-board-format',
            'planner_user_planner_plan_task_delete_assigned_to_task_board_format',
        )
        g.custom_command(
            'delete-bucket-task-board-format', 'planner_user_planner_plan_task_delete_bucket_task_board_format'
        )
        g.custom_command('delete-detail', 'planner_user_planner_plan_task_delete_detail')
        g.custom_command(
            'delete-progress-task-board-format', 'planner_user_planner_plan_task_delete_progress_task_board_format'
        )
        g.custom_command(
            'show-assigned-to-task-board-format', 'planner_user_planner_plan_task_show_assigned_to_task_board_format'
        )
        g.custom_command(
            'show-bucket-task-board-format', 'planner_user_planner_plan_task_show_bucket_task_board_format'
        )
        g.custom_command('show-detail', 'planner_user_planner_plan_task_show_detail')
        g.custom_command(
            'show-progress-task-board-format', 'planner_user_planner_plan_task_show_progress_task_board_format'
        )
        g.custom_command(
            'update-assigned-to-task-board-format',
            'planner_user_planner_plan_task_update_assigned_to_task_board_format',
        )
        g.custom_command(
            'update-bucket-task-board-format', 'planner_user_planner_plan_task_update_bucket_task_board_format'
        )
        g.custom_command('update-detail', 'planner_user_planner_plan_task_update_detail')
        g.custom_command(
            'update-progress-task-board-format', 'planner_user_planner_plan_task_update_progress_task_board_format'
        )

    with self.command_group(
        'planner user-planner-task', planner_user_planner_task, client_factory=cf_user_planner_task
    ) as g:
        g.custom_command(
            'delete-assigned-to-task-board-format', 'planner_user_planner_task_delete_assigned_to_task_board_format'
        )
        g.custom_command('delete-bucket-task-board-format', 'planner_user_planner_task_delete_bucket_task_board_format')
        g.custom_command('delete-detail', 'planner_user_planner_task_delete_detail')
        g.custom_command(
            'delete-progress-task-board-format', 'planner_user_planner_task_delete_progress_task_board_format'
        )
        g.custom_command(
            'show-assigned-to-task-board-format', 'planner_user_planner_task_show_assigned_to_task_board_format'
        )
        g.custom_command('show-bucket-task-board-format', 'planner_user_planner_task_show_bucket_task_board_format')
        g.custom_command('show-detail', 'planner_user_planner_task_show_detail')
        g.custom_command('show-progress-task-board-format', 'planner_user_planner_task_show_progress_task_board_format')
        g.custom_command(
            'update-assigned-to-task-board-format', 'planner_user_planner_task_update_assigned_to_task_board_format'
        )
        g.custom_command('update-bucket-task-board-format', 'planner_user_planner_task_update_bucket_task_board_format')
        g.custom_command('update-detail', 'planner_user_planner_task_update_detail')
        g.custom_command(
            'update-progress-task-board-format', 'planner_user_planner_task_update_progress_task_board_format'
        )
