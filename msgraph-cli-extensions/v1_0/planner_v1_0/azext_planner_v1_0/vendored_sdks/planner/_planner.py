# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import PlannerConfiguration
from .operations import GroupsOperations
from .operations import GroupsPlannerOperations
from .operations import GroupsPlannerPlansOperations
from .operations import GroupsPlannerPlansBucketsOperations
from .operations import GroupsPlannerPlansBucketsTasksOperations
from .operations import GroupsPlannerPlansTasksOperations
from .operations import PlannerPlannerOperations
from .operations import PlannerOperations
from .operations import PlannerBucketsOperations
from .operations import PlannerBucketsTasksOperations
from .operations import PlannerPlansOperations
from .operations import PlannerPlansBucketsOperations
from .operations import PlannerPlansBucketsTasksOperations
from .operations import PlannerPlansTasksOperations
from .operations import PlannerTasksOperations
from .operations import UsersOperations
from .operations import UsersPlannerOperations
from .operations import UsersPlannerPlansOperations
from .operations import UsersPlannerPlansBucketsOperations
from .operations import UsersPlannerPlansBucketsTasksOperations
from .operations import UsersPlannerPlansTasksOperations
from .operations import UsersPlannerTasksOperations
from . import models


class Planner(object):
    """Planner.

    :ivar groups: GroupsOperations operations
    :vartype groups: planner.operations.GroupsOperations
    :ivar groups_planner: GroupsPlannerOperations operations
    :vartype groups_planner: planner.operations.GroupsPlannerOperations
    :ivar groups_planner_plans: GroupsPlannerPlansOperations operations
    :vartype groups_planner_plans: planner.operations.GroupsPlannerPlansOperations
    :ivar groups_planner_plans_buckets: GroupsPlannerPlansBucketsOperations operations
    :vartype groups_planner_plans_buckets: planner.operations.GroupsPlannerPlansBucketsOperations
    :ivar groups_planner_plans_buckets_tasks: GroupsPlannerPlansBucketsTasksOperations operations
    :vartype groups_planner_plans_buckets_tasks: planner.operations.GroupsPlannerPlansBucketsTasksOperations
    :ivar groups_planner_plans_tasks: GroupsPlannerPlansTasksOperations operations
    :vartype groups_planner_plans_tasks: planner.operations.GroupsPlannerPlansTasksOperations
    :ivar planner_planner: PlannerPlannerOperations operations
    :vartype planner_planner: planner.operations.PlannerPlannerOperations
    :ivar planner: PlannerOperations operations
    :vartype planner: planner.operations.PlannerOperations
    :ivar planner_buckets: PlannerBucketsOperations operations
    :vartype planner_buckets: planner.operations.PlannerBucketsOperations
    :ivar planner_buckets_tasks: PlannerBucketsTasksOperations operations
    :vartype planner_buckets_tasks: planner.operations.PlannerBucketsTasksOperations
    :ivar planner_plans: PlannerPlansOperations operations
    :vartype planner_plans: planner.operations.PlannerPlansOperations
    :ivar planner_plans_buckets: PlannerPlansBucketsOperations operations
    :vartype planner_plans_buckets: planner.operations.PlannerPlansBucketsOperations
    :ivar planner_plans_buckets_tasks: PlannerPlansBucketsTasksOperations operations
    :vartype planner_plans_buckets_tasks: planner.operations.PlannerPlansBucketsTasksOperations
    :ivar planner_plans_tasks: PlannerPlansTasksOperations operations
    :vartype planner_plans_tasks: planner.operations.PlannerPlansTasksOperations
    :ivar planner_tasks: PlannerTasksOperations operations
    :vartype planner_tasks: planner.operations.PlannerTasksOperations
    :ivar users: UsersOperations operations
    :vartype users: planner.operations.UsersOperations
    :ivar users_planner: UsersPlannerOperations operations
    :vartype users_planner: planner.operations.UsersPlannerOperations
    :ivar users_planner_plans: UsersPlannerPlansOperations operations
    :vartype users_planner_plans: planner.operations.UsersPlannerPlansOperations
    :ivar users_planner_plans_buckets: UsersPlannerPlansBucketsOperations operations
    :vartype users_planner_plans_buckets: planner.operations.UsersPlannerPlansBucketsOperations
    :ivar users_planner_plans_buckets_tasks: UsersPlannerPlansBucketsTasksOperations operations
    :vartype users_planner_plans_buckets_tasks: planner.operations.UsersPlannerPlansBucketsTasksOperations
    :ivar users_planner_plans_tasks: UsersPlannerPlansTasksOperations operations
    :vartype users_planner_plans_tasks: planner.operations.UsersPlannerPlansTasksOperations
    :ivar users_planner_tasks: UsersPlannerTasksOperations operations
    :vartype users_planner_tasks: planner.operations.UsersPlannerTasksOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param top: Show only the first n items.
    :type top: int
    :param skip: Skip the first n items.
    :type skip: int
    :param search: Search items by search phrases.
    :type search: str
    :param filter: Filter items by property values.
    :type filter: str
    :param count: Include count of items.
    :type count: bool
    :param str base_url: Service URL
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        top=None,  # type: Optional[int]
        skip=None,  # type: Optional[int]
        search=None,  # type: Optional[str]
        filter=None,  # type: Optional[str]
        count=None,  # type: Optional[bool]
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://graph.microsoft.com/v1.0'
        self._config = PlannerConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.groups = GroupsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groups_planner = GroupsPlannerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groups_planner_plans = GroupsPlannerPlansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groups_planner_plans_buckets = GroupsPlannerPlansBucketsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groups_planner_plans_buckets_tasks = GroupsPlannerPlansBucketsTasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.groups_planner_plans_tasks = GroupsPlannerPlansTasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_planner = PlannerPlannerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner = PlannerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_buckets = PlannerBucketsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_buckets_tasks = PlannerBucketsTasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_plans = PlannerPlansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_plans_buckets = PlannerPlansBucketsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_plans_buckets_tasks = PlannerPlansBucketsTasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_plans_tasks = PlannerPlansTasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.planner_tasks = PlannerTasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users = UsersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_planner = UsersPlannerOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_planner_plans = UsersPlannerPlansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_planner_plans_buckets = UsersPlannerPlansBucketsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_planner_plans_buckets_tasks = UsersPlannerPlansBucketsTasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_planner_plans_tasks = UsersPlannerPlansTasksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.users_planner_tasks = UsersPlannerTasksOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> Planner
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
