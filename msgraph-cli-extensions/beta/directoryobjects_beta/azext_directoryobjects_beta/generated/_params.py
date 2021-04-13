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
# pylint: disable=too-many-statements

from msgraph.cli.core.commands.parameters import get_three_state_flag


def load_arguments(self, _):

    with self.argument_context('directoryobjects directory-object-directory-object delete') as c:
        c.argument('directory_object_id', type=str, help='key: id of directoryObject')
        c.argument('if_match', type=str, help='ETag')

    with self.argument_context('directoryobjects directory-object-directory-object create-directory-object') as c:
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('deleted_date_time', help='')

    with self.argument_context('directoryobjects directory-object-directory-object list-directory-object') as c:
        c.argument('orderby', nargs='+', help='Order items by property values')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('directoryobjects directory-object-directory-object show-directory-object') as c:
        c.argument('directory_object_id', type=str, help='key: id of directoryObject')
        c.argument('select', nargs='+', help='Select properties to be returned')
        c.argument('expand', nargs='+', help='Expand related entities')

    with self.argument_context('directoryobjects directory-object-directory-object update-directory-object') as c:
        c.argument('directory_object_id', type=str, help='key: id of directoryObject')
        c.argument('id_', options_list=['--id'], type=str, help='Read-only.')
        c.argument('deleted_date_time', help='')

    with self.argument_context('directoryobjects directory-object check-member-group') as c:
        c.argument('directory_object_id', type=str, help='key: id of directoryObject')
        c.argument('group_ids', nargs='+', help='')

    with self.argument_context('directoryobjects directory-object check-member-object') as c:
        c.argument('directory_object_id', type=str, help='key: id of directoryObject')
        c.argument('ids', nargs='+', help='')

    with self.argument_context('directoryobjects directory-object get-by-id') as c:
        c.argument('ids', nargs='+', help='')
        c.argument('types', nargs='+', help='')

    with self.argument_context('directoryobjects directory-object get-member-group') as c:
        c.argument('directory_object_id', type=str, help='key: id of directoryObject')
        c.argument('security_enabled_only', arg_type=get_three_state_flag(), help='')

    with self.argument_context('directoryobjects directory-object get-member-object') as c:
        c.argument('directory_object_id', type=str, help='key: id of directoryObject')
        c.argument('security_enabled_only', arg_type=get_three_state_flag(), help='')

    with self.argument_context('directoryobjects directory-object get-user-owned-object') as c:
        c.argument('user_id', type=str, help='')
        c.argument('type_', options_list=['--type'], type=str, help='')

    with self.argument_context('directoryobjects directory-object restore') as c:
        c.argument('directory_object_id', type=str, help='key: id of directoryObject')

    with self.argument_context('directoryobjects directory-object validate-property') as c:
        c.argument('entity_type', type=str, help='')
        c.argument('display_name', type=str, help='')
        c.argument('mail_nickname', type=str, help='')
        c.argument('on_behalf_of_user_id', help='')
