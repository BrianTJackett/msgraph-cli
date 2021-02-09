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


helps['crossdeviceexperiences user'] = """
    type: group
    short-summary: Manage user with crossdeviceexperiences_v1_0
"""

helps['crossdeviceexperiences user delete'] = """
    type: command
    short-summary: "Delete navigation property activities for users."
"""

helps['crossdeviceexperiences user create-activity'] = """
    type: command
    short-summary: "Create new navigation property to activities for users."
    parameters:
      - name: --attribution
        short-summary: "imageInfo"
        long-summary: |
            Usage: --attribution add-image-query=XX alternate-text=XX alternative-text=XX icon-url=XX

            add-image-query: Optional; parameter used to indicate the server is able to render image dynamically in \
response to parameterization. For example – a high contrast image
            alternate-text: Optional; alt-text accessible content for the image
            icon-url: Optional; URI that points to an icon which represents the application used to generate the \
activity
"""

helps['crossdeviceexperiences user list-activity'] = """
    type: command
    short-summary: "Get activities from users."
"""

helps['crossdeviceexperiences user show-activity'] = """
    type: command
    short-summary: "Get activities from users."
"""

helps['crossdeviceexperiences user update-activity'] = """
    type: command
    short-summary: "Update the navigation property activities in users."
    parameters:
      - name: --attribution
        short-summary: "imageInfo"
        long-summary: |
            Usage: --attribution add-image-query=XX alternate-text=XX alternative-text=XX icon-url=XX

            add-image-query: Optional; parameter used to indicate the server is able to render image dynamically in \
response to parameterization. For example – a high contrast image
            alternate-text: Optional; alt-text accessible content for the image
            icon-url: Optional; URI that points to an icon which represents the application used to generate the \
activity
"""

helps['crossdeviceexperiences user-activity'] = """
    type: group
    short-summary: Manage user activity with crossdeviceexperiences_v1_0
"""

helps['crossdeviceexperiences user-activity delete'] = """
    type: command
    short-summary: "Delete navigation property historyItems for users."
"""

helps['crossdeviceexperiences user-activity create-history-item'] = """
    type: command
    short-summary: "Create new navigation property to historyItems for users."
"""

helps['crossdeviceexperiences user-activity list-history-item'] = """
    type: command
    short-summary: "Get historyItems from users."
"""

helps['crossdeviceexperiences user-activity show-history-item'] = """
    type: command
    short-summary: "Get historyItems from users."
"""

helps['crossdeviceexperiences user-activity update-history-item'] = """
    type: command
    short-summary: "Update the navigation property historyItems in users."
"""

helps['crossdeviceexperiences user-activity-history-item'] = """
    type: group
    short-summary: Manage user activity history item with crossdeviceexperiences_v1_0
"""

helps['crossdeviceexperiences user-activity-history-item delete'] = """
    type: command
    short-summary: "Delete ref of navigation property activity for users."
"""

helps['crossdeviceexperiences user-activity-history-item set-ref-activity'] = """
    type: command
    short-summary: "Update the ref of navigation property activity in users."
"""

helps['crossdeviceexperiences user-activity-history-item show-activity'] = """
    type: command
    short-summary: "Get activity from users."
"""

helps['crossdeviceexperiences user-activity-history-item show-ref-activity'] = """
    type: command
    short-summary: "Get ref of activity from users."
"""
