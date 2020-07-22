# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['usersmail'] = """
    type: group
    short-summary: usersmail
"""

helps['usersmail update'] = """
    type: command
    short-summary: Update the navigation property inferenceClassification in users
    parameters:
      - name: --single-value-extended-properties
        short-summary: The collection of single-value extended properties defined for the mailFolder. Read-only. \
Nullable.
        long-summary: |
            Usage: --single-value-extended-properties value=XX id=XX

            value: A property value.
            id: Read-only.

            Multiple actions can be specified by using more than one --single-value-extended-properties argument.
      - name: --multi-value-extended-properties
        short-summary: The collection of multi-value extended properties defined for the mailFolder. Read-only. \
Nullable.
        long-summary: |
            Usage: --multi-value-extended-properties value=XX id=XX

            value: A collection of property values.
            id: Read-only.

            Multiple actions can be specified by using more than one --multi-value-extended-properties argument.
      - name: --user-configurations
        long-summary: |
            Usage: --user-configurations binary-data=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --user-configurations argument.
"""

helps['usersmail create-mail-folder'] = """
    type: command
    short-summary: Create new navigation property to mailFolders for users
    parameters:
      - name: --single-value-extended-properties
        short-summary: The collection of single-value extended properties defined for the mailFolder. Read-only. \
Nullable.
        long-summary: |
            Usage: --single-value-extended-properties value=XX id=XX

            value: A property value.
            id: Read-only.

            Multiple actions can be specified by using more than one --single-value-extended-properties argument.
      - name: --multi-value-extended-properties
        short-summary: The collection of multi-value extended properties defined for the mailFolder. Read-only. \
Nullable.
        long-summary: |
            Usage: --multi-value-extended-properties value=XX id=XX

            value: A collection of property values.
            id: Read-only.

            Multiple actions can be specified by using more than one --multi-value-extended-properties argument.
      - name: --user-configurations
        long-summary: |
            Usage: --user-configurations binary-data=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --user-configurations argument.
"""

helps['usersmail create-message'] = """
    type: command
    short-summary: Create new navigation property to messages for users
"""

helps['usersmail get-inference-classification'] = """
    type: command
    short-summary: Get inferenceClassification from users
"""

helps['usersmail get-mail-folder'] = """
    type: command
    short-summary: Get mailFolders from users
"""

helps['usersmail get-message'] = """
    type: command
    short-summary: Get messages from users
"""

helps['usersmail list-mail-folder'] = """
    type: command
    short-summary: Get mailFolders from users
"""

helps['usersmail list-message'] = """
    type: command
    short-summary: Get messages from users
"""

helps['usersmail'] = """
    type: group
    short-summary: usersmail
"""

helps['usersmail update'] = """
    type: command
    short-summary: Update the navigation property overrides in users
"""

helps['usersmail create-override'] = """
    type: command
    short-summary: Create new navigation property to overrides for users
"""

helps['usersmail get-override'] = """
    type: command
    short-summary: Get overrides from users
"""

helps['usersmail list-override'] = """
    type: command
    short-summary: Get overrides from users
"""

helps['usersmail'] = """
    type: group
    short-summary: usersmail
"""

helps['usersmail update'] = """
    type: command
    short-summary: Update the navigation property userConfigurations in users
    parameters:
      - name: --single-value-extended-properties
        short-summary: The collection of single-value extended properties defined for the mailFolder. Read-only. \
Nullable.
        long-summary: |
            Usage: --single-value-extended-properties value=XX id=XX

            value: A property value.
            id: Read-only.

            Multiple actions can be specified by using more than one --single-value-extended-properties argument.
      - name: --multi-value-extended-properties
        short-summary: The collection of multi-value extended properties defined for the mailFolder. Read-only. \
Nullable.
        long-summary: |
            Usage: --multi-value-extended-properties value=XX id=XX

            value: A collection of property values.
            id: Read-only.

            Multiple actions can be specified by using more than one --multi-value-extended-properties argument.
      - name: --user-configurations
        long-summary: |
            Usage: --user-configurations binary-data=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --user-configurations argument.
"""

helps['usersmail create-child-folder'] = """
    type: command
    short-summary: Create new navigation property to childFolders for users
    parameters:
      - name: --single-value-extended-properties
        short-summary: The collection of single-value extended properties defined for the mailFolder. Read-only. \
Nullable.
        long-summary: |
            Usage: --single-value-extended-properties value=XX id=XX

            value: A property value.
            id: Read-only.

            Multiple actions can be specified by using more than one --single-value-extended-properties argument.
      - name: --multi-value-extended-properties
        short-summary: The collection of multi-value extended properties defined for the mailFolder. Read-only. \
Nullable.
        long-summary: |
            Usage: --multi-value-extended-properties value=XX id=XX

            value: A collection of property values.
            id: Read-only.

            Multiple actions can be specified by using more than one --multi-value-extended-properties argument.
      - name: --user-configurations
        long-summary: |
            Usage: --user-configurations binary-data=XX id=XX

            id: Read-only.

            Multiple actions can be specified by using more than one --user-configurations argument.
"""

helps['usersmail create-message'] = """
    type: command
    short-summary: Create new navigation property to messages for users
"""

helps['usersmail create-message-rule'] = """
    type: command
    short-summary: Create new navigation property to messageRules for users
"""

helps['usersmail create-multi-value-extended-property'] = """
    type: command
    short-summary: Create new navigation property to multiValueExtendedProperties for users
"""

helps['usersmail create-single-value-extended-property'] = """
    type: command
    short-summary: Create new navigation property to singleValueExtendedProperties for users
"""

helps['usersmail create-user-configuration'] = """
    type: command
    short-summary: Create new navigation property to userConfigurations for users
"""

helps['usersmail get-child-folder'] = """
    type: command
    short-summary: Get childFolders from users
"""

helps['usersmail get-message'] = """
    type: command
    short-summary: Get messages from users
"""

helps['usersmail get-message-rule'] = """
    type: command
    short-summary: Get messageRules from users
"""

helps['usersmail get-multi-value-extended-property'] = """
    type: command
    short-summary: Get multiValueExtendedProperties from users
"""

helps['usersmail get-single-value-extended-property'] = """
    type: command
    short-summary: Get singleValueExtendedProperties from users
"""

helps['usersmail get-user-configuration'] = """
    type: command
    short-summary: Get userConfigurations from users
"""

helps['usersmail list-child-folder'] = """
    type: command
    short-summary: Get childFolders from users
"""

helps['usersmail list-message'] = """
    type: command
    short-summary: Get messages from users
"""

helps['usersmail list-message-rule'] = """
    type: command
    short-summary: Get messageRules from users
"""

helps['usersmail list-multi-value-extended-property'] = """
    type: command
    short-summary: Get multiValueExtendedProperties from users
"""

helps['usersmail list-single-value-extended-property'] = """
    type: command
    short-summary: Get singleValueExtendedProperties from users
"""

helps['usersmail list-user-configuration'] = """
    type: command
    short-summary: Get userConfigurations from users
"""

helps['usersmail'] = """
    type: group
    short-summary: usersmail
"""

helps['usersmail update'] = """
    type: command
    short-summary: Update the navigation property singleValueExtendedProperties in users
"""

helps['usersmail create-attachment'] = """
    type: command
    short-summary: Create new navigation property to attachments for users
"""

helps['usersmail create-extension'] = """
    type: command
    short-summary: Create new navigation property to extensions for users
"""

helps['usersmail create-mention'] = """
    type: command
    short-summary: Create new navigation property to mentions for users
    parameters:
      - name: --mentioned
        short-summary: emailAddress
        long-summary: |
            Usage: --mentioned name=XX address=XX

            name: The display name of the person or entity.
            address: The email address of the person or entity.
      - name: --created-by
        short-summary: emailAddress
        long-summary: |
            Usage: --created-by name=XX address=XX

            name: The display name of the person or entity.
            address: The email address of the person or entity.
"""

helps['usersmail create-multi-value-extended-property'] = """
    type: command
    short-summary: Create new navigation property to multiValueExtendedProperties for users
"""

helps['usersmail create-single-value-extended-property'] = """
    type: command
    short-summary: Create new navigation property to singleValueExtendedProperties for users
"""

helps['usersmail get-attachment'] = """
    type: command
    short-summary: Get attachments from users
"""

helps['usersmail get-extension'] = """
    type: command
    short-summary: Get extensions from users
"""

helps['usersmail get-mention'] = """
    type: command
    short-summary: Get mentions from users
"""

helps['usersmail get-multi-value-extended-property'] = """
    type: command
    short-summary: Get multiValueExtendedProperties from users
"""

helps['usersmail get-single-value-extended-property'] = """
    type: command
    short-summary: Get singleValueExtendedProperties from users
"""

helps['usersmail list-attachment'] = """
    type: command
    short-summary: Get attachments from users
"""

helps['usersmail list-extension'] = """
    type: command
    short-summary: Get extensions from users
"""

helps['usersmail list-mention'] = """
    type: command
    short-summary: Get mentions from users
"""

helps['usersmail list-multi-value-extended-property'] = """
    type: command
    short-summary: Get multiValueExtendedProperties from users
"""

helps['usersmail list-single-value-extended-property'] = """
    type: command
    short-summary: Get singleValueExtendedProperties from users
"""

helps['usersmail'] = """
    type: group
    short-summary: usersmail
"""

helps['usersmail update'] = """
    type: command
    short-summary: Update the navigation property singleValueExtendedProperties in users
"""

helps['usersmail create-attachment'] = """
    type: command
    short-summary: Create new navigation property to attachments for users
"""

helps['usersmail create-extension'] = """
    type: command
    short-summary: Create new navigation property to extensions for users
"""

helps['usersmail create-mention'] = """
    type: command
    short-summary: Create new navigation property to mentions for users
    parameters:
      - name: --mentioned
        short-summary: emailAddress
        long-summary: |
            Usage: --mentioned name=XX address=XX

            name: The display name of the person or entity.
            address: The email address of the person or entity.
      - name: --created-by
        short-summary: emailAddress
        long-summary: |
            Usage: --created-by name=XX address=XX

            name: The display name of the person or entity.
            address: The email address of the person or entity.
"""

helps['usersmail create-multi-value-extended-property'] = """
    type: command
    short-summary: Create new navigation property to multiValueExtendedProperties for users
"""

helps['usersmail create-single-value-extended-property'] = """
    type: command
    short-summary: Create new navigation property to singleValueExtendedProperties for users
"""

helps['usersmail get-attachment'] = """
    type: command
    short-summary: Get attachments from users
"""

helps['usersmail get-extension'] = """
    type: command
    short-summary: Get extensions from users
"""

helps['usersmail get-mention'] = """
    type: command
    short-summary: Get mentions from users
"""

helps['usersmail get-multi-value-extended-property'] = """
    type: command
    short-summary: Get multiValueExtendedProperties from users
"""

helps['usersmail get-single-value-extended-property'] = """
    type: command
    short-summary: Get singleValueExtendedProperties from users
"""

helps['usersmail list-attachment'] = """
    type: command
    short-summary: Get attachments from users
"""

helps['usersmail list-extension'] = """
    type: command
    short-summary: Get extensions from users
"""

helps['usersmail list-mention'] = """
    type: command
    short-summary: Get mentions from users
"""

helps['usersmail list-multi-value-extended-property'] = """
    type: command
    short-summary: Get multiValueExtendedProperties from users
"""

helps['usersmail list-single-value-extended-property'] = """
    type: command
    short-summary: Get singleValueExtendedProperties from users
"""
