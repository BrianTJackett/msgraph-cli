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

from azure.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_personalcontacts_beta.generated._client_factory import cf_user
    personalcontacts_beta_user = CliCommandType(
        operations_tmpl='azext_personalcontacts_beta.vendored_sdks.personalcontacts.operations._users_operations#UsersO'
        'perations.{}',
        client_factory=cf_user)
    with self.command_group('personalcontacts user', personalcontacts_beta_user, client_factory=cf_user) as g:
        g.custom_command('delete', 'personalcontacts_user_delete', confirmation=True)
        g.custom_command('create-contact', 'personalcontacts_user_create_contact')
        g.custom_command('create-contact-folder', 'personalcontacts_user_create_contact_folder')
        g.custom_command('list-contact', 'personalcontacts_user_list_contact')
        g.custom_command('list-contact-folder', 'personalcontacts_user_list_contact_folder')
        g.custom_command('show-contact', 'personalcontacts_user_show_contact')
        g.custom_command('show-contact-folder', 'personalcontacts_user_show_contact_folder')
        g.custom_command('update-contact', 'personalcontacts_user_update_contact')
        g.custom_command('update-contact-folder', 'personalcontacts_user_update_contact_folder')

    from azext_personalcontacts_beta.generated._client_factory import cf_user_contact_folder
    personalcontacts_beta_user_contact_folder = CliCommandType(
        operations_tmpl='azext_personalcontacts_beta.vendored_sdks.personalcontacts.operations._users_contact_folders_o'
        'perations#UsersContactFoldersOperations.{}',
        client_factory=cf_user_contact_folder)
    with self.command_group('personalcontacts user-contact-folder', personalcontacts_beta_user_contact_folder,
                            client_factory=cf_user_contact_folder) as g:
        g.custom_command('delete', 'personalcontacts_user_contact_folder_delete', confirmation=True)
        g.custom_command('create-child-folder', 'personalcontacts_user_contact_folder_create_child_folder')
        g.custom_command('create-contact', 'personalcontacts_user_contact_folder_create_contact')
        g.custom_command('create-multi-value-extended-property', 'personalcontacts_user_contact_folder_create_multi_val'
                         'ue_extended_property')
        g.custom_command('create-single-value-extended-property', 'personalcontacts_user_contact_folder_create_single_v'
                         'alue_extended_property')
        g.custom_command('list-child-folder', 'personalcontacts_user_contact_folder_list_child_folder')
        g.custom_command('list-contact', 'personalcontacts_user_contact_folder_list_contact')
        g.custom_command('list-multi-value-extended-property', 'personalcontacts_user_contact_folder_list_multi_value_e'
                         'xtended_property')
        g.custom_command('list-single-value-extended-property', 'personalcontacts_user_contact_folder_list_single_value'
                         '_extended_property')
        g.custom_command('show-child-folder', 'personalcontacts_user_contact_folder_show_child_folder')
        g.custom_command('show-contact', 'personalcontacts_user_contact_folder_show_contact')
        g.custom_command('show-multi-value-extended-property', 'personalcontacts_user_contact_folder_show_multi_value_e'
                         'xtended_property')
        g.custom_command('show-single-value-extended-property', 'personalcontacts_user_contact_folder_show_single_value'
                         '_extended_property')
        g.custom_command('update-child-folder', 'personalcontacts_user_contact_folder_update_child_folder')
        g.custom_command('update-contact', 'personalcontacts_user_contact_folder_update_contact')
        g.custom_command('update-multi-value-extended-property', 'personalcontacts_user_contact_folder_update_multi_val'
                         'ue_extended_property')
        g.custom_command('update-single-value-extended-property', 'personalcontacts_user_contact_folder_update_single_v'
                         'alue_extended_property')

    from azext_personalcontacts_beta.generated._client_factory import cf_user_contact_folder_contact
    personalcontacts_beta_user_contact_folder_contact = CliCommandType(
        operations_tmpl='azext_personalcontacts_beta.vendored_sdks.personalcontacts.operations._users_contact_folders_c'
        'ontacts_operations#UsersContactFoldersContactsOperations.{}',
        client_factory=cf_user_contact_folder_contact)
    with self.command_group('personalcontacts user-contact-folder-contact',
                            personalcontacts_beta_user_contact_folder_contact,
                            client_factory=cf_user_contact_folder_contact) as g:
        g.custom_command('delete', 'personalcontacts_user_contact_folder_contact_delete', confirmation=True)
        g.custom_command('create-extension', 'personalcontacts_user_contact_folder_contact_create_extension')
        g.custom_command('create-multi-value-extended-property', 'personalcontacts_user_contact_folder_contact_create_m'
                         'ulti_value_extended_property')
        g.custom_command('create-single-value-extended-property', 'personalcontacts_user_contact_folder_contact_create_'
                         'single_value_extended_property')
        g.custom_command('list-extension', 'personalcontacts_user_contact_folder_contact_list_extension')
        g.custom_command('list-multi-value-extended-property', 'personalcontacts_user_contact_folder_contact_list_multi'
                         '_value_extended_property')
        g.custom_command('list-single-value-extended-property', 'personalcontacts_user_contact_folder_contact_list_sing'
                         'le_value_extended_property')
        g.custom_command('set-photo-content', 'personalcontacts_user_contact_folder_contact_set_photo_content')
        g.custom_command('show-extension', 'personalcontacts_user_contact_folder_contact_show_extension')
        g.custom_command('show-multi-value-extended-property', 'personalcontacts_user_contact_folder_contact_show_multi'
                         '_value_extended_property')
        g.custom_command('show-photo', 'personalcontacts_user_contact_folder_contact_show_photo')
        g.custom_command('show-photo-content', 'personalcontacts_user_contact_folder_contact_show_photo_content')
        g.custom_command('show-single-value-extended-property', 'personalcontacts_user_contact_folder_contact_show_sing'
                         'le_value_extended_property')
        g.custom_command('update-extension', 'personalcontacts_user_contact_folder_contact_update_extension')
        g.custom_command('update-multi-value-extended-property', 'personalcontacts_user_contact_folder_contact_update_m'
                         'ulti_value_extended_property')
        g.custom_command('update-photo', 'personalcontacts_user_contact_folder_contact_update_photo')
        g.custom_command('update-single-value-extended-property', 'personalcontacts_user_contact_folder_contact_update_'
                         'single_value_extended_property')

    from azext_personalcontacts_beta.generated._client_factory import cf_user_contact
    personalcontacts_beta_user_contact = CliCommandType(
        operations_tmpl='azext_personalcontacts_beta.vendored_sdks.personalcontacts.operations._users_contacts_operatio'
        'ns#UsersContactsOperations.{}',
        client_factory=cf_user_contact)
    with self.command_group('personalcontacts user-contact', personalcontacts_beta_user_contact,
                            client_factory=cf_user_contact) as g:
        g.custom_command('delete', 'personalcontacts_user_contact_delete', confirmation=True)
        g.custom_command('create-extension', 'personalcontacts_user_contact_create_extension')
        g.custom_command('create-multi-value-extended-property', 'personalcontacts_user_contact_create_multi_value_exte'
                         'nded_property')
        g.custom_command('create-single-value-extended-property', 'personalcontacts_user_contact_create_single_value_ex'
                         'tended_property')
        g.custom_command('list-extension', 'personalcontacts_user_contact_list_extension')
        g.custom_command('list-multi-value-extended-property', 'personalcontacts_user_contact_list_multi_value_extended'
                         '_property')
        g.custom_command('list-single-value-extended-property', 'personalcontacts_user_contact_list_single_value_extend'
                         'ed_property')
        g.custom_command('set-photo-content', 'personalcontacts_user_contact_set_photo_content')
        g.custom_command('show-extension', 'personalcontacts_user_contact_show_extension')
        g.custom_command('show-multi-value-extended-property', 'personalcontacts_user_contact_show_multi_value_extended'
                         '_property')
        g.custom_command('show-photo', 'personalcontacts_user_contact_show_photo')
        g.custom_command('show-photo-content', 'personalcontacts_user_contact_show_photo_content')
        g.custom_command('show-single-value-extended-property', 'personalcontacts_user_contact_show_single_value_extend'
                         'ed_property')
        g.custom_command('update-extension', 'personalcontacts_user_contact_update_extension')
        g.custom_command('update-multi-value-extended-property', 'personalcontacts_user_contact_update_multi_value_exte'
                         'nded_property')
        g.custom_command('update-photo', 'personalcontacts_user_contact_update_photo')
        g.custom_command('update-single-value-extended-property', 'personalcontacts_user_contact_update_single_value_ex'
                         'tended_property')

    with self.command_group('personalcontacts_beta', is_experimental=True):
        pass
