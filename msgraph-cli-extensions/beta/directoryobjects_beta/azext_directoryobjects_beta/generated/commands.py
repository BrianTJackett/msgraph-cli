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
from azext_directoryobjects_beta.generated._client_factory import (
    cf_directory_object_directory_object,
    cf_directory_object,
)


directoryobjects_beta_directory_object_directory_object = CliCommandType(
    operations_tmpl='azext_directoryobjects_beta.vendored_sdks.directoryobjects.operations._directory_object_directory_object_operations#DirectoryObjectDirectoryObjectOperations.{}',
    client_factory=cf_directory_object_directory_object,
)


directoryobjects_beta_directory_object = CliCommandType(
    operations_tmpl='azext_directoryobjects_beta.vendored_sdks.directoryobjects.operations._directory_object_operations#DirectoryObjectOperations.{}',
    client_factory=cf_directory_object,
)


def load_command_table(self, _):

    with self.command_group(
        'directoryobjects directory-object-directory-object',
        directoryobjects_beta_directory_object_directory_object,
        client_factory=cf_directory_object_directory_object,
    ) as g:
        g.custom_command(
            'create-directory-object', 'directoryobjects_directory_object_directory_object_create_directory_object'
        )
        g.custom_command(
            'delete-directory-object', 'directoryobjects_directory_object_directory_object_delete_directory_object'
        )
        g.custom_command(
            'list-directory-object', 'directoryobjects_directory_object_directory_object_list_directory_object'
        )
        g.custom_command(
            'show-directory-object', 'directoryobjects_directory_object_directory_object_show_directory_object'
        )
        g.custom_command(
            'update-directory-object', 'directoryobjects_directory_object_directory_object_update_directory_object'
        )

    with self.command_group(
        'directoryobjects directory-object', directoryobjects_beta_directory_object, client_factory=cf_directory_object
    ) as g:
        g.custom_command('check-member-group', 'directoryobjects_directory_object_check_member_group')
        g.custom_command('check-member-object', 'directoryobjects_directory_object_check_member_object')
        g.custom_command('get-by-id', 'directoryobjects_directory_object_get_by_id')
        g.custom_command('get-member-group', 'directoryobjects_directory_object_get_member_group')
        g.custom_command('get-member-object', 'directoryobjects_directory_object_get_member_object')
        g.custom_command('get-user-owned-object', 'directoryobjects_directory_object_get_user_owned_object')
        g.custom_command('restore', 'directoryobjects_directory_object_restore')
        g.custom_command('validate-property', 'directoryobjects_directory_object_validate_property')

    with self.command_group('directoryobjects_beta', is_experimental=True):
        pass
