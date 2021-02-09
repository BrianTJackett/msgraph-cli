# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long
# pylint: disable=too-many-lines
# pylint: disable=too-many-statements

from azure.cli.core.commands.parameters import (
    get_three_state_flag,
    get_enum_type
)


def load_arguments(self, _):

    with self.argument_context('usersfunctions user-activity recent') as c:
        c.argument('user_id', type=str, help='key: id of user')

    with self.argument_context('usersfunctions user-calendar-calendar-view-calendar allowed-calendar-sharing-role') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('event_id', type=str, help='key: id of event')
        c.argument('user', type=str, help='')

    with self.argument_context('usersfunctions user-calendar-calendar-view-instance delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('event_id', type=str, help='key: id of event')

    with self.argument_context('usersfunctions user-calendar-calendar-view delta') as c:
        c.argument('user_id', type=str, help='key: id of user')

    with self.argument_context('usersfunctions user-calendar-event-calendar allowed-calendar-sharing-role') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('event_id', type=str, help='key: id of event')
        c.argument('user', type=str, help='')

    with self.argument_context('usersfunctions user-calendar-event-instance delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('event_id', type=str, help='key: id of event')

    with self.argument_context('usersfunctions user-calendar-event delta') as c:
        c.argument('user_id', type=str, help='key: id of user')

    with self.argument_context('usersfunctions user-calendar allowed-calendar-sharing-role') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('user', type=str, help='')

    with self.argument_context('usersfunctions user-calendar-group-calendar-calendar-view-calendar allowed-calendar-sharing-role') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('calendar_group_id', type=str, help='key: id of calendarGroup')
        c.argument('calendar_id', type=str, help='key: id of calendar')
        c.argument('event_id', type=str, help='key: id of event')
        c.argument('user', type=str, help='')

    with self.argument_context('usersfunctions user-calendar-group-calendar-calendar-view-instance delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('calendar_group_id', type=str, help='key: id of calendarGroup')
        c.argument('calendar_id', type=str, help='key: id of calendar')
        c.argument('event_id', type=str, help='key: id of event')

    with self.argument_context('usersfunctions user-calendar-group-calendar-calendar-view delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('calendar_group_id', type=str, help='key: id of calendarGroup')
        c.argument('calendar_id', type=str, help='key: id of calendar')

    with self.argument_context('usersfunctions user-calendar-group-calendar-event-calendar allowed-calendar-sharing-role') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('calendar_group_id', type=str, help='key: id of calendarGroup')
        c.argument('calendar_id', type=str, help='key: id of calendar')
        c.argument('event_id', type=str, help='key: id of event')
        c.argument('user', type=str, help='')

    with self.argument_context('usersfunctions user-calendar-group-calendar-event-instance delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('calendar_group_id', type=str, help='key: id of calendarGroup')
        c.argument('calendar_id', type=str, help='key: id of calendar')
        c.argument('event_id', type=str, help='key: id of event')

    with self.argument_context('usersfunctions user-calendar-group-calendar-event delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('calendar_group_id', type=str, help='key: id of calendarGroup')
        c.argument('calendar_id', type=str, help='key: id of calendar')

    with self.argument_context('usersfunctions user-calendar-group-calendar allowed-calendar-sharing-role') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('calendar_group_id', type=str, help='key: id of calendarGroup')
        c.argument('calendar_id', type=str, help='key: id of calendar')
        c.argument('user', type=str, help='')

    with self.argument_context('usersfunctions user-calendar-calendar-view-calendar allowed-calendar-sharing-role') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('calendar_id', type=str, help='key: id of calendar')
        c.argument('event_id', type=str, help='key: id of event')
        c.argument('user', type=str, help='')

    with self.argument_context('usersfunctions user-calendar-calendar-view-instance delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('calendar_id', type=str, help='key: id of calendar')
        c.argument('event_id', type=str, help='key: id of event')

    with self.argument_context('usersfunctions user-calendar-calendar-view delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('calendar_id', type=str, help='key: id of calendar')

    with self.argument_context('usersfunctions user-calendar-event-calendar allowed-calendar-sharing-role') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('calendar_id', type=str, help='key: id of calendar')
        c.argument('event_id', type=str, help='key: id of event')
        c.argument('user', type=str, help='')

    with self.argument_context('usersfunctions user-calendar-event-instance delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('calendar_id', type=str, help='key: id of calendar')
        c.argument('event_id', type=str, help='key: id of event')

    with self.argument_context('usersfunctions user-calendar-event delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('calendar_id', type=str, help='key: id of calendar')

    with self.argument_context('usersfunctions user-calendar allowed-calendar-sharing-role') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('calendar_id', type=str, help='key: id of calendar')
        c.argument('user', type=str, help='')

    with self.argument_context('usersfunctions user-calendar-view-calendar-calendar-view delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('event_id', type=str, help='key: id of event')

    with self.argument_context('usersfunctions user-calendar-view-calendar-event delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('event_id', type=str, help='key: id of event')

    with self.argument_context('usersfunctions user-calendar-view-calendar allowed-calendar-sharing-role') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('event_id', type=str, help='key: id of event')
        c.argument('user', type=str, help='')

    with self.argument_context('usersfunctions user-calendar-view-instance delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('event_id', type=str, help='key: id of event')

    with self.argument_context('usersfunctions user-calendar-view delta') as c:
        c.argument('user_id', type=str, help='key: id of user')

    with self.argument_context('usersfunctions user-contact-folder-child-folder delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('contact_folder_id', type=str, help='key: id of contactFolder')

    with self.argument_context('usersfunctions user-contact-folder-contact delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('contact_folder_id', type=str, help='key: id of contactFolder')

    with self.argument_context('usersfunctions user-contact-folder delta') as c:
        c.argument('user_id', type=str, help='key: id of user')

    with self.argument_context('usersfunctions user-contact delta') as c:
        c.argument('user_id', type=str, help='key: id of user')

    with self.argument_context('usersfunctions user-event-calendar-calendar-view delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('event_id', type=str, help='key: id of event')

    with self.argument_context('usersfunctions user-event-calendar-event delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('event_id', type=str, help='key: id of event')

    with self.argument_context('usersfunctions user-event-calendar allowed-calendar-sharing-role') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('event_id', type=str, help='key: id of event')
        c.argument('user', type=str, help='')

    with self.argument_context('usersfunctions user-event-instance delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('event_id', type=str, help='key: id of event')

    with self.argument_context('usersfunctions user-event delta') as c:
        c.argument('user_id', type=str, help='key: id of user')

    with self.argument_context('usersfunctions user-mail-folder-child-folder delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('mail_folder_id', type=str, help='key: id of mailFolder')

    with self.argument_context('usersfunctions user-mail-folder-message delta') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('mail_folder_id', type=str, help='key: id of mailFolder')

    with self.argument_context('usersfunctions user-mail-folder delta') as c:
        c.argument('user_id', type=str, help='key: id of user')

    with self.argument_context('usersfunctions user-managed-app-registration show-user-id-with-flagged-app-registration') as c:
        c.argument('user_id', type=str, help='key: id of user')

    with self.argument_context('usersfunctions user-message delta') as c:
        c.argument('user_id', type=str, help='key: id of user')

    with self.argument_context('usersfunctions user reminder-view') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('start_date_time', type=str, help='')
        c.argument('end_date_time', type=str, help='')

    with self.argument_context('usersfunctions user show-managed-app-diagnostic-statuses') as c:
        c.argument('user_id', type=str, help='key: id of user')

    with self.argument_context('usersfunctions user show-managed-app-policy') as c:
        c.argument('user_id', type=str, help='key: id of user')

    with self.argument_context('usersfunctions user-onenote-notebook-section-group-section-page preview') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('notebook_id', type=str, help='key: id of notebook')
        c.argument('section_group_id', type=str, help='key: id of sectionGroup')
        c.argument('onenote_section_id', type=str, help='key: id of onenoteSection')
        c.argument('onenote_page_id', type=str, help='key: id of onenotePage')

    with self.argument_context('usersfunctions user-onenote-notebook-section-page preview') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('notebook_id', type=str, help='key: id of notebook')
        c.argument('onenote_section_id', type=str, help='key: id of onenoteSection')
        c.argument('onenote_page_id', type=str, help='key: id of onenotePage')

    with self.argument_context('usersfunctions user-onenote-notebook show-recent-notebook') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('include_personal_notebooks', arg_type=get_three_state_flag(), help='')

    with self.argument_context('usersfunctions user-onenote-page preview') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('onenote_page_id', type=str, help='key: id of onenotePage')

    with self.argument_context('usersfunctions user-onenote-page-parent-notebook-section-group-section-page preview') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('onenote_page_id', type=str, help='key: id of onenotePage')
        c.argument('section_group_id', type=str, help='key: id of sectionGroup')
        c.argument('onenote_section_id', type=str, help='key: id of onenoteSection')
        c.argument('onenote_page_id1', type=str, help='key: id of onenotePage')

    with self.argument_context('usersfunctions user-onenote-page-parent-notebook-section-page preview') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('onenote_page_id', type=str, help='key: id of onenotePage')
        c.argument('onenote_section_id', type=str, help='key: id of onenoteSection')
        c.argument('onenote_page_id1', type=str, help='key: id of onenotePage')

    with self.argument_context('usersfunctions user-onenote-page-parent-section-page preview') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('onenote_page_id', type=str, help='key: id of onenotePage')
        c.argument('onenote_page_id1', type=str, help='key: id of onenotePage')

    with self.argument_context('usersfunctions user-onenote-section-group-parent-notebook-section-page preview') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('section_group_id', type=str, help='key: id of sectionGroup')
        c.argument('onenote_section_id', type=str, help='key: id of onenoteSection')
        c.argument('onenote_page_id', type=str, help='key: id of onenotePage')

    with self.argument_context('usersfunctions user-onenote-section-group-section-page preview') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('section_group_id', type=str, help='key: id of sectionGroup')
        c.argument('onenote_section_id', type=str, help='key: id of onenoteSection')
        c.argument('onenote_page_id', type=str, help='key: id of onenotePage')

    with self.argument_context('usersfunctions user-onenote-section-page preview') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('onenote_section_id', type=str, help='key: id of onenoteSection')
        c.argument('onenote_page_id', type=str, help='key: id of onenotePage')

    with self.argument_context('usersfunctions user-outlook supported-language') as c:
        c.argument('user_id', type=str, help='key: id of user')

    with self.argument_context('usersfunctions user-outlook supported-time-zone-ee48') as c:
        c.argument('user_id', type=str, help='key: id of user')

    with self.argument_context('usersfunctions user-outlook supported-time-zones51-c6') as c:
        c.argument('user_id', type=str, help='key: id of user')
        c.argument('time_zone_standard', arg_type=get_enum_type(['windows', 'iana']), help='')
