# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

try:
    from ._models_py3 import CollectionOfContact
    from ._models_py3 import CollectionOfContact0
    from ._models_py3 import CollectionOfContactFolder
    from ._models_py3 import CollectionOfContactFolder0
    from ._models_py3 import CollectionOfExtension
    from ._models_py3 import CollectionOfExtension0
    from ._models_py3 import CollectionOfMultiValueLegacyExtendedProperty
    from ._models_py3 import CollectionOfMultiValueLegacyExtendedProperty0
    from ._models_py3 import CollectionOfMultiValueLegacyExtendedProperty1
    from ._models_py3 import CollectionOfSingleValueLegacyExtendedProperty
    from ._models_py3 import CollectionOfSingleValueLegacyExtendedProperty0
    from ._models_py3 import CollectionOfSingleValueLegacyExtendedProperty1
    from ._models_py3 import MicrosoftGraphContact
    from ._models_py3 import MicrosoftGraphContactFolder
    from ._models_py3 import MicrosoftGraphEmailAddress
    from ._models_py3 import MicrosoftGraphEntity
    from ._models_py3 import MicrosoftGraphExtension
    from ._models_py3 import MicrosoftGraphMultiValueLegacyExtendedProperty
    from ._models_py3 import MicrosoftGraphOutlookItem
    from ._models_py3 import MicrosoftGraphPhysicalAddress
    from ._models_py3 import MicrosoftGraphProfilePhoto
    from ._models_py3 import MicrosoftGraphSingleValueLegacyExtendedProperty
    from ._models_py3 import OdataError
    from ._models_py3 import OdataErrorDetail
    from ._models_py3 import OdataErrorMain
except (SyntaxError, ImportError):
    from ._models import CollectionOfContact  # type: ignore
    from ._models import CollectionOfContact0  # type: ignore
    from ._models import CollectionOfContactFolder  # type: ignore
    from ._models import CollectionOfContactFolder0  # type: ignore
    from ._models import CollectionOfExtension  # type: ignore
    from ._models import CollectionOfExtension0  # type: ignore
    from ._models import CollectionOfMultiValueLegacyExtendedProperty  # type: ignore
    from ._models import CollectionOfMultiValueLegacyExtendedProperty0  # type: ignore
    from ._models import CollectionOfMultiValueLegacyExtendedProperty1  # type: ignore
    from ._models import CollectionOfSingleValueLegacyExtendedProperty  # type: ignore
    from ._models import CollectionOfSingleValueLegacyExtendedProperty0  # type: ignore
    from ._models import CollectionOfSingleValueLegacyExtendedProperty1  # type: ignore
    from ._models import MicrosoftGraphContact  # type: ignore
    from ._models import MicrosoftGraphContactFolder  # type: ignore
    from ._models import MicrosoftGraphEmailAddress  # type: ignore
    from ._models import MicrosoftGraphEntity  # type: ignore
    from ._models import MicrosoftGraphExtension  # type: ignore
    from ._models import MicrosoftGraphMultiValueLegacyExtendedProperty  # type: ignore
    from ._models import MicrosoftGraphOutlookItem  # type: ignore
    from ._models import MicrosoftGraphPhysicalAddress  # type: ignore
    from ._models import MicrosoftGraphProfilePhoto  # type: ignore
    from ._models import MicrosoftGraphSingleValueLegacyExtendedProperty  # type: ignore
    from ._models import OdataError  # type: ignore
    from ._models import OdataErrorDetail  # type: ignore
    from ._models import OdataErrorMain  # type: ignore

from ._personal_contacts_enums import (
    Enum10,
    Enum11,
    Enum12,
    Enum13,
    Enum14,
    Enum15,
    Enum16,
    Enum17,
    Enum18,
    Enum19,
    Enum20,
    Enum21,
    Enum22,
    Enum23,
    Enum24,
    Enum25,
    Enum26,
    Enum27,
    Enum28,
    Enum29,
    Enum30,
    Enum31,
    Enum32,
    Enum33,
    Enum34,
    Enum35,
    Enum36,
    Enum37,
    Enum38,
    Enum39,
    Enum40,
    Enum41,
    Enum5,
    Enum6,
    Enum8,
    Get2ItemsItem,
    Get3ItemsItem,
    Get4ItemsItem,
    Get6ItemsItem,
    Get7ItemsItem,
    Get8ItemsItem,
    Get9ItemsItem,
)

__all__ = [
    'CollectionOfContact',
    'CollectionOfContact0',
    'CollectionOfContactFolder',
    'CollectionOfContactFolder0',
    'CollectionOfExtension',
    'CollectionOfExtension0',
    'CollectionOfMultiValueLegacyExtendedProperty',
    'CollectionOfMultiValueLegacyExtendedProperty0',
    'CollectionOfMultiValueLegacyExtendedProperty1',
    'CollectionOfSingleValueLegacyExtendedProperty',
    'CollectionOfSingleValueLegacyExtendedProperty0',
    'CollectionOfSingleValueLegacyExtendedProperty1',
    'MicrosoftGraphContact',
    'MicrosoftGraphContactFolder',
    'MicrosoftGraphEmailAddress',
    'MicrosoftGraphEntity',
    'MicrosoftGraphExtension',
    'MicrosoftGraphMultiValueLegacyExtendedProperty',
    'MicrosoftGraphOutlookItem',
    'MicrosoftGraphPhysicalAddress',
    'MicrosoftGraphProfilePhoto',
    'MicrosoftGraphSingleValueLegacyExtendedProperty',
    'OdataError',
    'OdataErrorDetail',
    'OdataErrorMain',
    'Enum10',
    'Enum11',
    'Enum12',
    'Enum13',
    'Enum14',
    'Enum15',
    'Enum16',
    'Enum17',
    'Enum18',
    'Enum19',
    'Enum20',
    'Enum21',
    'Enum22',
    'Enum23',
    'Enum24',
    'Enum25',
    'Enum26',
    'Enum27',
    'Enum28',
    'Enum29',
    'Enum30',
    'Enum31',
    'Enum32',
    'Enum33',
    'Enum34',
    'Enum35',
    'Enum36',
    'Enum37',
    'Enum38',
    'Enum39',
    'Enum40',
    'Enum41',
    'Enum5',
    'Enum6',
    'Enum8',
    'Get2ItemsItem',
    'Get3ItemsItem',
    'Get4ItemsItem',
    'Get6ItemsItem',
    'Get7ItemsItem',
    'Get8ItemsItem',
    'Get9ItemsItem',
]
