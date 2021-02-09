# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_identitydirmgt_v1_0_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_identitydirmgt_v1_0.vendored_sdks.identitydirmgt import IdentityDirectoryManagement
    return get_mgmt_service_client(cli_ctx,
                                   IdentityDirectoryManagement,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_contact_org_contact(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).contacts_org_contact


def cf_contact(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).contacts


def cf_contract_contract(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).contracts_contract


def cf_contract(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).contracts


def cf_device_device(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).devices_device


def cf_device(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).devices


def cf_directory_directory(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).directory_directory


def cf_directory(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).directory


def cf_directory_administrative_unit(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).directory_administrative_units


def cf_directory_role_directory_role(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).directory_roles_directory_role


def cf_directory_role(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).directory_roles


def cf_directory_role_template_directory_role_template(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).directory_role_templates_directory_role_template


def cf_directory_role_template(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).directory_role_templates


def cf_domain_domain(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).domains_domain


def cf_domain(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).domains


def cf_organization_organization(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).organization_organization


def cf_organization(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).organization


def cf_subscribed_sku_subscribed_sku(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).subscribed_skus_subscribed_sku


def cf_user(cli_ctx, *_):
    return cf_identitydirmgt_v1_0_cl(cli_ctx).users
