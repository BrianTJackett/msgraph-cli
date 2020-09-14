# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines


def groupsplanner_get_planner(client,
                              group_id,
                              select=None,
                              expand=None):
    return client.get_planner(group_id=group_id,
                              select=select,
                              expand=expand)


def groupsplanner_update_planner(client,
                                 group_id,
                                 id_=None,
                                 plans=None):
    return client.update_planner(group_id=group_id,
                                 id=id_,
                                 plans=plans)


def groupsplanner_create_plan(client,
                              group_id,
                              id_=None,
                              created_date_time=None,
                              owner=None,
                              title=None,
                              contexts=None,
                              tasks=None,
                              buckets=None,
                              details_id=None,
                              details_shared_with=None,
                              details_category_descriptions=None,
                              details_context_details=None,
                              created_by_application=None,
                              created_by_device=None,
                              created_by_user=None):
    return client.create_plan(group_id=group_id,
                              id=id_,
                              created_date_time=created_date_time,
                              owner=owner,
                              title=title,
                              contexts=contexts,
                              tasks=tasks,
                              buckets=buckets,
                              microsoft_graph_entity_id=details_id,
                              shared_with=details_shared_with,
                              category_descriptions=details_category_descriptions,
                              context_details=details_context_details,
                              application=created_by_application,
                              device=created_by_device,
                              user=created_by_user)


def groupsplanner_get_plan(client,
                           group_id,
                           planner_plan_id,
                           select=None,
                           expand=None):
    return client.get_plan(group_id=group_id,
                           planner_plan_id=planner_plan_id,
                           select=select,
                           expand=expand)


def groupsplanner_list_plan(client,
                            group_id,
                            orderby=None,
                            select=None,
                            expand=None):
    return client.list_plan(group_id=group_id,
                            orderby=orderby,
                            select=select,
                            expand=expand)


def groupsplanner_update_plan(client,
                              group_id,
                              planner_plan_id,
                              id_=None,
                              created_date_time=None,
                              owner=None,
                              title=None,
                              contexts=None,
                              tasks=None,
                              buckets=None,
                              details_id=None,
                              details_shared_with=None,
                              details_category_descriptions=None,
                              details_context_details=None,
                              created_by_application=None,
                              created_by_device=None,
                              created_by_user=None):
    return client.update_plan(group_id=group_id,
                              planner_plan_id=planner_plan_id,
                              id=id_,
                              created_date_time=created_date_time,
                              owner=owner,
                              title=title,
                              contexts=contexts,
                              tasks=tasks,
                              buckets=buckets,
                              microsoft_graph_entity_id=details_id,
                              shared_with=details_shared_with,
                              category_descriptions=details_category_descriptions,
                              context_details=details_context_details,
                              application=created_by_application,
                              device=created_by_device,
                              user=created_by_user)


def groupsplanner_create_bucket(client,
                                group_id,
                                planner_plan_id,
                                id_=None,
                                name=None,
                                plan_id=None,
                                order_hint=None,
                                tasks=None):
    return client.create_bucket(group_id=group_id,
                                planner_plan_id=planner_plan_id,
                                id=id_,
                                name=name,
                                plan_id=plan_id,
                                order_hint=order_hint,
                                tasks=tasks)


def groupsplanner_create_task(client,
                              group_id,
                              planner_plan_id,
                              body):
    return client.create_task(group_id=group_id,
                              planner_plan_id=planner_plan_id,
                              body=body)


def groupsplanner_get_bucket(client,
                             group_id,
                             planner_plan_id,
                             planner_bucket_id,
                             select=None,
                             expand=None):
    return client.get_bucket(group_id=group_id,
                             planner_plan_id=planner_plan_id,
                             planner_bucket_id=planner_bucket_id,
                             select=select,
                             expand=expand)


def groupsplanner_get_detail(client,
                             group_id,
                             planner_plan_id,
                             select=None,
                             expand=None):
    return client.get_detail(group_id=group_id,
                             planner_plan_id=planner_plan_id,
                             select=select,
                             expand=expand)


def groupsplanner_get_task(client,
                           group_id,
                           planner_plan_id,
                           planner_task_id,
                           select=None,
                           expand=None):
    return client.get_task(group_id=group_id,
                           planner_plan_id=planner_plan_id,
                           planner_task_id=planner_task_id,
                           select=select,
                           expand=expand)


def groupsplanner_list_bucket(client,
                              group_id,
                              planner_plan_id,
                              orderby=None,
                              select=None,
                              expand=None):
    return client.list_bucket(group_id=group_id,
                              planner_plan_id=planner_plan_id,
                              orderby=orderby,
                              select=select,
                              expand=expand)


def groupsplanner_list_task(client,
                            group_id,
                            planner_plan_id,
                            orderby=None,
                            select=None,
                            expand=None):
    return client.list_task(group_id=group_id,
                            planner_plan_id=planner_plan_id,
                            orderby=orderby,
                            select=select,
                            expand=expand)


def groupsplanner_update_bucket(client,
                                group_id,
                                planner_plan_id,
                                planner_bucket_id,
                                id_=None,
                                name=None,
                                plan_id=None,
                                order_hint=None,
                                tasks=None):
    return client.update_bucket(group_id=group_id,
                                planner_plan_id=planner_plan_id,
                                planner_bucket_id=planner_bucket_id,
                                id=id_,
                                name=name,
                                plan_id=plan_id,
                                order_hint=order_hint,
                                tasks=tasks)


def groupsplanner_update_detail(client,
                                group_id,
                                planner_plan_id,
                                id_=None,
                                shared_with=None,
                                category_descriptions=None,
                                context_details=None):
    return client.update_detail(group_id=group_id,
                                planner_plan_id=planner_plan_id,
                                id=id_,
                                shared_with=shared_with,
                                category_descriptions=category_descriptions,
                                context_details=context_details)


def groupsplanner_update_task(client,
                              group_id,
                              planner_plan_id,
                              planner_task_id,
                              body):
    return client.update_task(group_id=group_id,
                              planner_plan_id=planner_plan_id,
                              planner_task_id=planner_task_id,
                              body=body)


def groupsplanner_create_task(client,
                              group_id,
                              planner_plan_id,
                              planner_bucket_id,
                              body):
    return client.create_task(group_id=group_id,
                              planner_plan_id=planner_plan_id,
                              planner_bucket_id=planner_bucket_id,
                              body=body)


def groupsplanner_get_task(client,
                           group_id,
                           planner_plan_id,
                           planner_bucket_id,
                           planner_task_id,
                           select=None,
                           expand=None):
    return client.get_task(group_id=group_id,
                           planner_plan_id=planner_plan_id,
                           planner_bucket_id=planner_bucket_id,
                           planner_task_id=planner_task_id,
                           select=select,
                           expand=expand)


def groupsplanner_list_task(client,
                            group_id,
                            planner_plan_id,
                            planner_bucket_id,
                            orderby=None,
                            select=None,
                            expand=None):
    return client.list_task(group_id=group_id,
                            planner_plan_id=planner_plan_id,
                            planner_bucket_id=planner_bucket_id,
                            orderby=orderby,
                            select=select,
                            expand=expand)


def groupsplanner_update_task(client,
                              group_id,
                              planner_plan_id,
                              planner_bucket_id,
                              planner_task_id,
                              body):
    return client.update_task(group_id=group_id,
                              planner_plan_id=planner_plan_id,
                              planner_bucket_id=planner_bucket_id,
                              planner_task_id=planner_task_id,
                              body=body)


def groupsplanner_get_assigned_to_task_board_format(client,
                                                    group_id,
                                                    planner_plan_id,
                                                    planner_bucket_id,
                                                    planner_task_id,
                                                    select=None,
                                                    expand=None):
    return client.get_assigned_to_task_board_format(group_id=group_id,
                                                    planner_plan_id=planner_plan_id,
                                                    planner_bucket_id=planner_bucket_id,
                                                    planner_task_id=planner_task_id,
                                                    select=select,
                                                    expand=expand)


def groupsplanner_get_bucket_task_board_format(client,
                                               group_id,
                                               planner_plan_id,
                                               planner_bucket_id,
                                               planner_task_id,
                                               select=None,
                                               expand=None):
    return client.get_bucket_task_board_format(group_id=group_id,
                                               planner_plan_id=planner_plan_id,
                                               planner_bucket_id=planner_bucket_id,
                                               planner_task_id=planner_task_id,
                                               select=select,
                                               expand=expand)


def groupsplanner_get_detail(client,
                             group_id,
                             planner_plan_id,
                             planner_bucket_id,
                             planner_task_id,
                             select=None,
                             expand=None):
    return client.get_detail(group_id=group_id,
                             planner_plan_id=planner_plan_id,
                             planner_bucket_id=planner_bucket_id,
                             planner_task_id=planner_task_id,
                             select=select,
                             expand=expand)


def groupsplanner_get_progress_task_board_format(client,
                                                 group_id,
                                                 planner_plan_id,
                                                 planner_bucket_id,
                                                 planner_task_id,
                                                 select=None,
                                                 expand=None):
    return client.get_progress_task_board_format(group_id=group_id,
                                                 planner_plan_id=planner_plan_id,
                                                 planner_bucket_id=planner_bucket_id,
                                                 planner_task_id=planner_task_id,
                                                 select=select,
                                                 expand=expand)


def groupsplanner_update_assigned_to_task_board_format(client,
                                                       group_id,
                                                       planner_plan_id,
                                                       planner_bucket_id,
                                                       planner_task_id,
                                                       id_=None,
                                                       unassigned_order_hint=None,
                                                       order_hints_by_assignee=None):
    return client.update_assigned_to_task_board_format(group_id=group_id,
                                                       planner_plan_id=planner_plan_id,
                                                       planner_bucket_id=planner_bucket_id,
                                                       planner_task_id=planner_task_id,
                                                       id=id_,
                                                       unassigned_order_hint=unassigned_order_hint,
                                                       order_hints_by_assignee=order_hints_by_assignee)


def groupsplanner_update_bucket_task_board_format(client,
                                                  group_id,
                                                  planner_plan_id,
                                                  planner_bucket_id,
                                                  planner_task_id,
                                                  id_=None,
                                                  order_hint=None):
    return client.update_bucket_task_board_format(group_id=group_id,
                                                  planner_plan_id=planner_plan_id,
                                                  planner_bucket_id=planner_bucket_id,
                                                  planner_task_id=planner_task_id,
                                                  id=id_,
                                                  order_hint=order_hint)


def groupsplanner_update_detail(client,
                                group_id,
                                planner_plan_id,
                                planner_bucket_id,
                                planner_task_id,
                                id_=None,
                                description=None,
                                preview_type=None,
                                references=None,
                                checklist=None):
    return client.update_detail(group_id=group_id,
                                planner_plan_id=planner_plan_id,
                                planner_bucket_id=planner_bucket_id,
                                planner_task_id=planner_task_id,
                                id=id_,
                                description=description,
                                preview_type=preview_type,
                                references=references,
                                checklist=checklist)


def groupsplanner_update_progress_task_board_format(client,
                                                    group_id,
                                                    planner_plan_id,
                                                    planner_bucket_id,
                                                    planner_task_id,
                                                    id_=None,
                                                    order_hint=None):
    return client.update_progress_task_board_format(group_id=group_id,
                                                    planner_plan_id=planner_plan_id,
                                                    planner_bucket_id=planner_bucket_id,
                                                    planner_task_id=planner_task_id,
                                                    id=id_,
                                                    order_hint=order_hint)


def groupsplanner_get_assigned_to_task_board_format(client,
                                                    group_id,
                                                    planner_plan_id,
                                                    planner_task_id,
                                                    select=None,
                                                    expand=None):
    return client.get_assigned_to_task_board_format(group_id=group_id,
                                                    planner_plan_id=planner_plan_id,
                                                    planner_task_id=planner_task_id,
                                                    select=select,
                                                    expand=expand)


def groupsplanner_get_bucket_task_board_format(client,
                                               group_id,
                                               planner_plan_id,
                                               planner_task_id,
                                               select=None,
                                               expand=None):
    return client.get_bucket_task_board_format(group_id=group_id,
                                               planner_plan_id=planner_plan_id,
                                               planner_task_id=planner_task_id,
                                               select=select,
                                               expand=expand)


def groupsplanner_get_detail(client,
                             group_id,
                             planner_plan_id,
                             planner_task_id,
                             select=None,
                             expand=None):
    return client.get_detail(group_id=group_id,
                             planner_plan_id=planner_plan_id,
                             planner_task_id=planner_task_id,
                             select=select,
                             expand=expand)


def groupsplanner_get_progress_task_board_format(client,
                                                 group_id,
                                                 planner_plan_id,
                                                 planner_task_id,
                                                 select=None,
                                                 expand=None):
    return client.get_progress_task_board_format(group_id=group_id,
                                                 planner_plan_id=planner_plan_id,
                                                 planner_task_id=planner_task_id,
                                                 select=select,
                                                 expand=expand)


def groupsplanner_update_assigned_to_task_board_format(client,
                                                       group_id,
                                                       planner_plan_id,
                                                       planner_task_id,
                                                       id_=None,
                                                       unassigned_order_hint=None,
                                                       order_hints_by_assignee=None):
    return client.update_assigned_to_task_board_format(group_id=group_id,
                                                       planner_plan_id=planner_plan_id,
                                                       planner_task_id=planner_task_id,
                                                       id=id_,
                                                       unassigned_order_hint=unassigned_order_hint,
                                                       order_hints_by_assignee=order_hints_by_assignee)


def groupsplanner_update_bucket_task_board_format(client,
                                                  group_id,
                                                  planner_plan_id,
                                                  planner_task_id,
                                                  id_=None,
                                                  order_hint=None):
    return client.update_bucket_task_board_format(group_id=group_id,
                                                  planner_plan_id=planner_plan_id,
                                                  planner_task_id=planner_task_id,
                                                  id=id_,
                                                  order_hint=order_hint)


def groupsplanner_update_detail(client,
                                group_id,
                                planner_plan_id,
                                planner_task_id,
                                id_=None,
                                description=None,
                                preview_type=None,
                                references=None,
                                checklist=None):
    return client.update_detail(group_id=group_id,
                                planner_plan_id=planner_plan_id,
                                planner_task_id=planner_task_id,
                                id=id_,
                                description=description,
                                preview_type=preview_type,
                                references=references,
                                checklist=checklist)


def groupsplanner_update_progress_task_board_format(client,
                                                    group_id,
                                                    planner_plan_id,
                                                    planner_task_id,
                                                    id_=None,
                                                    order_hint=None):
    return client.update_progress_task_board_format(group_id=group_id,
                                                    planner_plan_id=planner_plan_id,
                                                    planner_task_id=planner_task_id,
                                                    id=id_,
                                                    order_hint=order_hint)
