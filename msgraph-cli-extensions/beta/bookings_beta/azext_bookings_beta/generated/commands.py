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
# pylint: disable=line-too-long

from msgraph.cli.core.commands import CliCommandType


def load_command_table(self, _):

    from azext_bookings_beta.generated._client_factory import cf_booking_business_booking_business

    bookings_beta_booking_business_booking_business = CliCommandType(
        operations_tmpl='azext_bookings_beta.vendored_sdks.bookings.operations._booking_business_booking_business_operations#BookingBusinessBookingBusinessOperations.{}',
        client_factory=cf_booking_business_booking_business,
    )
    with self.command_group(
        'bookings booking-business-booking-business',
        bookings_beta_booking_business_booking_business,
        client_factory=cf_booking_business_booking_business,
    ) as g:
        g.custom_command('delete', 'bookings_booking_business_booking_business_delete', confirmation=True)
        g.custom_command(
            'create-booking-business', 'bookings_booking_business_booking_business_create_booking_business'
        )
        g.custom_command('list-booking-business', 'bookings_booking_business_booking_business_list_booking_business')
        g.custom_command('show-booking-business', 'bookings_booking_business_booking_business_show_booking_business')
        g.custom_command(
            'update-booking-business', 'bookings_booking_business_booking_business_update_booking_business'
        )

    from azext_bookings_beta.generated._client_factory import cf_booking_business

    bookings_beta_booking_business = CliCommandType(
        operations_tmpl='azext_bookings_beta.vendored_sdks.bookings.operations._booking_business_operations#BookingBusinessOperations.{}',
        client_factory=cf_booking_business,
    )
    with self.command_group(
        'bookings booking-business', bookings_beta_booking_business, client_factory=cf_booking_business
    ) as g:
        g.custom_command('delete', 'bookings_booking_business_delete', confirmation=True)
        g.custom_command('create-appointment', 'bookings_booking_business_create_appointment')
        g.custom_command('create-calendar-view', 'bookings_booking_business_create_calendar_view')
        g.custom_command('create-customer', 'bookings_booking_business_create_customer')
        g.custom_command('create-service', 'bookings_booking_business_create_service')
        g.custom_command('create-staff-member', 'bookings_booking_business_create_staff_member')
        g.custom_command('list-appointment', 'bookings_booking_business_list_appointment')
        g.custom_command('list-calendar-view', 'bookings_booking_business_list_calendar_view')
        g.custom_command('list-customer', 'bookings_booking_business_list_customer')
        g.custom_command('list-service', 'bookings_booking_business_list_service')
        g.custom_command('list-staff-member', 'bookings_booking_business_list_staff_member')
        g.custom_command('publish', 'bookings_booking_business_publish')
        g.custom_command('show-appointment', 'bookings_booking_business_show_appointment')
        g.custom_command('show-calendar-view', 'bookings_booking_business_show_calendar_view')
        g.custom_command('show-customer', 'bookings_booking_business_show_customer')
        g.custom_command('show-service', 'bookings_booking_business_show_service')
        g.custom_command('show-staff-member', 'bookings_booking_business_show_staff_member')
        g.custom_command('unpublish', 'bookings_booking_business_unpublish')
        g.custom_command('update-appointment', 'bookings_booking_business_update_appointment')
        g.custom_command('update-calendar-view', 'bookings_booking_business_update_calendar_view')
        g.custom_command('update-customer', 'bookings_booking_business_update_customer')
        g.custom_command('update-service', 'bookings_booking_business_update_service')
        g.custom_command('update-staff-member', 'bookings_booking_business_update_staff_member')

    from azext_bookings_beta.generated._client_factory import cf_booking_business_appointment

    bookings_beta_booking_business_appointment = CliCommandType(
        operations_tmpl='azext_bookings_beta.vendored_sdks.bookings.operations._booking_business_appointment_operations#BookingBusinessAppointmentOperations.{}',
        client_factory=cf_booking_business_appointment,
    )
    with self.command_group(
        'bookings booking-business-appointment',
        bookings_beta_booking_business_appointment,
        client_factory=cf_booking_business_appointment,
    ) as g:
        g.custom_command('cancel', 'bookings_booking_business_appointment_cancel')

    from azext_bookings_beta.generated._client_factory import cf_booking_business_calendar_view

    bookings_beta_booking_business_calendar_view = CliCommandType(
        operations_tmpl='azext_bookings_beta.vendored_sdks.bookings.operations._booking_business_calendar_view_operations#BookingBusinessCalendarViewOperations.{}',
        client_factory=cf_booking_business_calendar_view,
    )
    with self.command_group(
        'bookings booking-business-calendar-view',
        bookings_beta_booking_business_calendar_view,
        client_factory=cf_booking_business_calendar_view,
    ) as g:
        g.custom_command('cancel', 'bookings_booking_business_calendar_view_cancel')

    from azext_bookings_beta.generated._client_factory import cf_booking_currency_booking_currency

    bookings_beta_booking_currency_booking_currency = CliCommandType(
        operations_tmpl='azext_bookings_beta.vendored_sdks.bookings.operations._booking_currency_booking_currency_operations#BookingCurrencyBookingCurrencyOperations.{}',
        client_factory=cf_booking_currency_booking_currency,
    )
    with self.command_group(
        'bookings booking-currency-booking-currency',
        bookings_beta_booking_currency_booking_currency,
        client_factory=cf_booking_currency_booking_currency,
    ) as g:
        g.custom_command('delete', 'bookings_booking_currency_booking_currency_delete', confirmation=True)
        g.custom_command(
            'create-booking-currency', 'bookings_booking_currency_booking_currency_create_booking_currency'
        )
        g.custom_command('list-booking-currency', 'bookings_booking_currency_booking_currency_list_booking_currency')
        g.custom_command('show-booking-currency', 'bookings_booking_currency_booking_currency_show_booking_currency')
        g.custom_command(
            'update-booking-currency', 'bookings_booking_currency_booking_currency_update_booking_currency'
        )

    with self.command_group('bookings_beta', is_experimental=True):
        pass
