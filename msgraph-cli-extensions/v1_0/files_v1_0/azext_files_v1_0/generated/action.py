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


class AddParentReferenceSharepointIds(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.parent_reference_sharepoint_ids = action

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
            if kl == 'list-id':
                d['list_id'] = v[0]
            elif kl == 'list-item-id':
                d['list_item_id'] = v[0]
            elif kl == 'list-item-unique-id':
                d['list_item_unique_id'] = v[0]
            elif kl == 'site-id':
                d['site_id'] = v[0]
            elif kl == 'site-url':
                d['site_url'] = v[0]
            elif kl == 'tenant-id':
                d['tenant_id'] = v[0]
            elif kl == 'web-id':
                d['web_id'] = v[0]
        return d


class AddLastModifiedByApplication(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.last_modified_by_application = action

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


class AddListList(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.list_list = action

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
            if kl == 'content-types-enabled':
                d['content_types_enabled'] = v[0]
            elif kl == 'hidden':
                d['hidden'] = v[0]
            elif kl == 'template':
                d['template'] = v[0]
        return d


class AddListSubscriptions(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddListSubscriptions, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'application-id':
                d['application_id'] = v[0]
            elif kl == 'change-type':
                d['change_type'] = v[0]
            elif kl == 'client-state':
                d['client_state'] = v[0]
            elif kl == 'creator-id':
                d['creator_id'] = v[0]
            elif kl == 'encryption-certificate':
                d['encryption_certificate'] = v[0]
            elif kl == 'encryption-certificate-id':
                d['encryption_certificate_id'] = v[0]
            elif kl == 'expiration-date-time':
                d['expiration_date_time'] = v[0]
            elif kl == 'include-resource-data':
                d['include_resource_data'] = v[0]
            elif kl == 'latest-supported-tls-version':
                d['latest_supported_tls_version'] = v[0]
            elif kl == 'lifecycle-notification-url':
                d['lifecycle_notification_url'] = v[0]
            elif kl == 'notification-url':
                d['notification_url'] = v[0]
            elif kl == 'resource':
                d['resource'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddQuotaStoragePlanInformation(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.quota_storage_plan_information = action

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
            if kl == 'upgrade-available':
                d['upgrade_available'] = v[0]
        return d


class AddCalculated(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.calculated = action

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
            if kl == 'format':
                d['format'] = v[0]
            elif kl == 'formula':
                d['formula'] = v[0]
            elif kl == 'output-type':
                d['output_type'] = v[0]
        return d


class AddChoice(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.choice = action

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
            if kl == 'allow-text-entry':
                d['allow_text_entry'] = v[0]
            elif kl == 'choices':
                d['choices'] = v
            elif kl == 'display-as':
                d['display_as'] = v[0]
        return d


class AddDateTime(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.date_time = action

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
            if kl == 'display-as':
                d['display_as'] = v[0]
            elif kl == 'format':
                d['format'] = v[0]
        return d


class AddDefaultValue(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.default_value = action

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
            if kl == 'formula':
                d['formula'] = v[0]
            elif kl == 'value':
                d['value'] = v[0]
        return d


class AddLookup(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.lookup = action

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
            if kl == 'allow-multiple-values':
                d['allow_multiple_values'] = v[0]
            elif kl == 'allow-unlimited-length':
                d['allow_unlimited_length'] = v[0]
            elif kl == 'column-name':
                d['column_name'] = v[0]
            elif kl == 'list-id':
                d['list_id'] = v[0]
            elif kl == 'primary-lookup-column-id':
                d['primary_lookup_column_id'] = v[0]
        return d


class AddNumber(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.number = action

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
            if kl == 'decimal-places':
                d['decimal_places'] = v[0]
            elif kl == 'display-as':
                d['display_as'] = v[0]
            elif kl == 'maximum':
                d['maximum'] = v[0]
            elif kl == 'minimum':
                d['minimum'] = v[0]
        return d


class AddPersonOrGroup(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.person_or_group = action

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
            if kl == 'allow-multiple-selection':
                d['allow_multiple_selection'] = v[0]
            elif kl == 'choose-from-type':
                d['choose_from_type'] = v[0]
            elif kl == 'display-as':
                d['display_as'] = v[0]
        return d


class AddText(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.text = action

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
            if kl == 'allow-multiple-lines':
                d['allow_multiple_lines'] = v[0]
            elif kl == 'append-changes-to-existing-text':
                d['append_changes_to_existing_text'] = v[0]
            elif kl == 'lines-for-editing':
                d['lines_for_editing'] = v[0]
            elif kl == 'max-length':
                d['max_length'] = v[0]
            elif kl == 'text-type':
                d['text_type'] = v[0]
        return d


class AddOrder(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.order = action

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
            if kl == 'default':
                d['default'] = v[0]
            elif kl == 'position':
                d['position'] = v[0]
        return d


class AddColumnLinks(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddColumnLinks, self).__call__(parser, namespace, action, option_string)

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
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddContentType(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.content_type = action

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
            if kl == 'id':
                d['id'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
        return d


class AddVersions(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddVersions, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'id-fields-id':
                d['id_fields_id'] = v[0]
            elif kl == 'last-modified-date-time':
                d['last_modified_date_time'] = v[0]
            elif kl == 'publication':
                d['publication'] = v[0]
            elif kl == 'application':
                d['application'] = v[0]
            elif kl == 'device':
                d['device'] = v[0]
            elif kl == 'user':
                d['user'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddPublication(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.publication = action

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
            if kl == 'level':
                d['level'] = v[0]
            elif kl == 'version-id':
                d['version_id'] = v[0]
        return d


class AddOnenoteResources(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddOnenoteResources, self).__call__(parser, namespace, action, option_string)

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
            elif kl == 'content-url':
                d['content_url'] = v[0]
            elif kl == 'self':
                d['self_property'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddErrorDetails(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddErrorDetails, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'code':
                d['code'] = v[0]
            elif kl == 'message':
                d['message'] = v[0]
            elif kl == 'target':
                d['target'] = v[0]
        return d


class AddErrorInnerError(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.error_inner_error = action

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
            if kl == 'code':
                d['code'] = v[0]
            elif kl == 'details':
                d['details'] = v
            elif kl == 'message':
                d['message'] = v[0]
            elif kl == 'target':
                d['target'] = v[0]
        return d


class AddRecipients(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddRecipients, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'alias':
                d['alias'] = v[0]
            elif kl == 'email':
                d['email'] = v[0]
            elif kl == 'object-id':
                d['object_id'] = v[0]
        return d
