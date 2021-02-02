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


class AddBccRecipients(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddBccRecipients, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'address':
                d['address'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
        return d


class AddBody(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.body = action

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
            elif kl == 'content-type':
                d['content_type'] = v[0]
        return d


class AddCcRecipients(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddCcRecipients, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'address':
                d['address'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
        return d


class AddInternetMessageHeaders(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddInternetMessageHeaders, self).__call__(parser, namespace, action, option_string)

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
            elif kl == 'value':
                d['value'] = v[0]
        return d


class AddReplyTo(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddReplyTo, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'address':
                d['address'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
        return d


class AddToRecipients(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddToRecipients, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'address':
                d['address'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
        return d


class AddAttachments(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddAttachments, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'content-type':
                d['content_type'] = v[0]
            elif kl == 'is-inline':
                d['is_inline'] = v[0]
            elif kl == 'last-modified-date-time':
                d['last_modified_date_time'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
            elif kl == 'size':
                d['size'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddExtensions(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddExtensions, self).__call__(parser, namespace, action, option_string)

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
        return d


class AddMailUserCreateMessageMultiValueExtendedProperties(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddMailUserCreateMessageMultiValueExtendedProperties, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'value':
                d['value'] = v
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddMailUserCreateMessageSingleValueExtendedProperties(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddMailUserCreateMessageSingleValueExtendedProperties, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'value':
                d['value'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddFlagCompletedDateTime(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.flag_completed_date_time = action

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
            if kl == 'date-time':
                d['date_time'] = v[0]
            elif kl == 'time-zone':
                d['time_zone'] = v[0]
        return d


class AddMailUserCreatelFolderMultiValueExtendedProperties(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddMailUserCreatelFolderMultiValueExtendedProperties, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'value':
                d['value'] = v
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddMailUserCreatelFolderSingleValueExtendedProperties(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddMailUserCreatelFolderSingleValueExtendedProperties, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'value':
                d['value'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d


class AddOverrides(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddOverrides, self).__call__(parser, namespace, action, option_string)

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
            if kl == 'classify-as':
                d['classify_as'] = v[0]
            elif kl == 'address':
                d['address'] = v[0]
            elif kl == 'name':
                d['name'] = v[0]
            elif kl == 'id':
                d['id'] = v[0]
        return d
