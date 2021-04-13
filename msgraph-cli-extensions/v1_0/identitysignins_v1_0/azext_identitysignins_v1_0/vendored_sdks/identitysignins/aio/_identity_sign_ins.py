# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import Any, Optional, TYPE_CHECKING

from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

from ._configuration import IdentitySignInsConfiguration
from .operations import DataPolicyOperationDataPolicyOperationOperations
from .operations import IdentityOperations
from .operations import IdentityConditionalAccessOperations
from .operations import IdentityProviderIdentityProviderOperations
from .operations import InformationProtectionInformationProtectionOperations
from .operations import InformationProtectionOperations
from .operations import InformationProtectionThreatAssessmentRequestOperations
from .operations import InvitationInvitationOperations
from .operations import InvitationOperations
from .operations import Oauth2PermissionGrantOAuth2PermissionGrantOperations
from .operations import Oauth2PermissionGrantOperations
from .operations import OrganizationOperations
from .operations import PolicyPolicyRootOperations
from .operations import PolicyOperations
from .operations import PolicyPermissionGrantPolicyOperations
from .. import models


class IdentitySignIns(object):
    """IdentitySignIns.

    :ivar data_policy_operation_data_policy_operation: DataPolicyOperationDataPolicyOperationOperations operations
    :vartype data_policy_operation_data_policy_operation: identity_sign_ins.aio.operations.DataPolicyOperationDataPolicyOperationOperations
    :ivar identity: IdentityOperations operations
    :vartype identity: identity_sign_ins.aio.operations.IdentityOperations
    :ivar identity_conditional_access: IdentityConditionalAccessOperations operations
    :vartype identity_conditional_access: identity_sign_ins.aio.operations.IdentityConditionalAccessOperations
    :ivar identity_provider_identity_provider: IdentityProviderIdentityProviderOperations operations
    :vartype identity_provider_identity_provider: identity_sign_ins.aio.operations.IdentityProviderIdentityProviderOperations
    :ivar information_protection_information_protection: InformationProtectionInformationProtectionOperations operations
    :vartype information_protection_information_protection: identity_sign_ins.aio.operations.InformationProtectionInformationProtectionOperations
    :ivar information_protection: InformationProtectionOperations operations
    :vartype information_protection: identity_sign_ins.aio.operations.InformationProtectionOperations
    :ivar information_protection_threat_assessment_request: InformationProtectionThreatAssessmentRequestOperations operations
    :vartype information_protection_threat_assessment_request: identity_sign_ins.aio.operations.InformationProtectionThreatAssessmentRequestOperations
    :ivar invitation_invitation: InvitationInvitationOperations operations
    :vartype invitation_invitation: identity_sign_ins.aio.operations.InvitationInvitationOperations
    :ivar invitation: InvitationOperations operations
    :vartype invitation: identity_sign_ins.aio.operations.InvitationOperations
    :ivar oauth2_permission_grant_oauth2_permission_grant: Oauth2PermissionGrantOAuth2PermissionGrantOperations operations
    :vartype oauth2_permission_grant_oauth2_permission_grant: identity_sign_ins.aio.operations.Oauth2PermissionGrantOAuth2PermissionGrantOperations
    :ivar oauth2_permission_grant: Oauth2PermissionGrantOperations operations
    :vartype oauth2_permission_grant: identity_sign_ins.aio.operations.Oauth2PermissionGrantOperations
    :ivar organization: OrganizationOperations operations
    :vartype organization: identity_sign_ins.aio.operations.OrganizationOperations
    :ivar policy_policy_root: PolicyPolicyRootOperations operations
    :vartype policy_policy_root: identity_sign_ins.aio.operations.PolicyPolicyRootOperations
    :ivar policy: PolicyOperations operations
    :vartype policy: identity_sign_ins.aio.operations.PolicyOperations
    :ivar policy_permission_grant_policy: PolicyPermissionGrantPolicyOperations operations
    :vartype policy_permission_grant_policy: identity_sign_ins.aio.operations.PolicyPermissionGrantPolicyOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
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
        credential: "AsyncTokenCredential",
        top: Optional[int] = None,
        skip: Optional[int] = None,
        search: Optional[str] = None,
        filter: Optional[str] = None,
        count: Optional[bool] = None,
        base_url: Optional[str] = None,
        **kwargs: Any
    ) -> None:
        if not base_url:
            base_url = 'https://graph.microsoft.com/v1.0'
        self._config = IdentitySignInsConfiguration(credential, top, skip, search, filter, count, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.data_policy_operation_data_policy_operation = DataPolicyOperationDataPolicyOperationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.identity = IdentityOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.identity_conditional_access = IdentityConditionalAccessOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.identity_provider_identity_provider = IdentityProviderIdentityProviderOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.information_protection_information_protection = InformationProtectionInformationProtectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.information_protection = InformationProtectionOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.information_protection_threat_assessment_request = InformationProtectionThreatAssessmentRequestOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.invitation_invitation = InvitationInvitationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.invitation = InvitationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.oauth2_permission_grant_oauth2_permission_grant = Oauth2PermissionGrantOAuth2PermissionGrantOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.oauth2_permission_grant = Oauth2PermissionGrantOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.organization = OrganizationOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policy_policy_root = PolicyPolicyRootOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policy = PolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.policy_permission_grant_policy = PolicyPermissionGrantPolicyOperations(
            self._client, self._config, self._serialize, self._deserialize)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "IdentitySignIns":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
