# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


def cf_sites_cl(cli_ctx, *_):
    from azure.cli.core.commands.client_factory import get_mgmt_service_client
    from azext_sites.vendored_sdks.sites import Sites
    return get_mgmt_service_client(cli_ctx,
                                   Sites,
                                   subscription_bound=False,
                                   base_url_bound=False)


def cf_group(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).groups


def cf_site_site(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_site


def cf_site(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites


def cf_site_content_type(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_content_types


def cf_site_list(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_lists


def cf_site_list_content_type(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_lists_content_types


def cf_site_list_item(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_lists_items


def cf_site_list_item_version(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_lists_items_versions


def cf_site_onenote_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_notebooks


def cf_site_onenote_notebook_section_group_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_notebooks_section_groups_parent_notebook


def cf_site_onenote_notebook_section_group_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_notebooks_section_groups_sections


def cf_site_onenote_notebook_section_group_section_page(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_notebooks_section_groups_sections_pages


def cf_site_onenote_notebook_section_group_section_page_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_notebooks_section_groups_sections_pages_parent_notebook


def cf_site_onenote_notebook_section_group_section_page_parent_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_notebooks_section_groups_sections_pages_parent_section


def cf_site_onenote_notebook_section_group_section_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_notebooks_section_groups_sections_parent_notebook


def cf_site_onenote_notebook_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_notebooks_sections


def cf_site_onenote_notebook_section_page(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_notebooks_sections_pages


def cf_site_onenote_notebook_section_page_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_notebooks_sections_pages_parent_notebook


def cf_site_onenote_notebook_section_page_parent_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_notebooks_sections_pages_parent_section


def cf_site_onenote_notebook_section_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_notebooks_sections_parent_notebook


def cf_site_onenote_notebook_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_notebooks_sections_parent_section_group_parent_notebook


def cf_site_onenote_notebook_section_parent_section_group_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_notebooks_sections_parent_section_group_sections


def cf_site_onenote_page(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages


def cf_site_onenote_page_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_notebook


def cf_site_onenote_page_parent_notebook_section_group_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_notebook_section_groups_parent_notebook


def cf_site_onenote_page_parent_notebook_section_group_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_notebook_section_groups_sections


def cf_site_onenote_page_parent_notebook_section_group_section_page(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_notebook_section_groups_sections_pages


def cf_site_onenote_page_parent_notebook_section_group_section_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_notebook_section_groups_sections_parent_notebook


def cf_site_onenote_page_parent_notebook_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_notebook_sections


def cf_site_onenote_page_parent_notebook_section_page(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_notebook_sections_pages


def cf_site_onenote_page_parent_notebook_section_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_notebook_sections_parent_notebook


def cf_site_onenote_page_parent_notebook_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_notebook_sections_parent_section_group_parent_notebook


def cf_site_onenote_page_parent_notebook_section_parent_section_group_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_notebook_sections_parent_section_group_sections


def cf_site_onenote_page_parent_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_section


def cf_site_onenote_page_parent_section_page(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_section_pages


def cf_site_onenote_page_parent_section_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_section_parent_notebook


def cf_site_onenote_page_parent_section_parent_notebook_section_group_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_section_parent_notebook_section_groups_parent_notebook


def cf_site_onenote_page_parent_section_parent_notebook_section_group_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_section_parent_notebook_section_groups_sections


def cf_site_onenote_page_parent_section_parent_notebook_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_section_parent_notebook_sections


def cf_site_onenote_page_parent_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_section_parent_section_group_parent_notebook


def cf_site_onenote_page_parent_section_parent_section_group_parent_notebook_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_section_parent_section_group_parent_notebook_sections


def cf_site_onenote_page_parent_section_parent_section_group_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_pages_parent_section_parent_section_group_sections


def cf_site_onenote_section_group_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_section_groups_parent_notebook


def cf_site_onenote_section_group_parent_notebook_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_section_groups_parent_notebook_sections


def cf_site_onenote_section_group_parent_notebook_section_page(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_section_groups_parent_notebook_sections_pages


def cf_site_onenote_section_group_parent_notebook_section_page_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_section_groups_parent_notebook_sections_pages_parent_notebook


def cf_site_onenote_section_group_parent_notebook_section_page_parent_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_section_groups_parent_notebook_sections_pages_parent_section


def cf_site_onenote_section_group_parent_notebook_section_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_section_groups_parent_notebook_sections_parent_notebook


def cf_site_onenote_section_group_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_section_groups_sections


def cf_site_onenote_section_group_section_page(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_section_groups_sections_pages


def cf_site_onenote_section_group_section_page_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_section_groups_sections_pages_parent_notebook


def cf_site_onenote_section_group_section_page_parent_notebook_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_section_groups_sections_pages_parent_notebook_sections


def cf_site_onenote_section_group_section_page_parent_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_section_groups_sections_pages_parent_section


def cf_site_onenote_section_group_section_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_section_groups_sections_parent_notebook


def cf_site_onenote_section_group_section_parent_notebook_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_section_groups_sections_parent_notebook_sections


def cf_site_onenote_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_sections


def cf_site_onenote_section_page(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_sections_pages


def cf_site_onenote_section_page_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_sections_pages_parent_notebook


def cf_site_onenote_section_page_parent_notebook_section_group_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_sections_pages_parent_notebook_section_groups_parent_notebook


def cf_site_onenote_section_page_parent_notebook_section_group_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_sections_pages_parent_notebook_section_groups_sections


def cf_site_onenote_section_page_parent_notebook_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_sections_pages_parent_notebook_sections


def cf_site_onenote_section_page_parent_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_sections_pages_parent_section


def cf_site_onenote_section_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_sections_parent_notebook


def cf_site_onenote_section_parent_notebook_section_group_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_sections_parent_notebook_section_groups_parent_notebook


def cf_site_onenote_section_parent_notebook_section_group_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_sections_parent_notebook_section_groups_sections


def cf_site_onenote_section_parent_notebook_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_sections_parent_notebook_sections


def cf_site_onenote_section_parent_section_group_parent_notebook(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_sections_parent_section_group_parent_notebook


def cf_site_onenote_section_parent_section_group_parent_notebook_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_sections_parent_section_group_parent_notebook_sections


def cf_site_onenote_section_parent_section_group_section(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).sites_onenote_sections_parent_section_group_sections


def cf_user(cli_ctx, *_):
    return cf_sites_cl(cli_ctx).users
