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

import json


def msgraphusersuser_user_user_update(client,
                                      user_id,
                                      body):
    if isinstance(body, str):
        body = json.loads(body)
    return client.update_user(user_id=user_id,
                              body=body)


def msgraphusersuser_user_user_delete(client,
                                      user_id,
                                      if_match=None):
    return client.delete_user(user_id=user_id,
                              if_match=if_match)


def msgraphusersuser_user_user_create_user(client,
                                           body):
    if isinstance(body, str):
        body = json.loads(body)
    return client.create_user(body=body)


def msgraphusersuser_user_user_get_user(client,
                                        user_id,
                                        select=None,
                                        expand=None):
    return client.get_user(user_id=user_id,
                           select=select,
                           expand=expand)


def msgraphusersuser_user_user_list_user(client,
                                         orderby=None,
                                         select=None,
                                         expand=None):
    return client.list_user(orderby=orderby,
                            select=select,
                            expand=expand)


def msgraphusersuser_user_update(client,
                                 user_id,
                                 id_=None,
                                 availability=None,
                                 activity=None):
    return client.update_presence(user_id=user_id,
                                  id=id_,
                                  availability=availability,
                                  activity=activity)


def msgraphusersuser_user_get_presence(client,
                                       user_id,
                                       select=None,
                                       expand=None):
    return client.get_presence(user_id=user_id,
                               select=select,
                               expand=expand)
