# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CollectionOfContact(msrest.serialization.Model):
    """Collection of contact.

    :param value:
    :type value: list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphContact]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphContact]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfContact, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class CollectionOfContact0(msrest.serialization.Model):
    """Collection of contact.

    :param value:
    :type value: list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphContact]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphContact]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfContact0, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class CollectionOfContactFolder(msrest.serialization.Model):
    """Collection of contactFolder.

    :param value:
    :type value: list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphContactFolder]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphContactFolder]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfContactFolder, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class CollectionOfContactFolder0(msrest.serialization.Model):
    """Collection of contactFolder.

    :param value:
    :type value: list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphContactFolder]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphContactFolder]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfContactFolder0, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class CollectionOfExtension(msrest.serialization.Model):
    """Collection of extension.

    :param value:
    :type value: list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphEntity]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphEntity]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfExtension, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class CollectionOfExtension0(msrest.serialization.Model):
    """Collection of extension.

    :param value:
    :type value: list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphEntity]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphEntity]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfExtension0, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class CollectionOfMultiValueLegacyExtendedProperty(msrest.serialization.Model):
    """Collection of multiValueLegacyExtendedProperty.

    :param value:
    :type value:
     list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphMultiValueLegacyExtendedProperty]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphMultiValueLegacyExtendedProperty]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfMultiValueLegacyExtendedProperty, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class CollectionOfMultiValueLegacyExtendedProperty0(msrest.serialization.Model):
    """Collection of multiValueLegacyExtendedProperty.

    :param value:
    :type value:
     list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphMultiValueLegacyExtendedProperty]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphMultiValueLegacyExtendedProperty]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfMultiValueLegacyExtendedProperty0, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class CollectionOfMultiValueLegacyExtendedProperty1(msrest.serialization.Model):
    """Collection of multiValueLegacyExtendedProperty.

    :param value:
    :type value:
     list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphMultiValueLegacyExtendedProperty]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphMultiValueLegacyExtendedProperty]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfMultiValueLegacyExtendedProperty1, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class CollectionOfSingleValueLegacyExtendedProperty(msrest.serialization.Model):
    """Collection of singleValueLegacyExtendedProperty.

    :param value:
    :type value:
     list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphSingleValueLegacyExtendedProperty]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphSingleValueLegacyExtendedProperty]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfSingleValueLegacyExtendedProperty, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class CollectionOfSingleValueLegacyExtendedProperty0(msrest.serialization.Model):
    """Collection of singleValueLegacyExtendedProperty.

    :param value:
    :type value:
     list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphSingleValueLegacyExtendedProperty]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphSingleValueLegacyExtendedProperty]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfSingleValueLegacyExtendedProperty0, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class CollectionOfSingleValueLegacyExtendedProperty1(msrest.serialization.Model):
    """Collection of singleValueLegacyExtendedProperty.

    :param value:
    :type value:
     list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphSingleValueLegacyExtendedProperty]
    :param odata_next_link:
    :type odata_next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[MicrosoftGraphSingleValueLegacyExtendedProperty]'},
        'odata_next_link': {'key': '@odata\\.nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CollectionOfSingleValueLegacyExtendedProperty1, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.odata_next_link = kwargs.get('odata_next_link', None)


class MicrosoftGraphEntity(msrest.serialization.Model):
    """entity.

    :param id: Read-only.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphEntity, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)


class MicrosoftGraphOutlookItem(MicrosoftGraphEntity):
    """outlookItem.

    :param id: Read-only.
    :type id: str
    :param created_date_time: The Timestamp type represents date and time information using ISO
     8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like
     this: '2014-01-01T00:00:00Z'.
    :type created_date_time: ~datetime.datetime
    :param last_modified_date_time: The Timestamp type represents date and time information using
     ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look
     like this: '2014-01-01T00:00:00Z'.
    :type last_modified_date_time: ~datetime.datetime
    :param change_key: Identifies the version of the item. Every time the item is changed,
     changeKey changes as well. This allows Exchange to apply changes to the correct version of the
     object. Read-only.
    :type change_key: str
    :param categories: The categories associated with the item.
    :type categories: list[str]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'change_key': {'key': 'changeKey', 'type': 'str'},
        'categories': {'key': 'categories', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphOutlookItem, self).__init__(**kwargs)
        self.created_date_time = kwargs.get('created_date_time', None)
        self.last_modified_date_time = kwargs.get('last_modified_date_time', None)
        self.change_key = kwargs.get('change_key', None)
        self.categories = kwargs.get('categories', None)


class MicrosoftGraphContact(MicrosoftGraphOutlookItem):
    """contact.

    :param id: Read-only.
    :type id: str
    :param created_date_time: The Timestamp type represents date and time information using ISO
     8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look like
     this: '2014-01-01T00:00:00Z'.
    :type created_date_time: ~datetime.datetime
    :param last_modified_date_time: The Timestamp type represents date and time information using
     ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 would look
     like this: '2014-01-01T00:00:00Z'.
    :type last_modified_date_time: ~datetime.datetime
    :param change_key: Identifies the version of the item. Every time the item is changed,
     changeKey changes as well. This allows Exchange to apply changes to the correct version of the
     object. Read-only.
    :type change_key: str
    :param categories: The categories associated with the item.
    :type categories: list[str]
    :param parent_folder_id: The ID of the contact's parent folder.
    :type parent_folder_id: str
    :param birthday: The contact's birthday. The Timestamp type represents date and time
     information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan
     1, 2014 would look like this: '2014-01-01T00:00:00Z'.
    :type birthday: ~datetime.datetime
    :param file_as: The name the contact is filed under.
    :type file_as: str
    :param display_name: The contact's display name. You can specify the display name in a create
     or update operation. Note that later updates to other properties may cause an automatically
     generated value to overwrite the displayName value you have specified. To preserve a pre-
     existing value, always include it as displayName in an update operation.
    :type display_name: str
    :param given_name: The contact's given name.
    :type given_name: str
    :param initials: The contact's initials.
    :type initials: str
    :param middle_name: The contact's middle name.
    :type middle_name: str
    :param nick_name: The contact's nickname.
    :type nick_name: str
    :param surname: The contact's surname.
    :type surname: str
    :param title: The contact's title.
    :type title: str
    :param yomi_given_name: The phonetic Japanese given name (first name) of the contact.
    :type yomi_given_name: str
    :param yomi_surname: The phonetic Japanese surname (last name)  of the contact.
    :type yomi_surname: str
    :param yomi_company_name: The phonetic Japanese company name of the contact.
    :type yomi_company_name: str
    :param generation: The contact's generation.
    :type generation: str
    :param email_addresses: The contact's email addresses.
    :type email_addresses: list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphTypedEmailAddress]
    :param websites:
    :type websites: list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphWebsite]
    :param im_addresses: The contact's instant messaging (IM) addresses.
    :type im_addresses: list[str]
    :param job_title: The contact’s job title.
    :type job_title: str
    :param company_name: The name of the contact's company.
    :type company_name: str
    :param department: The contact's department.
    :type department: str
    :param office_location: The location of the contact's office.
    :type office_location: str
    :param profession: The contact's profession.
    :type profession: str
    :param assistant_name: The name of the contact's assistant.
    :type assistant_name: str
    :param manager: The name of the contact's manager.
    :type manager: str
    :param phones:
    :type phones: list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphPhone]
    :param postal_addresses:
    :type postal_addresses: list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphPhysicalAddress]
    :param spouse_name: The name of the contact's spouse/partner.
    :type spouse_name: str
    :param personal_notes: The user's notes about the contact.
    :type personal_notes: str
    :param children: The names of the contact's children.
    :type children: list[str]
    :param wedding_anniversary:
    :type wedding_anniversary: ~datetime.date
    :param gender:
    :type gender: str
    :param is_favorite:
    :type is_favorite: bool
    :param flag: followupFlag.
    :type flag: ~Microsoft.Graph.PowerShell.models.MicrosoftGraphFollowupFlag
    :param single_value_extended_properties: The collection of single-value extended properties
     defined for the contact. Read-only. Nullable.
    :type single_value_extended_properties:
     list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphSingleValueLegacyExtendedProperty]
    :param multi_value_extended_properties: The collection of multi-value extended properties
     defined for the contact. Read-only. Nullable.
    :type multi_value_extended_properties:
     list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphMultiValueLegacyExtendedProperty]
    :param photo: profilePhoto.
    :type photo: ~Microsoft.Graph.PowerShell.models.MicrosoftGraphProfilePhoto
    :param extensions: The collection of open extensions defined for the contact. Read-only.
     Nullable.
    :type extensions: list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphEntity]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'created_date_time': {'key': 'createdDateTime', 'type': 'iso-8601'},
        'last_modified_date_time': {'key': 'lastModifiedDateTime', 'type': 'iso-8601'},
        'change_key': {'key': 'changeKey', 'type': 'str'},
        'categories': {'key': 'categories', 'type': '[str]'},
        'parent_folder_id': {'key': 'parentFolderId', 'type': 'str'},
        'birthday': {'key': 'birthday', 'type': 'iso-8601'},
        'file_as': {'key': 'fileAs', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'given_name': {'key': 'givenName', 'type': 'str'},
        'initials': {'key': 'initials', 'type': 'str'},
        'middle_name': {'key': 'middleName', 'type': 'str'},
        'nick_name': {'key': 'nickName', 'type': 'str'},
        'surname': {'key': 'surname', 'type': 'str'},
        'title': {'key': 'title', 'type': 'str'},
        'yomi_given_name': {'key': 'yomiGivenName', 'type': 'str'},
        'yomi_surname': {'key': 'yomiSurname', 'type': 'str'},
        'yomi_company_name': {'key': 'yomiCompanyName', 'type': 'str'},
        'generation': {'key': 'generation', 'type': 'str'},
        'email_addresses': {'key': 'emailAddresses', 'type': '[MicrosoftGraphTypedEmailAddress]'},
        'websites': {'key': 'websites', 'type': '[MicrosoftGraphWebsite]'},
        'im_addresses': {'key': 'imAddresses', 'type': '[str]'},
        'job_title': {'key': 'jobTitle', 'type': 'str'},
        'company_name': {'key': 'companyName', 'type': 'str'},
        'department': {'key': 'department', 'type': 'str'},
        'office_location': {'key': 'officeLocation', 'type': 'str'},
        'profession': {'key': 'profession', 'type': 'str'},
        'assistant_name': {'key': 'assistantName', 'type': 'str'},
        'manager': {'key': 'manager', 'type': 'str'},
        'phones': {'key': 'phones', 'type': '[MicrosoftGraphPhone]'},
        'postal_addresses': {'key': 'postalAddresses', 'type': '[MicrosoftGraphPhysicalAddress]'},
        'spouse_name': {'key': 'spouseName', 'type': 'str'},
        'personal_notes': {'key': 'personalNotes', 'type': 'str'},
        'children': {'key': 'children', 'type': '[str]'},
        'wedding_anniversary': {'key': 'weddingAnniversary', 'type': 'date'},
        'gender': {'key': 'gender', 'type': 'str'},
        'is_favorite': {'key': 'isFavorite', 'type': 'bool'},
        'flag': {'key': 'flag', 'type': 'MicrosoftGraphFollowupFlag'},
        'single_value_extended_properties': {'key': 'singleValueExtendedProperties', 'type': '[MicrosoftGraphSingleValueLegacyExtendedProperty]'},
        'multi_value_extended_properties': {'key': 'multiValueExtendedProperties', 'type': '[MicrosoftGraphMultiValueLegacyExtendedProperty]'},
        'photo': {'key': 'photo', 'type': 'MicrosoftGraphProfilePhoto'},
        'extensions': {'key': 'extensions', 'type': '[MicrosoftGraphEntity]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphContact, self).__init__(**kwargs)
        self.parent_folder_id = kwargs.get('parent_folder_id', None)
        self.birthday = kwargs.get('birthday', None)
        self.file_as = kwargs.get('file_as', None)
        self.display_name = kwargs.get('display_name', None)
        self.given_name = kwargs.get('given_name', None)
        self.initials = kwargs.get('initials', None)
        self.middle_name = kwargs.get('middle_name', None)
        self.nick_name = kwargs.get('nick_name', None)
        self.surname = kwargs.get('surname', None)
        self.title = kwargs.get('title', None)
        self.yomi_given_name = kwargs.get('yomi_given_name', None)
        self.yomi_surname = kwargs.get('yomi_surname', None)
        self.yomi_company_name = kwargs.get('yomi_company_name', None)
        self.generation = kwargs.get('generation', None)
        self.email_addresses = kwargs.get('email_addresses', None)
        self.websites = kwargs.get('websites', None)
        self.im_addresses = kwargs.get('im_addresses', None)
        self.job_title = kwargs.get('job_title', None)
        self.company_name = kwargs.get('company_name', None)
        self.department = kwargs.get('department', None)
        self.office_location = kwargs.get('office_location', None)
        self.profession = kwargs.get('profession', None)
        self.assistant_name = kwargs.get('assistant_name', None)
        self.manager = kwargs.get('manager', None)
        self.phones = kwargs.get('phones', None)
        self.postal_addresses = kwargs.get('postal_addresses', None)
        self.spouse_name = kwargs.get('spouse_name', None)
        self.personal_notes = kwargs.get('personal_notes', None)
        self.children = kwargs.get('children', None)
        self.wedding_anniversary = kwargs.get('wedding_anniversary', None)
        self.gender = kwargs.get('gender', None)
        self.is_favorite = kwargs.get('is_favorite', None)
        self.flag = kwargs.get('flag', None)
        self.single_value_extended_properties = kwargs.get('single_value_extended_properties', None)
        self.multi_value_extended_properties = kwargs.get('multi_value_extended_properties', None)
        self.photo = kwargs.get('photo', None)
        self.extensions = kwargs.get('extensions', None)


class MicrosoftGraphContactFolder(MicrosoftGraphEntity):
    """contactFolder.

    :param id: Read-only.
    :type id: str
    :param parent_folder_id: The ID of the folder's parent folder.
    :type parent_folder_id: str
    :param display_name: The folder's display name.
    :type display_name: str
    :param well_known_name:
    :type well_known_name: str
    :param single_value_extended_properties: The collection of single-value extended properties
     defined for the contactFolder. Read-only. Nullable.
    :type single_value_extended_properties:
     list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphSingleValueLegacyExtendedProperty]
    :param multi_value_extended_properties: The collection of multi-value extended properties
     defined for the contactFolder. Read-only. Nullable.
    :type multi_value_extended_properties:
     list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphMultiValueLegacyExtendedProperty]
    :param contacts: The contacts in the folder. Navigation property. Read-only. Nullable.
    :type contacts: list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphContact]
    :param child_folders: The collection of child folders in the folder. Navigation property. Read-
     only. Nullable.
    :type child_folders: list[~Microsoft.Graph.PowerShell.models.MicrosoftGraphContactFolder]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'parent_folder_id': {'key': 'parentFolderId', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'well_known_name': {'key': 'wellKnownName', 'type': 'str'},
        'single_value_extended_properties': {'key': 'singleValueExtendedProperties', 'type': '[MicrosoftGraphSingleValueLegacyExtendedProperty]'},
        'multi_value_extended_properties': {'key': 'multiValueExtendedProperties', 'type': '[MicrosoftGraphMultiValueLegacyExtendedProperty]'},
        'contacts': {'key': 'contacts', 'type': '[MicrosoftGraphContact]'},
        'child_folders': {'key': 'childFolders', 'type': '[MicrosoftGraphContactFolder]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphContactFolder, self).__init__(**kwargs)
        self.parent_folder_id = kwargs.get('parent_folder_id', None)
        self.display_name = kwargs.get('display_name', None)
        self.well_known_name = kwargs.get('well_known_name', None)
        self.single_value_extended_properties = kwargs.get('single_value_extended_properties', None)
        self.multi_value_extended_properties = kwargs.get('multi_value_extended_properties', None)
        self.contacts = kwargs.get('contacts', None)
        self.child_folders = kwargs.get('child_folders', None)


class MicrosoftGraphDateTimeZone(msrest.serialization.Model):
    """dateTimeTimeZone.

    :param date_time: A single point of time in a combined date and time representation
     ({date}T{time}; for example, 2017-08-29T04:00:00.0000000).
    :type date_time: str
    :param time_zone: Represents a time zone, for example, 'Pacific Standard Time'. See below for
     more possible values.
    :type time_zone: str
    """

    _attribute_map = {
        'date_time': {'key': 'dateTime', 'type': 'str'},
        'time_zone': {'key': 'timeZone', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphDateTimeZone, self).__init__(**kwargs)
        self.date_time = kwargs.get('date_time', None)
        self.time_zone = kwargs.get('time_zone', None)


class MicrosoftGraphEmailAddress(msrest.serialization.Model):
    """emailAddress.

    :param name: The display name of the person or entity.
    :type name: str
    :param address: The email address of the person or entity.
    :type address: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'address': {'key': 'address', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphEmailAddress, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.address = kwargs.get('address', None)


class MicrosoftGraphExtension(MicrosoftGraphEntity):
    """extension.

    :param id: Read-only.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphExtension, self).__init__(**kwargs)


class MicrosoftGraphFollowupFlag(msrest.serialization.Model):
    """followupFlag.

    :param completed_date_time: dateTimeTimeZone.
    :type completed_date_time: ~Microsoft.Graph.PowerShell.models.MicrosoftGraphDateTimeZone
    :param due_date_time: dateTimeTimeZone.
    :type due_date_time: ~Microsoft.Graph.PowerShell.models.MicrosoftGraphDateTimeZone
    :param start_date_time: dateTimeTimeZone.
    :type start_date_time: ~Microsoft.Graph.PowerShell.models.MicrosoftGraphDateTimeZone
    :param flag_status: followupFlagStatus. Possible values include: "notFlagged", "complete",
     "flagged".
    :type flag_status: str or ~Microsoft.Graph.PowerShell.models.MicrosoftGraphFollowupFlagStatus
    """

    _attribute_map = {
        'completed_date_time': {'key': 'completedDateTime', 'type': 'MicrosoftGraphDateTimeZone'},
        'due_date_time': {'key': 'dueDateTime', 'type': 'MicrosoftGraphDateTimeZone'},
        'start_date_time': {'key': 'startDateTime', 'type': 'MicrosoftGraphDateTimeZone'},
        'flag_status': {'key': 'flagStatus', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphFollowupFlag, self).__init__(**kwargs)
        self.completed_date_time = kwargs.get('completed_date_time', None)
        self.due_date_time = kwargs.get('due_date_time', None)
        self.start_date_time = kwargs.get('start_date_time', None)
        self.flag_status = kwargs.get('flag_status', None)


class MicrosoftGraphMultiValueLegacyExtendedProperty(MicrosoftGraphEntity):
    """multiValueLegacyExtendedProperty.

    :param id: Read-only.
    :type id: str
    :param value: A collection of property values.
    :type value: list[str]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'value': {'key': 'value', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphMultiValueLegacyExtendedProperty, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class MicrosoftGraphPhone(msrest.serialization.Model):
    """phone.

    :param type: phoneType. Possible values include: "home", "business", "mobile", "other",
     "assistant", "homeFax", "businessFax", "otherFax", "pager", "radio".
    :type type: str or ~Microsoft.Graph.PowerShell.models.MicrosoftGraphPhoneType
    :param number: The phone number.
    :type number: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'number': {'key': 'number', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphPhone, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.number = kwargs.get('number', None)


class MicrosoftGraphPhysicalAddress(msrest.serialization.Model):
    """physicalAddress.

    :param type: physicalAddressType. Possible values include: "unknown", "home", "business",
     "other".
    :type type: str or ~Microsoft.Graph.PowerShell.models.MicrosoftGraphPhysicalAddressType
    :param post_office_box:
    :type post_office_box: str
    :param street: The street.
    :type street: str
    :param city: The city.
    :type city: str
    :param state: The state.
    :type state: str
    :param country_or_region: The country or region. It's a free-format string value, for example,
     'United States'.
    :type country_or_region: str
    :param postal_code: The postal code.
    :type postal_code: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'post_office_box': {'key': 'postOfficeBox', 'type': 'str'},
        'street': {'key': 'street', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
        'state': {'key': 'state', 'type': 'str'},
        'country_or_region': {'key': 'countryOrRegion', 'type': 'str'},
        'postal_code': {'key': 'postalCode', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphPhysicalAddress, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.post_office_box = kwargs.get('post_office_box', None)
        self.street = kwargs.get('street', None)
        self.city = kwargs.get('city', None)
        self.state = kwargs.get('state', None)
        self.country_or_region = kwargs.get('country_or_region', None)
        self.postal_code = kwargs.get('postal_code', None)


class MicrosoftGraphProfilePhoto(MicrosoftGraphEntity):
    """profilePhoto.

    :param id: Read-only.
    :type id: str
    :param height: The height of the photo. Read-only.
    :type height: int
    :param width: The width of the photo. Read-only.
    :type width: int
    """

    _validation = {
        'height': {'maximum': 2147483647, 'minimum': -2147483648},
        'width': {'maximum': 2147483647, 'minimum': -2147483648},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'height': {'key': 'height', 'type': 'int'},
        'width': {'key': 'width', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphProfilePhoto, self).__init__(**kwargs)
        self.height = kwargs.get('height', None)
        self.width = kwargs.get('width', None)


class MicrosoftGraphSingleValueLegacyExtendedProperty(MicrosoftGraphEntity):
    """singleValueLegacyExtendedProperty.

    :param id: Read-only.
    :type id: str
    :param value: A property value.
    :type value: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphSingleValueLegacyExtendedProperty, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class MicrosoftGraphTypedEmailAddress(MicrosoftGraphEmailAddress):
    """typedEmailAddress.

    :param name: The display name of the person or entity.
    :type name: str
    :param address: The email address of the person or entity.
    :type address: str
    :param type: emailType. Possible values include: "unknown", "work", "personal", "main",
     "other".
    :type type: str or ~Microsoft.Graph.PowerShell.models.MicrosoftGraphEmailType
    :param other_label:
    :type other_label: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'address': {'key': 'address', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'other_label': {'key': 'otherLabel', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphTypedEmailAddress, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.other_label = kwargs.get('other_label', None)


class MicrosoftGraphWebsite(msrest.serialization.Model):
    """website.

    :param type: websiteType. Possible values include: "other", "home", "work", "blog", "profile".
    :type type: str or ~Microsoft.Graph.PowerShell.models.MicrosoftGraphWebsiteType
    :param address: The URL of the website.
    :type address: str
    :param display_name: The display name of the web site.
    :type display_name: str
    """

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'address': {'key': 'address', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(MicrosoftGraphWebsite, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.address = kwargs.get('address', None)
        self.display_name = kwargs.get('display_name', None)


class OdataError(msrest.serialization.Model):
    """OdataError.

    All required parameters must be populated in order to send to Azure.

    :param error: Required.
    :type error: ~Microsoft.Graph.PowerShell.models.OdataErrorMain
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'OdataErrorMain'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OdataError, self).__init__(**kwargs)
        self.error = kwargs['error']


class OdataErrorDetail(msrest.serialization.Model):
    """OdataErrorDetail.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OdataErrorDetail, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)


class OdataErrorMain(msrest.serialization.Model):
    """OdataErrorMain.

    All required parameters must be populated in order to send to Azure.

    :param code: Required.
    :type code: str
    :param message: Required.
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~Microsoft.Graph.PowerShell.models.OdataErrorDetail]
    :param innererror: The structure of this object is service-specific.
    :type innererror: object
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[OdataErrorDetail]'},
        'innererror': {'key': 'innererror', 'type': 'object'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OdataErrorMain, self).__init__(**kwargs)
        self.code = kwargs['code']
        self.message = kwargs['message']
        self.target = kwargs.get('target', None)
        self.details = kwargs.get('details', None)
        self.innererror = kwargs.get('innererror', None)
