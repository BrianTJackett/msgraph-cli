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


class AddCloudAppStates(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddCloudAppStates, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'destination-service-ip':
                d['destination_service_ip'] = v[0]
            elif kl == 'destination-service-name':
                d['destination_service_name'] = v[0]
            elif kl == 'risk-score':
                d['risk_score'] = v[0]
        return d


class AddFileStates(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddFileStates, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'name':
                d['name'] = v[0]
            elif kl == 'path':
                d['path'] = v[0]
            elif kl == 'risk-score':
                d['risk_score'] = v[0]
            elif kl == 'hash-type':
                d['hash_type'] = v[0]
            elif kl == 'hash-value':
                d['hash_value'] = v[0]
        return d


class AddHistoryStates(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddHistoryStates, self).__call__(parser, namespace, action, option_string)

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
            elif kl == 'assigned-to':
                d['assigned_to'] = v[0]
            elif kl == 'comments':
                d['comments'] = v
            elif kl == 'feedback':
                d['feedback'] = v[0]
            elif kl == 'status':
                d['status'] = v[0]
            elif kl == 'updated-date-time':
                d['updated_date_time'] = v[0]
            elif kl == 'user':
                d['user'] = v[0]
        return d


class AddHostStates(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddHostStates, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'fqdn':
                d['fqdn'] = v[0]
            elif kl == 'is-azure-ad-joined':
                d['is_azure_ad_joined'] = v[0]
            elif kl == 'is-azure-ad-registered':
                d['is_azure_ad_registered'] = v[0]
            elif kl == 'is-hybrid-azure-domain-joined':
                d['is_hybrid_azure_domain_joined'] = v[0]
            elif kl == 'net-bios-name':
                d['net_bios_name'] = v[0]
            elif kl == 'os':
                d['os'] = v[0]
            elif kl == 'private-ip-address':
                d['private_ip_address'] = v[0]
            elif kl == 'public-ip-address':
                d['public_ip_address'] = v[0]
            elif kl == 'risk-score':
                d['risk_score'] = v[0]
        return d


class AddMalwareStates(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddMalwareStates, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'category':
                d['category'] = v[0]
            elif kl == 'family':
                d['family'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
            elif kl == 'severity':
                d['severity'] = v[0]
            elif kl == 'was-running':
                d['was_running'] = v[0]
        return d


class AddNetworkConnections(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddNetworkConnections, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'application-name':
                d['application_name'] = v[0]
            elif kl == 'destination-address':
                d['destination_address'] = v[0]
            elif kl == 'destination-domain':
                d['destination_domain'] = v[0]
            elif kl == 'destination-location':
                d['destination_location'] = v[0]
            elif kl == 'destination-port':
                d['destination_port'] = v[0]
            elif kl == 'destination-url':
                d['destination_url'] = v[0]
            elif kl == 'direction':
                d['direction'] = v[0]
            elif kl == 'domain-registered-date-time':
                d['domain_registered_date_time'] = v[0]
            elif kl == 'local-dns-name':
                d['local_dns_name'] = v[0]
            elif kl == 'nat-destination-address':
                d['nat_destination_address'] = v[0]
            elif kl == 'nat-destination-port':
                d['nat_destination_port'] = v[0]
            elif kl == 'nat-source-address':
                d['nat_source_address'] = v[0]
            elif kl == 'nat-source-port':
                d['nat_source_port'] = v[0]
            elif kl == 'protocol':
                d['protocol'] = v[0]
            elif kl == 'risk-score':
                d['risk_score'] = v[0]
            elif kl == 'source-address':
                d['source_address'] = v[0]
            elif kl == 'source-location':
                d['source_location'] = v[0]
            elif kl == 'source-port':
                d['source_port'] = v[0]
            elif kl == 'status':
                d['status'] = v[0]
            elif kl == 'url-parameters':
                d['url_parameters'] = v[0]
        return d


class AddRegistryKeyStates(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddRegistryKeyStates, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'hive':
                d['hive'] = v[0]
            elif kl == 'key':
                d['key'] = v[0]
            elif kl == 'old-key':
                d['old_key'] = v[0]
            elif kl == 'old-value-data':
                d['old_value_data'] = v[0]
            elif kl == 'old-value-name':
                d['old_value_name'] = v[0]
            elif kl == 'operation':
                d['operation'] = v[0]
            elif kl == 'process-id':
                d['process_id'] = v[0]
            elif kl == 'value-data':
                d['value_data'] = v[0]
            elif kl == 'value-name':
                d['value_name'] = v[0]
            elif kl == 'value-type':
                d['value_type'] = v[0]
        return d


class AddSecurityResources(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddSecurityResources, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'resource':
                d['resource'] = v[0]
            elif kl == 'resource-type':
                d['resource_type'] = v[0]
        return d


class AddTriggers(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddTriggers, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'name':
                d['name'] = v[0]
            elif kl == 'type':
                d['type'] = v[0]
            elif kl == 'value':
                d['value'] = v[0]
        return d


class AddUserStates(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddUserStates, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'aad-user-id':
                d['aad_user_id'] = v[0]
            elif kl == 'account-name':
                d['account_name'] = v[0]
            elif kl == 'domain-name':
                d['domain_name'] = v[0]
            elif kl == 'email-role':
                d['email_role'] = v[0]
            elif kl == 'is-vpn':
                d['is_vpn'] = v[0]
            elif kl == 'logon-date-time':
                d['logon_date_time'] = v[0]
            elif kl == 'logon-id':
                d['logon_id'] = v[0]
            elif kl == 'logon-ip':
                d['logon_ip'] = v[0]
            elif kl == 'logon-location':
                d['logon_location'] = v[0]
            elif kl == 'logon-type':
                d['logon_type'] = v[0]
            elif kl == 'on-premises-security-identifier':
                d['on_premises_security_identifier'] = v[0]
            elif kl == 'risk-score':
                d['risk_score'] = v[0]
            elif kl == 'user-account-type':
                d['user_account_type'] = v[0]
            elif kl == 'user-principal-name':
                d['user_principal_name'] = v[0]
        return d


class AddVendorInformation(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.vendor_information = action

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
            if kl == 'provider':
                d['provider'] = v[0]
            elif kl == 'provider-version':
                d['provider_version'] = v[0]
            elif kl == 'sub-provider':
                d['sub_provider'] = v[0]
            elif kl == 'vendor':
                d['vendor'] = v[0]
        return d


class AddVulnerabilityStates(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddVulnerabilityStates, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'cve':
                d['cve'] = v[0]
            elif kl == 'severity':
                d['severity'] = v[0]
            elif kl == 'was-running':
                d['was_running'] = v[0]
        return d


class AddAverageComparativeScores(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAverageComparativeScores, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'average-score':
                d['average_score'] = v[0]
            elif kl == 'basis':
                d['basis'] = v[0]
        return d


class AddControlScores(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddControlScores, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'control-category':
                d['control_category'] = v[0]
            elif kl == 'control-name':
                d['control_name'] = v[0]
            elif kl == 'description':
                d['description'] = v[0]
            elif kl == 'score':
                d['score'] = v[0]
        return d


class AddComplianceInformation(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddComplianceInformation, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'certification-controls':
                d['certification_controls'] = v
            elif kl == 'certification-name':
                d['certification_name'] = v[0]
        return d


class AddControlStateUpdates(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddControlStateUpdates, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'assigned-to':
                d['assigned_to'] = v[0]
            elif kl == 'comment':
                d['comment'] = v[0]
            elif kl == 'state':
                d['state'] = v[0]
            elif kl == 'updated-by':
                d['updated_by'] = v[0]
            elif kl == 'updated-date-time':
                d['updated_date_time'] = v[0]
        return d
