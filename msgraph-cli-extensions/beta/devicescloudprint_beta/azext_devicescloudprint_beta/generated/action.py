# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=protected-access

import argparse
from collections import defaultdict
from knack.util import CLIError


class AddOperations(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddOperations, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'created-date-time':
                d['created_date_time'] = v[0]
            elif kl == 'description':
                d['description'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddServices(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddServices, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'endpoints':
                d['endpoints'] = v
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddLocation(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.location = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'altitude-in-meters':
                d['altitude_in_meters'] = v[0]
            elif kl == 'building':
                d['building'] = v[0]
            elif kl == 'city':
                d['city'] = v[0]
            elif kl == 'country-or-region':
                d['country_or_region'] = v[0]
            elif kl == 'floor-description':
                d['floor_description'] = v[0]
            elif kl == 'floor-number':
                d['floor_number'] = v[0]
            elif kl == 'latitude':
                d['latitude'] = v[0]
            elif kl == 'longitude':
                d['longitude'] = v[0]
            elif kl == 'organization':
                d['organization'] = v
            elif kl == 'postal-code':
                d['postal_code'] = v[0]
            elif kl == 'room-description':
                d['room_description'] = v[0]
            elif kl == 'room-number':
                d['room_number'] = v[0]
            elif kl == 'site':
                d['site'] = v[0]
            elif kl == 'state-or-province':
                d['state_or_province'] = v[0]
            elif kl == 'street-address':
                d['street_address'] = v[0]
            elif kl == 'subdivision':
                d['subdivision'] = v
            elif kl == 'subunit':
                d['subunit'] = v
        return d


class AddDefaults(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.defaults = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'color-mode':
                d['color_mode'] = v[0]
            elif kl == 'content-type':
                d['content_type'] = v[0]
            elif kl == 'copies-per-job':
                d['copies_per_job'] = v[0]
            elif kl == 'document-mime-type':
                d['document_mime_type'] = v[0]
            elif kl == 'dpi':
                d['dpi'] = v[0]
            elif kl == 'duplex-configuration':
                d['duplex_configuration'] = v[0]
            elif kl == 'duplex-mode':
                d['duplex_mode'] = v[0]
            elif kl == 'finishings':
                d['finishings'] = v
            elif kl == 'fit-pdf-to-page':
                d['fit_pdf_to_page'] = v[0]
            elif kl == 'media-color':
                d['media_color'] = v[0]
            elif kl == 'media-size':
                d['media_size'] = v[0]
            elif kl == 'media-type':
                d['media_type'] = v[0]
            elif kl == 'multipage-layout':
                d['multipage_layout'] = v[0]
            elif kl == 'orientation':
                d['orientation'] = v[0]
            elif kl == 'output-bin':
                d['output_bin'] = v[0]
            elif kl == 'pages-per-sheet':
                d['pages_per_sheet'] = v[0]
            elif kl == 'pdf-fit-to-page':
                d['pdf_fit_to_page'] = v[0]
            elif kl == 'presentation-direction':
                d['presentation_direction'] = v[0]
            elif kl == 'print-color-configuration':
                d['print_color_configuration'] = v[0]
            elif kl == 'print-quality':
                d['print_quality'] = v[0]
            elif kl == 'quality':
                d['quality'] = v[0]
            elif kl == 'scaling':
                d['scaling'] = v[0]
        return d


class AddPrintStatus(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.status = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'description':
                d['description'] = v[0]
            elif kl == 'details':
                d['details'] = v
            elif kl == 'processing-state':
                d['processing_state'] = v[0]
            elif kl == 'processing-state-description':
                d['processing_state_description'] = v[0]
            elif kl == 'processing-state-reasons':
                d['processing_state_reasons'] = v
            elif kl == 'state':
                d['state'] = v[0]
        return d


class AddCapabilitiesCopiesPerJob(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.capabilities_copies_per_job = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'end':
                d['end'] = v[0]
            elif kl == 'maximum':
                d['maximum'] = v[0]
            elif kl == 'minimum':
                d['minimum'] = v[0]
            elif kl == 'start':
                d['start'] = v[0]
        return d


class AddDevicescloudprintCreatePrinterAllowedGroups(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDevicescloudprintCreatePrinterAllowedGroups, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddDevicescloudprintCreatePrinterAllowedUsers(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDevicescloudprintCreatePrinterAllowedUsers, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'ip-address':
                d['ip_address'] = v[0]
            elif kl == 'user-principal-name':
                d['user_principal_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddDevicescloudprintCreatePrinterShareAllowedGroups(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDevicescloudprintCreatePrinterShareAllowedGroups, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddDevicescloudprintCreatePrinterShareAllowedUsers(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDevicescloudprintCreatePrinterShareAllowedUsers, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'ip-address':
                d['ip_address'] = v[0]
            elif kl == 'user-principal-name':
                d['user_principal_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddApplicationSignInDetailedSummary(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddApplicationSignInDetailedSummary, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'aggregated-event-date-time':
                d['aggregated_event_date_time'] = v[0]
            elif kl == 'app-display-name':
                d['app_display_name'] = v[0]
            elif kl == 'app-id':
                d['app_id'] = v[0]
            elif kl == 'sign-in-count':
                d['sign_in_count'] = v[0]
            elif kl == 'additional-details':
                d['additional_details'] = v[0]
            elif kl == 'error-code':
                d['error_code'] = v[0]
            elif kl == 'failure-reason':
                d['failure_reason'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddCredentialUserRegistrationDetails(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddCredentialUserRegistrationDetails, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'auth-methods':
                d['auth_methods'] = v
            elif kl == 'is-capable':
                d['is_capable'] = v[0]
            elif kl == 'is-enabled':
                d['is_enabled'] = v[0]
            elif kl == 'is-mfa-registered':
                d['is_mfa_registered'] = v[0]
            elif kl == 'is-registered':
                d['is_registered'] = v[0]
            elif kl == 'user-display-name':
                d['user_display_name'] = v[0]
            elif kl == 'user-principal-name':
                d['user_principal_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddUserCredentialUsageDetails(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddUserCredentialUsageDetails, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'auth-method':
                d['auth_method'] = v[0]
            elif kl == 'event-date-time':
                d['event_date_time'] = v[0]
            elif kl == 'failure-reason':
                d['failure_reason'] = v[0]
            elif kl == 'feature':
                d['feature'] = v[0]
            elif kl == 'is-success':
                d['is_success'] = v[0]
            elif kl == 'user-display-name':
                d['user_display_name'] = v[0]
            elif kl == 'user-principal-name':
                d['user_principal_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddDailyPrintUsageSummariesByPrinter(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDailyPrintUsageSummariesByPrinter, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'completed-black-and-white-job-count':
                d['completed_black_and_white_job_count'] = v[0]
            elif kl == 'completed-color-job-count':
                d['completed_color_job_count'] = v[0]
            elif kl == 'incomplete-job-count':
                d['incomplete_job_count'] = v[0]
            elif kl == 'printer-id':
                d['printer_id'] = v[0]
            elif kl == 'usage-date':
                d['usage_date'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddDailyPrintUsageSummariesByUser(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddDailyPrintUsageSummariesByUser, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'completed-black-and-white-job-count':
                d['completed_black_and_white_job_count'] = v[0]
            elif kl == 'completed-color-job-count':
                d['completed_color_job_count'] = v[0]
            elif kl == 'incomplete-job-count':
                d['incomplete_job_count'] = v[0]
            elif kl == 'usage-date':
                d['usage_date'] = v[0]
            elif kl == 'user-principal-name':
                d['user_principal_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddMonthlyPrintUsageSummariesByPrinter(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddMonthlyPrintUsageSummariesByPrinter, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'completed-black-and-white-job-count':
                d['completed_black_and_white_job_count'] = v[0]
            elif kl == 'completed-color-job-count':
                d['completed_color_job_count'] = v[0]
            elif kl == 'incomplete-job-count':
                d['incomplete_job_count'] = v[0]
            elif kl == 'printer-id':
                d['printer_id'] = v[0]
            elif kl == 'usage-date':
                d['usage_date'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddMonthlyPrintUsageSummariesByUser(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddMonthlyPrintUsageSummariesByUser, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'completed-black-and-white-job-count':
                d['completed_black_and_white_job_count'] = v[0]
            elif kl == 'completed-color-job-count':
                d['completed_color_job_count'] = v[0]
            elif kl == 'incomplete-job-count':
                d['incomplete_job_count'] = v[0]
            elif kl == 'usage-date':
                d['usage_date'] = v[0]
            elif kl == 'user-principal-name':
                d['user_principal_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddEndpoints(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddEndpoints, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'uri':
                d['uri'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddCreatedBy(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.created_by = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'app-id':
                d['app_id'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'service-principal-id':
                d['service_principal_id'] = v[0]
            elif kl == 'service-principal-name':
                d['service_principal_name'] = v[0]
        return d


class AddCertificateSigningRequest(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.certificate_signing_request = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'content':
                d['content'] = v[0]
            elif kl == 'transport-key':
                d['transport_key'] = v[0]
        return d


class AddPrintTaskdefinitionsStatus(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.status = action

    def get_action(self, values, option_string):  # pylint: disable=no-self-use
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]
            if kl == 'description':
                d['description'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
        return d
