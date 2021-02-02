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
            elif kl == 'app-display-name':
                d['app_display_name'] = v[0]
            elif kl == 'app-id':
                d['app_id'] = v[0]
            elif kl == 'applied-conditional-access-policies':
                d['applied_conditional_access_policies'] = v
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
            elif kl == 'resource-display-name':
                d['resource_display_name'] = v[0]
            elif kl == 'resource-id':
                d['resource_id'] = v[0]
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
            elif kl == 'status':
                d['status'] = v[0]
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
            if kl == 'display-name':
                d['display_name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
            elif kl == 'ip-address':
                d['ip_address'] = v[0]
            elif kl == 'user-principal-name':
                d['user_principal_name'] = v[0]
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
            if kl == 'display-name':
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
