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

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_places.generated._client_factory import cf_place_place
    places_place_place = CliCommandType(
        operations_tmpl='azext_places.vendored_sdks.places.operations._place_place_operations#PlaceOperations.{}',
        client_factory=cf_place_place)
    with self.command_group('places', places_place_place, client_factory=cf_place_place) as g:
        g.custom_command('update', 'places_update')
        g.custom_command('delete', 'places_delete')
        g.custom_command('create-place', 'places_create_place')
        g.custom_command('get-place', 'places_get_place')
        g.custom_command('list-place', 'places_list_place')
