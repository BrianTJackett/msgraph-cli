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


class AddRestrictedSignIns(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddRestrictedSignIns, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'target-tenant-id':
                d['target_tenant_id'] = v[0]
            elif kl == 'alternate-sign-in-name':
                d['alternate_sign_in_name'] = v[0]
            elif kl == 'app-display-name':
                d['app_display_name'] = v[0]
            elif kl == 'app-id':
                d['app_id'] = v[0]
            elif kl == 'applied-conditional-access-policies':
                d['applied_conditional_access_policies'] = v
            elif kl == 'authentication-details':
                d['authentication_details'] = v
            elif kl == 'authentication-methods-used':
                d['authentication_methods_used'] = v
            elif kl == 'authentication-processing-details':
                d['authentication_processing_details'] = v
            elif kl == 'authentication-requirement':
                d['authentication_requirement'] = v[0]
            elif kl == 'authentication-requirement-policies':
                d['authentication_requirement_policies'] = v
            elif kl == 'client-app-used':
                d['client_app_used'] = v[0]
            elif kl == 'conditional-access-status':
                d['conditional_access_status'] = v[0]
            elif kl == 'correlation-id':
                d['correlation_id'] = v[0]
            elif kl == 'created-date-time':
                d['created_date_time'] = v[0]
            elif kl == 'device-detail':
                d['device_detail'] = v[0]
            elif kl == 'ip-address':
                d['ip_address'] = v[0]
            elif kl == 'is-interactive':
                d['is_interactive'] = v[0]
            elif kl == 'mfa-detail':
                d['mfa_detail'] = v[0]
            elif kl == 'network-location-details':
                d['network_location_details'] = v
            elif kl == 'original-request-id':
                d['original_request_id'] = v[0]
            elif kl == 'processing-time-in-milliseconds':
                d['processing_time_in_milliseconds'] = v[0]
            elif kl == 'resource-display-name':
                d['resource_display_name'] = v[0]
            elif kl == 'resource-id':
                d['resource_id'] = v[0]
            elif kl == 'resource-tenant-id':
                d['resource_tenant_id'] = v[0]
            elif kl == 'risk-detail':
                d['risk_detail'] = v[0]
            elif kl == 'risk-event-types':
                d['risk_event_types'] = v
            elif kl == 'risk-event-types-v2':
                d['risk_event_types_v2'] = v
            elif kl == 'risk-level-aggregated':
                d['risk_level_aggregated'] = v[0]
            elif kl == 'risk-level-during-sign-in':
                d['risk_level_during_sign_in'] = v[0]
            elif kl == 'risk-state':
                d['risk_state'] = v[0]
            elif kl == 'service-principal-id':
                d['service_principal_id'] = v[0]
            elif kl == 'service-principal-name':
                d['service_principal_name'] = v[0]
            elif kl == 'sign-in-event-types':
                d['sign_in_event_types'] = v
            elif kl == 'status':
                d['status'] = v[0]
            elif kl == 'token-issuer-name':
                d['token_issuer_name'] = v[0]
            elif kl == 'token-issuer-type':
                d['token_issuer_type'] = v[0]
            elif kl == 'user-agent':
                d['user_agent'] = v[0]
            elif kl == 'user-display-name':
                d['user_display_name'] = v[0]
            elif kl == 'user-id':
                d['user_id'] = v[0]
            elif kl == 'user-principal-name':
                d['user_principal_name'] = v[0]
            elif kl == 'city':
                d['city'] = v[0]
            elif kl == 'country-or-region':
                d['country_or_region'] = v[0]
            elif kl == 'geo-coordinates':
                d['geo_coordinates'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddAdditionalDetails(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAdditionalDetails, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'key':
                d['key'] = v[0]
            elif kl == 'value':
                d['value'] = v[0]
        return d


class AddTargetResources(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddTargetResources, self).__call__(parser, namespace, action, option_string)

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
            elif kl == 'group-type':
                d['group_type'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            elif kl == 'modified-properties':
                d['modified_properties'] = v
            elif kl == 'type':
                d['type'] = v[0]
            elif kl == 'user-principal-name':
                d['user_principal_name'] = v[0]
        return d


class AddInitiatedByApp(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.initiated_by_app = action

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


class AddInitiatedByUser(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.initiated_by_user = action

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
            if kl == 'ip-address':
                d['ip_address'] = v[0]
            elif kl == 'user-principal-name':
                d['user_principal_name'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddAppliedConditionalAccessPolicies(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAppliedConditionalAccessPolicies, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'conditions-not-satisfied':
                d['conditions_not_satisfied'] = v[0]
            elif kl == 'conditions-satisfied':
                d['conditions_satisfied'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'enforced-grant-controls':
                d['enforced_grant_controls'] = v
            elif kl == 'enforced-session-controls':
                d['enforced_session_controls'] = v
            elif kl == 'id':
                d['id'] = v[0]
            elif kl == 'result':
                d['result'] = v[0]
        return d


class AddAuthenticationDetails(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAuthenticationDetails, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'authentication-method':
                d['authentication_method'] = v[0]
            elif kl == 'authentication-method-detail':
                d['authentication_method_detail'] = v[0]
            elif kl == 'authentication-step-date-time':
                d['authentication_step_date_time'] = v[0]
            elif kl == 'authentication-step-requirement':
                d['authentication_step_requirement'] = v[0]
            elif kl == 'authentication-step-result-detail':
                d['authentication_step_result_detail'] = v[0]
            elif kl == 'succeeded':
                d['succeeded'] = v[0]
        return d


class AddAuthenticationProcessingDetails(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAuthenticationProcessingDetails, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'key':
                d['key'] = v[0]
            elif kl == 'value':
                d['value'] = v[0]
        return d


class AddAuthenticationRequirementPolicies(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAuthenticationRequirementPolicies, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'detail':
                d['detail'] = v[0]
            elif kl == 'requirement-provider':
                d['requirement_provider'] = v[0]
        return d


class AddDeviceDetail(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.device_detail = action

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
            if kl == 'browser':
                d['browser'] = v[0]
            elif kl == 'browser-id':
                d['browser_id'] = v[0]
            elif kl == 'device-id':
                d['device_id'] = v[0]
            elif kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'is-compliant':
                d['is_compliant'] = v[0]
            elif kl == 'is-managed':
                d['is_managed'] = v[0]
            elif kl == 'operating-system':
                d['operating_system'] = v[0]
            elif kl == 'trust-type':
                d['trust_type'] = v[0]
        return d


class AddMfaDetail(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.mfa_detail = action

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
            if kl == 'auth-detail':
                d['auth_detail'] = v[0]
            elif kl == 'auth-method':
                d['auth_method'] = v[0]
        return d


class AddNetworkLocationDetails(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddNetworkLocationDetails, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'network-names':
                d['network_names'] = v
            elif kl == 'network-type':
                d['network_type'] = v[0]
        return d


class AddStatus(argparse.Action):
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
            if kl == 'additional-details':
                d['additional_details'] = v[0]
            elif kl == 'error-code':
                d['error_code'] = v[0]
            elif kl == 'failure-reason':
                d['failure_reason'] = v[0]
        return d


class AddLocationGeoCoordinates(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.location_geo_coordinates = action

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
            if kl == 'altitude':
                d['altitude'] = v[0]
            elif kl == 'latitude':
                d['latitude'] = v[0]
            elif kl == 'longitude':
                d['longitude'] = v[0]
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
