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


helps['reports'] = '''
    type: group
    short-summary: Manage Reports
'''

helps['reports audit-log-audit-log-root'] = """
    type: group
    short-summary: Manage audit log audit log root with reports
"""

helps['reports audit-log-audit-log-root show-audit-log-root'] = """
    type: command
    short-summary: "Get auditLogs."
"""

helps['reports audit-log-audit-log-root update-audit-log-root'] = """
    type: command
    short-summary: "Update auditLogs."
    parameters:
      - name: --restricted-sign-ins
        long-summary: |
            Usage: --restricted-sign-ins target-tenant-id=XX app-display-name=XX app-id=XX \
applied-conditional-access-policies=XX client-app-used=XX conditional-access-status=XX correlation-id=XX \
created-date-time=XX device-detail=XX ip-address=XX is-interactive=XX resource-display-name=XX resource-id=XX \
risk-detail=XX risk-event-types=XX risk-event-types-v2=XX risk-level-aggregated=XX risk-level-during-sign-in=XX \
risk-state=XX status=XX user-display-name=XX user-id=XX user-principal-name=XX city=XX country-or-region=XX \
geo-coordinates=XX state=XX id=XX

            app-display-name: App name displayed in the Azure Portal.
            app-id: Unique GUID representing the app ID in the Azure Active Directory.
            client-app-used: Identifies the legacy client used for sign-in activity.  Includes Browser, Exchange \
Active Sync, modern clients, IMAP, MAPI, SMTP, and POP.
            correlation-id: The request ID sent from the client when the sign-in is initiated; used to troubleshoot \
sign-in activity.
            created-date-time: Date and time (UTC) the sign-in was initiated. Example: midnight on Jan 1, 2014 is \
reported as '2014-01-01T00:00:00Z'.
            device-detail: deviceDetail
            ip-address: IP address of the client used to sign in.
            is-interactive: Indicates if a sign-in is interactive or not.
            resource-display-name: Name of the resource the user signed into.
            resource-id: ID of the resource that the user signed into.
            risk-event-types: Risk event types associated with the sign-in. The possible values are: unlikelyTravel, \
anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, suspiciousIPAddress, \
leakedCredentials, investigationsThreatIntelligence,  generic, and unknownFutureValue.
            risk-event-types-v2: The list of risk event types associated with the sign-in. Possible values: \
unlikelyTravel, anonymizedIPAddress, maliciousIPAddress, unfamiliarFeatures, malwareInfectedIPAddress, \
suspiciousIPAddress, leakedCredentials, investigationsThreatIntelligence,  generic, or unknownFutureValue.
            status: signInStatus
            user-display-name: Display name of the user that initiated the sign-in.
            user-id: ID of the user that initiated the sign-in.
            user-principal-name: User principal name of the user that initiated the sign-in.
            city: Provides the city where the sign-in originated. This is calculated using latitude/longitude \
information from the sign-in activity.
            country-or-region: Provides the country code info (2 letter code) where the sign-in originated.  This is \
calculated using latitude/longitude information from the sign-in activity.
            geo-coordinates: geoCoordinates
            state: Provides the State where the sign-in originated. This is calculated using latitude/longitude \
information from the sign-in activity.
            id: Read-only.

            Multiple actions can be specified by using more than one --restricted-sign-ins argument.
"""

helps['reports audit-log'] = """
    type: group
    short-summary: Manage audit log with reports
"""

helps['reports audit-log create-directory-audit'] = """
    type: command
    short-summary: "Create new navigation property to directoryAudits for auditLogs."
    parameters:
      - name: --additional-details
        short-summary: "Indicates additional details on the activity."
        long-summary: |
            Usage: --additional-details key=XX value=XX

            key: Key for the key-value pair.
            value: Value for the key-value pair.

            Multiple actions can be specified by using more than one --additional-details argument.
      - name: --app
        short-summary: "appIdentity"
        long-summary: |
            Usage: --app app-id=XX display-name=XX service-principal-id=XX service-principal-name=XX

            app-id: Refers to the Unique GUID representing Application Id in the Azure Active Directory.
            display-name: Refers to the Application Name displayed in the Azure Portal.
            service-principal-id: Refers to the Unique GUID indicating Service Principal Id in Azure Active Directory \
for the corresponding App.
            service-principal-name: Refers to the Service Principal Name is the Application name in the tenant.
      - name: --user
        short-summary: "userIdentity"
        long-summary: |
            Usage: --user display-name=XX id=XX ip-address=XX user-principal-name=XX

            display-name: The identity's display name. Note that this may not always be available or up-to-date.
            id: Unique identifier for the identity.
            ip-address: Indicates the client IP address used by user performing the activity (audit log only).
            user-principal-name: The userPrincipalName attribute of the user.
"""

helps['reports audit-log create-restricted-sign-in'] = """
    type: command
    short-summary: "Create new navigation property to restrictedSignIns for auditLogs."
    parameters:
      - name: --applied-conditional-access-policies
        long-summary: |
            Usage: --applied-conditional-access-policies display-name=XX enforced-grant-controls=XX \
enforced-session-controls=XX id=XX result=XX

            display-name: Refers to the Name of the conditional access policy (example: 'Require MFA for Salesforce').
            enforced-grant-controls: Refers to the grant controls enforced by the conditional access policy (example: \
'Require multi-factor authentication').
            enforced-session-controls: Refers to the session controls enforced by the conditional access policy \
(example: 'Require app enforced controls').
            id: Unique GUID of the conditional access policy.

            Multiple actions can be specified by using more than one --applied-conditional-access-policies argument.
      - name: --device-detail
        short-summary: "deviceDetail"
        long-summary: |
            Usage: --device-detail browser=XX device-id=XX display-name=XX is-compliant=XX is-managed=XX \
operating-system=XX trust-type=XX

            browser: Indicates the browser information of the used for signing in.
            device-id: Refers to the UniqueID of the device used for signing in.
            display-name: Refers to the name of the device used for signing in.
            is-compliant: Indicates whether the device is compliant.
            is-managed: Indicates whether the device is managed.
            operating-system: Indicates the operating system name and version used for signing in.
            trust-type: Provides information about whether the signed-in device is Workplace Joined, AzureAD Joined, \
Domain Joined.
      - name: --status
        short-summary: "signInStatus"
        long-summary: |
            Usage: --status additional-details=XX error-code=XX failure-reason=XX

            additional-details: Provides additional details on the sign-in activity
            error-code: Provides the 5-6digit error code that's generated during a sign-in failure. Check out the list \
of error codes and messages.
            failure-reason: Provides the error message or the reason for failure for the corresponding sign-in \
activity. Check out the list of error codes and messages.
      - name: --geo-coordinates
        short-summary: "geoCoordinates"
        long-summary: |
            Usage: --geo-coordinates altitude=XX latitude=XX longitude=XX

            altitude: Optional. The altitude (height), in feet,  above sea level for the item. Read-only.
            latitude: Optional. The latitude, in decimal, for the item. Read-only.
            longitude: Optional. The longitude, in decimal, for the item. Read-only.
"""

helps['reports audit-log create-sign-in'] = """
    type: command
    short-summary: "Create new navigation property to signIns for auditLogs."
    parameters:
      - name: --applied-conditional-access-policies
        long-summary: |
            Usage: --applied-conditional-access-policies display-name=XX enforced-grant-controls=XX \
enforced-session-controls=XX id=XX result=XX

            display-name: Refers to the Name of the conditional access policy (example: 'Require MFA for Salesforce').
            enforced-grant-controls: Refers to the grant controls enforced by the conditional access policy (example: \
'Require multi-factor authentication').
            enforced-session-controls: Refers to the session controls enforced by the conditional access policy \
(example: 'Require app enforced controls').
            id: Unique GUID of the conditional access policy.

            Multiple actions can be specified by using more than one --applied-conditional-access-policies argument.
      - name: --device-detail
        short-summary: "deviceDetail"
        long-summary: |
            Usage: --device-detail browser=XX device-id=XX display-name=XX is-compliant=XX is-managed=XX \
operating-system=XX trust-type=XX

            browser: Indicates the browser information of the used for signing in.
            device-id: Refers to the UniqueID of the device used for signing in.
            display-name: Refers to the name of the device used for signing in.
            is-compliant: Indicates whether the device is compliant.
            is-managed: Indicates whether the device is managed.
            operating-system: Indicates the operating system name and version used for signing in.
            trust-type: Provides information about whether the signed-in device is Workplace Joined, AzureAD Joined, \
Domain Joined.
      - name: --status
        short-summary: "signInStatus"
        long-summary: |
            Usage: --status additional-details=XX error-code=XX failure-reason=XX

            additional-details: Provides additional details on the sign-in activity
            error-code: Provides the 5-6digit error code that's generated during a sign-in failure. Check out the list \
of error codes and messages.
            failure-reason: Provides the error message or the reason for failure for the corresponding sign-in \
activity. Check out the list of error codes and messages.
      - name: --geo-coordinates
        short-summary: "geoCoordinates"
        long-summary: |
            Usage: --geo-coordinates altitude=XX latitude=XX longitude=XX

            altitude: Optional. The altitude (height), in feet,  above sea level for the item. Read-only.
            latitude: Optional. The latitude, in decimal, for the item. Read-only.
            longitude: Optional. The longitude, in decimal, for the item. Read-only.
"""

helps['reports audit-log delete-directory-audit'] = """
    type: command
    short-summary: "Delete navigation property directoryAudits for auditLogs."
"""

helps['reports audit-log delete-restricted-sign-in'] = """
    type: command
    short-summary: "Delete navigation property restrictedSignIns for auditLogs."
"""

helps['reports audit-log delete-sign-in'] = """
    type: command
    short-summary: "Delete navigation property signIns for auditLogs."
"""

helps['reports audit-log list-directory-audit'] = """
    type: command
    short-summary: "Get directoryAudits from auditLogs."
"""

helps['reports audit-log list-restricted-sign-in'] = """
    type: command
    short-summary: "Get restrictedSignIns from auditLogs."
"""

helps['reports audit-log list-sign-in'] = """
    type: command
    short-summary: "Get signIns from auditLogs."
"""

helps['reports audit-log show-directory-audit'] = """
    type: command
    short-summary: "Get directoryAudits from auditLogs."
"""

helps['reports audit-log show-restricted-sign-in'] = """
    type: command
    short-summary: "Get restrictedSignIns from auditLogs."
"""

helps['reports audit-log show-sign-in'] = """
    type: command
    short-summary: "Get signIns from auditLogs."
"""

helps['reports audit-log update-directory-audit'] = """
    type: command
    short-summary: "Update the navigation property directoryAudits in auditLogs."
    parameters:
      - name: --additional-details
        short-summary: "Indicates additional details on the activity."
        long-summary: |
            Usage: --additional-details key=XX value=XX

            key: Key for the key-value pair.
            value: Value for the key-value pair.

            Multiple actions can be specified by using more than one --additional-details argument.
      - name: --app
        short-summary: "appIdentity"
        long-summary: |
            Usage: --app app-id=XX display-name=XX service-principal-id=XX service-principal-name=XX

            app-id: Refers to the Unique GUID representing Application Id in the Azure Active Directory.
            display-name: Refers to the Application Name displayed in the Azure Portal.
            service-principal-id: Refers to the Unique GUID indicating Service Principal Id in Azure Active Directory \
for the corresponding App.
            service-principal-name: Refers to the Service Principal Name is the Application name in the tenant.
      - name: --user
        short-summary: "userIdentity"
        long-summary: |
            Usage: --user display-name=XX id=XX ip-address=XX user-principal-name=XX

            display-name: The identity's display name. Note that this may not always be available or up-to-date.
            id: Unique identifier for the identity.
            ip-address: Indicates the client IP address used by user performing the activity (audit log only).
            user-principal-name: The userPrincipalName attribute of the user.
"""

helps['reports audit-log update-restricted-sign-in'] = """
    type: command
    short-summary: "Update the navigation property restrictedSignIns in auditLogs."
    parameters:
      - name: --applied-conditional-access-policies
        long-summary: |
            Usage: --applied-conditional-access-policies display-name=XX enforced-grant-controls=XX \
enforced-session-controls=XX id=XX result=XX

            display-name: Refers to the Name of the conditional access policy (example: 'Require MFA for Salesforce').
            enforced-grant-controls: Refers to the grant controls enforced by the conditional access policy (example: \
'Require multi-factor authentication').
            enforced-session-controls: Refers to the session controls enforced by the conditional access policy \
(example: 'Require app enforced controls').
            id: Unique GUID of the conditional access policy.

            Multiple actions can be specified by using more than one --applied-conditional-access-policies argument.
      - name: --device-detail
        short-summary: "deviceDetail"
        long-summary: |
            Usage: --device-detail browser=XX device-id=XX display-name=XX is-compliant=XX is-managed=XX \
operating-system=XX trust-type=XX

            browser: Indicates the browser information of the used for signing in.
            device-id: Refers to the UniqueID of the device used for signing in.
            display-name: Refers to the name of the device used for signing in.
            is-compliant: Indicates whether the device is compliant.
            is-managed: Indicates whether the device is managed.
            operating-system: Indicates the operating system name and version used for signing in.
            trust-type: Provides information about whether the signed-in device is Workplace Joined, AzureAD Joined, \
Domain Joined.
      - name: --status
        short-summary: "signInStatus"
        long-summary: |
            Usage: --status additional-details=XX error-code=XX failure-reason=XX

            additional-details: Provides additional details on the sign-in activity
            error-code: Provides the 5-6digit error code that's generated during a sign-in failure. Check out the list \
of error codes and messages.
            failure-reason: Provides the error message or the reason for failure for the corresponding sign-in \
activity. Check out the list of error codes and messages.
      - name: --geo-coordinates
        short-summary: "geoCoordinates"
        long-summary: |
            Usage: --geo-coordinates altitude=XX latitude=XX longitude=XX

            altitude: Optional. The altitude (height), in feet,  above sea level for the item. Read-only.
            latitude: Optional. The latitude, in decimal, for the item. Read-only.
            longitude: Optional. The longitude, in decimal, for the item. Read-only.
"""

helps['reports audit-log update-sign-in'] = """
    type: command
    short-summary: "Update the navigation property signIns in auditLogs."
    parameters:
      - name: --applied-conditional-access-policies
        long-summary: |
            Usage: --applied-conditional-access-policies display-name=XX enforced-grant-controls=XX \
enforced-session-controls=XX id=XX result=XX

            display-name: Refers to the Name of the conditional access policy (example: 'Require MFA for Salesforce').
            enforced-grant-controls: Refers to the grant controls enforced by the conditional access policy (example: \
'Require multi-factor authentication').
            enforced-session-controls: Refers to the session controls enforced by the conditional access policy \
(example: 'Require app enforced controls').
            id: Unique GUID of the conditional access policy.

            Multiple actions can be specified by using more than one --applied-conditional-access-policies argument.
      - name: --device-detail
        short-summary: "deviceDetail"
        long-summary: |
            Usage: --device-detail browser=XX device-id=XX display-name=XX is-compliant=XX is-managed=XX \
operating-system=XX trust-type=XX

            browser: Indicates the browser information of the used for signing in.
            device-id: Refers to the UniqueID of the device used for signing in.
            display-name: Refers to the name of the device used for signing in.
            is-compliant: Indicates whether the device is compliant.
            is-managed: Indicates whether the device is managed.
            operating-system: Indicates the operating system name and version used for signing in.
            trust-type: Provides information about whether the signed-in device is Workplace Joined, AzureAD Joined, \
Domain Joined.
      - name: --status
        short-summary: "signInStatus"
        long-summary: |
            Usage: --status additional-details=XX error-code=XX failure-reason=XX

            additional-details: Provides additional details on the sign-in activity
            error-code: Provides the 5-6digit error code that's generated during a sign-in failure. Check out the list \
of error codes and messages.
            failure-reason: Provides the error message or the reason for failure for the corresponding sign-in \
activity. Check out the list of error codes and messages.
      - name: --geo-coordinates
        short-summary: "geoCoordinates"
        long-summary: |
            Usage: --geo-coordinates altitude=XX latitude=XX longitude=XX

            altitude: Optional. The altitude (height), in feet,  above sea level for the item. Read-only.
            latitude: Optional. The latitude, in decimal, for the item. Read-only.
            longitude: Optional. The longitude, in decimal, for the item. Read-only.
"""

helps['reports report-root'] = """
    type: group
    short-summary: Manage report report root with reports
"""

helps['reports report-root show-report-root'] = """
    type: command
    short-summary: "Get reports."
"""

helps['reports report-root update-report-root'] = """
    type: command
    short-summary: "Update reports."
"""

helps['reports report'] = """
    type: group
    short-summary: Manage report with reports
"""

helps['reports report device-configuration-device-activity'] = """
    type: command
    short-summary: "Invoke function deviceConfigurationDeviceActivity."
"""

helps['reports report device-configuration-user-activity'] = """
    type: command
    short-summary: "Invoke function deviceConfigurationUserActivity."
"""

helps['reports report managed-device-enrollment-failure-details027-e'] = """
    type: command
    short-summary: "Invoke function managedDeviceEnrollmentFailureDetails."
"""

helps['reports report managed-device-enrollment-failure-details2-b3-d'] = """
    type: command
    short-summary: "Invoke function managedDeviceEnrollmentFailureDetails."
"""

helps['reports report managed-device-enrollment-top-failure-afd1'] = """
    type: command
    short-summary: "Invoke function managedDeviceEnrollmentTopFailures."
"""

helps['reports report managed-device-enrollment-top-failures4669'] = """
    type: command
    short-summary: "Invoke function managedDeviceEnrollmentTopFailures."
"""

helps['reports report show-email-activity-count'] = """
    type: command
    short-summary: "Invoke function getEmailActivityCounts."
"""

helps['reports report show-email-activity-user-count'] = """
    type: command
    short-summary: "Invoke function getEmailActivityUserCounts."
"""

helps['reports report show-email-activity-user-detail-ddb2'] = """
    type: command
    short-summary: "Invoke function getEmailActivityUserDetail."
"""

helps['reports report show-email-activity-user-detail-fe32'] = """
    type: command
    short-summary: "Invoke function getEmailActivityUserDetail."
"""

helps['reports report show-email-app-usage-app-user-count'] = """
    type: command
    short-summary: "Invoke function getEmailAppUsageAppsUserCounts."
"""

helps['reports report show-email-app-usage-user-count'] = """
    type: command
    short-summary: "Invoke function getEmailAppUsageUserCounts."
"""

helps['reports report show-email-app-usage-user-detail546-b'] = """
    type: command
    short-summary: "Invoke function getEmailAppUsageUserDetail."
"""

helps['reports report show-email-app-usage-user-detail62-ec'] = """
    type: command
    short-summary: "Invoke function getEmailAppUsageUserDetail."
"""

helps['reports report show-email-app-usage-version-user-count'] = """
    type: command
    short-summary: "Invoke function getEmailAppUsageVersionsUserCounts."
"""

helps['reports report show-mailbox-usage-detail'] = """
    type: command
    short-summary: "Invoke function getMailboxUsageDetail."
"""

helps['reports report show-mailbox-usage-mailbox-count'] = """
    type: command
    short-summary: "Invoke function getMailboxUsageMailboxCounts."
"""

helps['reports report show-mailbox-usage-quota-status-mailbox-count'] = """
    type: command
    short-summary: "Invoke function getMailboxUsageQuotaStatusMailboxCounts."
"""

helps['reports report show-mailbox-usage-storage'] = """
    type: command
    short-summary: "Invoke function getMailboxUsageStorage."
"""

helps['reports report show-office365-activation-count'] = """
    type: command
    short-summary: "Invoke function getOffice365ActivationCounts."
"""

helps['reports report show-office365-activation-user-count'] = """
    type: command
    short-summary: "Invoke function getOffice365ActivationsUserCounts."
"""

helps['reports report show-office365-activation-user-detail'] = """
    type: command
    short-summary: "Invoke function getOffice365ActivationsUserDetail."
"""

helps['reports report show-office365-active-user-count'] = """
    type: command
    short-summary: "Invoke function getOffice365ActiveUserCounts."
"""

helps['reports report show-office365-active-user-detail-d389'] = """
    type: command
    short-summary: "Invoke function getOffice365ActiveUserDetail."
"""

helps['reports report show-office365-active-user-detail68-ad'] = """
    type: command
    short-summary: "Invoke function getOffice365ActiveUserDetail."
"""

helps['reports report show-office365-group-activity-count'] = """
    type: command
    short-summary: "Invoke function getOffice365GroupsActivityCounts."
"""

helps['reports report show-office365-group-activity-detail38-f6'] = """
    type: command
    short-summary: "Invoke function getOffice365GroupsActivityDetail."
"""

helps['reports report show-office365-group-activity-detail81-cc'] = """
    type: command
    short-summary: "Invoke function getOffice365GroupsActivityDetail."
"""

helps['reports report show-office365-group-activity-file-count'] = """
    type: command
    short-summary: "Invoke function getOffice365GroupsActivityFileCounts."
"""

helps['reports report show-office365-group-activity-group-count'] = """
    type: command
    short-summary: "Invoke function getOffice365GroupsActivityGroupCounts."
"""

helps['reports report show-office365-group-activity-storage'] = """
    type: command
    short-summary: "Invoke function getOffice365GroupsActivityStorage."
"""

helps['reports report show-office365-service-user-count'] = """
    type: command
    short-summary: "Invoke function getOffice365ServicesUserCounts."
"""

helps['reports report show-one-drive-activity-file-count'] = """
    type: command
    short-summary: "Invoke function getOneDriveActivityFileCounts."
"""

helps['reports report show-one-drive-activity-user-count'] = """
    type: command
    short-summary: "Invoke function getOneDriveActivityUserCounts."
"""

helps['reports report show-one-drive-activity-user-detail-c424'] = """
    type: command
    short-summary: "Invoke function getOneDriveActivityUserDetail."
"""

helps['reports report show-one-drive-activity-user-detail05-f1'] = """
    type: command
    short-summary: "Invoke function getOneDriveActivityUserDetail."
"""

helps['reports report show-one-drive-usage-account-count'] = """
    type: command
    short-summary: "Invoke function getOneDriveUsageAccountCounts."
"""

helps['reports report show-one-drive-usage-account-detail-dd7-f'] = """
    type: command
    short-summary: "Invoke function getOneDriveUsageAccountDetail."
"""

helps['reports report show-one-drive-usage-account-detail-e827'] = """
    type: command
    short-summary: "Invoke function getOneDriveUsageAccountDetail."
"""

helps['reports report show-one-drive-usage-file-count'] = """
    type: command
    short-summary: "Invoke function getOneDriveUsageFileCounts."
"""

helps['reports report show-one-drive-usage-storage'] = """
    type: command
    short-summary: "Invoke function getOneDriveUsageStorage."
"""

helps['reports report show-share-point-activity-file-count'] = """
    type: command
    short-summary: "Invoke function getSharePointActivityFileCounts."
"""

helps['reports report show-share-point-activity-page'] = """
    type: command
    short-summary: "Invoke function getSharePointActivityPages."
"""

helps['reports report show-share-point-activity-user-count'] = """
    type: command
    short-summary: "Invoke function getSharePointActivityUserCounts."
"""

helps['reports report show-share-point-activity-user-detail-b778'] = """
    type: command
    short-summary: "Invoke function getSharePointActivityUserDetail."
"""

helps['reports report show-share-point-activity-user-detail-f3-be'] = """
    type: command
    short-summary: "Invoke function getSharePointActivityUserDetail."
"""

helps['reports report show-share-point-site-usage-detail-d27-a'] = """
    type: command
    short-summary: "Invoke function getSharePointSiteUsageDetail."
"""

helps['reports report show-share-point-site-usage-detail204-b'] = """
    type: command
    short-summary: "Invoke function getSharePointSiteUsageDetail."
"""

helps['reports report show-share-point-site-usage-file-count'] = """
    type: command
    short-summary: "Invoke function getSharePointSiteUsageFileCounts."
"""

helps['reports report show-share-point-site-usage-page'] = """
    type: command
    short-summary: "Invoke function getSharePointSiteUsagePages."
"""

helps['reports report show-share-point-site-usage-site-count'] = """
    type: command
    short-summary: "Invoke function getSharePointSiteUsageSiteCounts."
"""

helps['reports report show-share-point-site-usage-storage'] = """
    type: command
    short-summary: "Invoke function getSharePointSiteUsageStorage."
"""

helps['reports report show-skype-for-business-activity-count'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessActivityCounts."
"""

helps['reports report show-skype-for-business-activity-user-count'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessActivityUserCounts."
"""

helps['reports report show-skype-for-business-activity-user-detail-e4-c9'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessActivityUserDetail."
"""

helps['reports report show-skype-for-business-activity-user-detail744-e'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessActivityUserDetail."
"""

helps['reports report show-skype-for-business-device-usage-distribution-user-count'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessDeviceUsageDistributionUserCounts."
"""

helps['reports report show-skype-for-business-device-usage-user-count'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessDeviceUsageUserCounts."
"""

helps['reports report show-skype-for-business-device-usage-user-detail-a692'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessDeviceUsageUserDetail."
"""

helps['reports report show-skype-for-business-device-usage-user-detail-e753'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessDeviceUsageUserDetail."
"""

helps['reports report show-skype-for-business-organizer-activity-count'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessOrganizerActivityCounts."
"""

helps['reports report show-skype-for-business-organizer-activity-minute-count'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessOrganizerActivityMinuteCounts."
"""

helps['reports report show-skype-for-business-organizer-activity-user-count'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessOrganizerActivityUserCounts."
"""

helps['reports report show-skype-for-business-participant-activity-count'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessParticipantActivityCounts."
"""

helps['reports report show-skype-for-business-participant-activity-minute-count'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessParticipantActivityMinuteCounts."
"""

helps['reports report show-skype-for-business-participant-activity-user-count'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessParticipantActivityUserCounts."
"""

helps['reports report show-skype-for-business-peer-to-peer-activity-count'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessPeerToPeerActivityCounts."
"""

helps['reports report show-skype-for-business-peer-to-peer-activity-minute-count'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessPeerToPeerActivityMinuteCounts."
"""

helps['reports report show-skype-for-business-peer-to-peer-activity-user-count'] = """
    type: command
    short-summary: "Invoke function getSkypeForBusinessPeerToPeerActivityUserCounts."
"""

helps['reports report show-team-device-usage-distribution-user-count'] = """
    type: command
    short-summary: "Invoke function getTeamsDeviceUsageDistributionUserCounts."
"""

helps['reports report show-team-device-usage-user-count'] = """
    type: command
    short-summary: "Invoke function getTeamsDeviceUsageUserCounts."
"""

helps['reports report show-team-device-usage-user-detail7148'] = """
    type: command
    short-summary: "Invoke function getTeamsDeviceUsageUserDetail."
"""

helps['reports report show-team-device-usage-user-detail7565'] = """
    type: command
    short-summary: "Invoke function getTeamsDeviceUsageUserDetail."
"""

helps['reports report show-team-user-activity-count'] = """
    type: command
    short-summary: "Invoke function getTeamsUserActivityCounts."
"""

helps['reports report show-team-user-activity-user-count'] = """
    type: command
    short-summary: "Invoke function getTeamsUserActivityUserCounts."
"""

helps['reports report show-team-user-activity-user-detail-a3-f1'] = """
    type: command
    short-summary: "Invoke function getTeamsUserActivityUserDetail."
"""

helps['reports report show-team-user-activity-user-detail-eb13'] = """
    type: command
    short-summary: "Invoke function getTeamsUserActivityUserDetail."
"""

helps['reports report show-yammer-activity-count'] = """
    type: command
    short-summary: "Invoke function getYammerActivityCounts."
"""

helps['reports report show-yammer-activity-user-count'] = """
    type: command
    short-summary: "Invoke function getYammerActivityUserCounts."
"""

helps['reports report show-yammer-activity-user-detail-ac30'] = """
    type: command
    short-summary: "Invoke function getYammerActivityUserDetail."
"""

helps['reports report show-yammer-activity-user-detail15-a5'] = """
    type: command
    short-summary: "Invoke function getYammerActivityUserDetail."
"""

helps['reports report show-yammer-device-usage-distribution-user-count'] = """
    type: command
    short-summary: "Invoke function getYammerDeviceUsageDistributionUserCounts."
"""

helps['reports report show-yammer-device-usage-user-count'] = """
    type: command
    short-summary: "Invoke function getYammerDeviceUsageUserCounts."
"""

helps['reports report show-yammer-device-usage-user-detail-cfad'] = """
    type: command
    short-summary: "Invoke function getYammerDeviceUsageUserDetail."
"""

helps['reports report show-yammer-device-usage-user-detail-d0-ac'] = """
    type: command
    short-summary: "Invoke function getYammerDeviceUsageUserDetail."
"""

helps['reports report show-yammer-group-activity-count'] = """
    type: command
    short-summary: "Invoke function getYammerGroupsActivityCounts."
"""

helps['reports report show-yammer-group-activity-detail-da9-a'] = """
    type: command
    short-summary: "Invoke function getYammerGroupsActivityDetail."
"""

helps['reports report show-yammer-group-activity-detail0-d7-d'] = """
    type: command
    short-summary: "Invoke function getYammerGroupsActivityDetail."
"""

helps['reports report show-yammer-group-activity-group-count'] = """
    type: command
    short-summary: "Invoke function getYammerGroupsActivityGroupCounts."
"""
