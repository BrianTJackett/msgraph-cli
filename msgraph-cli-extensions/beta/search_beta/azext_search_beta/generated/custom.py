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


def search_external_external_get_external(client,
                                          select=None,
                                          expand=None):
    return client.get_external(select=select,
                               expand=expand)


def search_external_external_update_external(client,
                                             connections=None):
    return client.update_external(connections=connections)


def search_external_delete(client,
                           external_connection_id,
                           if_match=None):
    return client.delete_connection(external_connection_id=external_connection_id,
                                    if_match=if_match)


def search_external_create_connection(client,
                                      id_=None,
                                      configuration=None,
                                      description=None,
                                      name=None,
                                      state=None,
                                      groups=None,
                                      items=None,
                                      operations=None,
                                      schema_id=None,
                                      schema_base_type=None,
                                      schema_properties=None):
    return client.create_connection(id=id_,
                                    configuration=configuration,
                                    description=description,
                                    name=name,
                                    state=state,
                                    groups=groups,
                                    items=items,
                                    operations=operations,
                                    microsoft_graph_entity_id=schema_id,
                                    base_type=schema_base_type,
                                    properties=schema_properties)


def search_external_get_connection(client,
                                   external_connection_id,
                                   select=None,
                                   expand=None):
    return client.get_connection(external_connection_id=external_connection_id,
                                 select=select,
                                 expand=expand)


def search_external_list_connection(client,
                                    orderby=None,
                                    select=None,
                                    expand=None):
    return client.list_connection(orderby=orderby,
                                  select=select,
                                  expand=expand)


def search_external_update_connection(client,
                                      external_connection_id,
                                      id_=None,
                                      configuration=None,
                                      description=None,
                                      name=None,
                                      state=None,
                                      groups=None,
                                      items=None,
                                      operations=None,
                                      schema_id=None,
                                      schema_base_type=None,
                                      schema_properties=None):
    return client.update_connection(external_connection_id=external_connection_id,
                                    id=id_,
                                    configuration=configuration,
                                    description=description,
                                    name=name,
                                    state=state,
                                    groups=groups,
                                    items=items,
                                    operations=operations,
                                    microsoft_graph_entity_id=schema_id,
                                    base_type=schema_base_type,
                                    properties=schema_properties)


def search_search_search_entity_geth_entity(client,
                                            select=None,
                                            expand=None):
    return client.get_search_entity(select=select,
                                    expand=expand)


def search_search_search_entity_updateh_entity(client,
                                               id_=None):
    return client.update_search_entity(id=id_)


def search_search_query(client,
                        requests=None):
    return client.query(requests=requests)
