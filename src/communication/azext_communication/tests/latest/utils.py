# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.communication.phonenumbers import (
    PhoneNumbersClient,
    PhoneNumberCapabilityType,
    PhoneNumberAssignmentType,
    PhoneNumberType,
    PhoneNumberCapabilities
)
from azure.communication.identity import CommunicationIdentityClient
import uuid, os

TEST_RESOURCE_IDENTIFIER = "sanitized"
TEST_SOURCE_PHONENUMBER_DEFAULT = "sanitized"
TEST_RECIPIENT_PHONENUMBER_DEFAULT = "sanitized"


def get_from_os_environment(env_name, default):
    import os
    return os.environ[env_name] if env_name in os.environ and os.environ[env_name] != "" else default


def get_test_identity_id(is_live, in_recording, connection_str):
    if not is_live and not in_recording:
        return TEST_RESOURCE_IDENTIFIER
    else:
        identity_client = CommunicationIdentityClient.from_connection_string(connection_str)
        user = identity_client.create_user()
        return user.properties['id']


def get_test_source_phonenumber(is_live, in_recording):
    if not is_live and not in_recording:
        return TEST_SOURCE_PHONENUMBER_DEFAULT
    else:
        return get_from_os_environment("AZURE_COMMUNICATION_SOURCE_PHONENUMBER", None)


def get_test_recipient_phonenumber(is_live, in_recording):
    if not is_live and not in_recording:
        return TEST_RECIPIENT_PHONENUMBER_DEFAULT
    else:
        return get_from_os_environment("AZURE_COMMUNICATION_RECIPIENT_PHONENUMBER", None)


def get_new_phonenumber(connection_string):
    try:
        phone_numbers_client = PhoneNumbersClient.from_connection_string(
            connection_string)
        capabilities = PhoneNumberCapabilities(
            calling=PhoneNumberCapabilityType.INBOUND,
            sms=PhoneNumberCapabilityType.INBOUND_OUTBOUND
        )
        search_poller = phone_numbers_client.begin_search_available_phone_numbers(
            "US",
            PhoneNumberType.TOLL_FREE,
            PhoneNumberAssignmentType.APPLICATION,
            capabilities,
            area_code="833",
            polling=True
        )
        search_result = search_poller.result()

        purchase_poller = phone_numbers_client.begin_purchase_phone_numbers(
            search_result.search_id, polling=True)
        purchase_poller.result()
        if(purchase_poller.status() == 'succeeded'):
            phone_number_list = search_result.phone_numbers
            for phone_number in phone_number_list:
                return phone_number

    except Exception as ex:
        return TEST_RECIPIENT_PHONENUMBER_DEFAULT


def _get_content_type(entity):
    # 'headers' is a field of 'request', but it is a dict-key in 'response'
    headers = getattr(entity, 'headers', None)
    if headers is None:
        headers = entity.get('headers')

    content_type = None
    if headers:
        content_type = headers.get('content-type', None)
        if content_type:
            # content-type could an array from response, let us extract it out
            content_type = content_type[0] if isinstance(content_type, list) else content_type
            content_type = content_type.split(";")[0].lower()
    return content_type

    
def is_text_payload(entity):
    text_content_list = ['application/json', 'application/xml', 'text/', 'application/test-content']

    content_type = _get_content_type(entity)
    if content_type:
        return any(content_type.startswith(x) for x in text_content_list)
    return True
