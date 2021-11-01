# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.core.exceptions import HttpResponseError
import msrest.serialization


class CheckNameAvailabilityInput(msrest.serialization.Model):
    """Input of CheckNameAvailability API.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The resource name to validate.
    :type name: str
    :param type: Required. The type of resource. Possible values include:
     "Microsoft.Support/supportTickets", "Microsoft.Support/communications".
    :type type: str or ~azure.mgmt.support.models.Type
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CheckNameAvailabilityInput, self).__init__(**kwargs)
        self.name = kwargs['name']
        self.type = kwargs['type']


class CheckNameAvailabilityOutput(msrest.serialization.Model):
    """Output of check name availability API.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name_available: Indicates whether the name is available.
    :vartype name_available: bool
    :ivar reason: The reason why the name is not available.
    :vartype reason: str
    :ivar message: The detailed error message describing why the name is not available.
    :vartype message: str
    """

    _validation = {
        'name_available': {'readonly': True},
        'reason': {'readonly': True},
        'message': {'readonly': True},
    }

    _attribute_map = {
        'name_available': {'key': 'nameAvailable', 'type': 'bool'},
        'reason': {'key': 'reason', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CheckNameAvailabilityOutput, self).__init__(**kwargs)
        self.name_available = None
        self.reason = None
        self.message = None


class CommunicationDetails(msrest.serialization.Model):
    """Object that represents a Communication resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Id of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of the resource 'Microsoft.Support/communications'.
    :vartype type: str
    :ivar communication_type: Communication type. Possible values include: "web", "phone".
    :vartype communication_type: str or ~azure.mgmt.support.models.CommunicationType
    :ivar communication_direction: Direction of communication. Possible values include: "inbound",
     "outbound".
    :vartype communication_direction: str or ~azure.mgmt.support.models.CommunicationDirection
    :param sender: Email address of the sender. This property is required if called by a service
     principal.
    :type sender: str
    :param subject: Subject of the communication.
    :type subject: str
    :param body: Body of the communication.
    :type body: str
    :ivar created_date: Time in UTC (ISO 8601 format) when the communication was created.
    :vartype created_date: ~datetime.datetime
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'communication_type': {'readonly': True},
        'communication_direction': {'readonly': True},
        'created_date': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'communication_type': {'key': 'properties.communicationType', 'type': 'str'},
        'communication_direction': {'key': 'properties.communicationDirection', 'type': 'str'},
        'sender': {'key': 'properties.sender', 'type': 'str'},
        'subject': {'key': 'properties.subject', 'type': 'str'},
        'body': {'key': 'properties.body', 'type': 'str'},
        'created_date': {'key': 'properties.createdDate', 'type': 'iso-8601'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CommunicationDetails, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.communication_type = None
        self.communication_direction = None
        self.sender = kwargs.get('sender', None)
        self.subject = kwargs.get('subject', None)
        self.body = kwargs.get('body', None)
        self.created_date = None


class CommunicationsListResult(msrest.serialization.Model):
    """Collection of Communication resources.

    :param value: List of Communication resources.
    :type value: list[~azure.mgmt.support.models.CommunicationDetails]
    :param next_link: The URI to fetch the next page of Communication resources.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[CommunicationDetails]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(CommunicationsListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class ContactProfile(msrest.serialization.Model):
    """Contact information associated with the support ticket.

    All required parameters must be populated in order to send to Azure.

    :param first_name: Required. First name.
    :type first_name: str
    :param last_name: Required. Last name.
    :type last_name: str
    :param preferred_contact_method: Required. Preferred contact method. Possible values include:
     "email", "phone".
    :type preferred_contact_method: str or ~azure.mgmt.support.models.PreferredContactMethod
    :param primary_email_address: Required. Primary email address.
    :type primary_email_address: str
    :param additional_email_addresses: Additional email addresses listed will be copied on any
     correspondence about the support ticket.
    :type additional_email_addresses: list[str]
    :param phone_number: Phone number. This is required if preferred contact method is phone.
    :type phone_number: str
    :param preferred_time_zone: Required. Time zone of the user. This is the name of the time zone
     from `Microsoft Time Zone Index Values <https://support.microsoft.com/help/973627/microsoft-
     time-zone-index-values>`_.
    :type preferred_time_zone: str
    :param country: Required. Country of the user. This is the ISO 3166-1 alpha-3 code.
    :type country: str
    :param preferred_support_language: Required. Preferred language of support from Azure. Support
     languages vary based on the severity you choose for your support ticket. Learn more at `Azure
     Severity and responsiveness <https://azure.microsoft.com/support/plans/response>`_. Use the
     standard language-country code. Valid values are 'en-us' for English, 'zh-hans' for Chinese,
     'es-es' for Spanish, 'fr-fr' for French, 'ja-jp' for Japanese, 'ko-kr' for Korean, 'ru-ru' for
     Russian, 'pt-br' for Portuguese, 'it-it' for Italian, 'zh-tw' for Chinese and 'de-de' for
     German.
    :type preferred_support_language: str
    """

    _validation = {
        'first_name': {'required': True},
        'last_name': {'required': True},
        'preferred_contact_method': {'required': True},
        'primary_email_address': {'required': True},
        'preferred_time_zone': {'required': True},
        'country': {'required': True},
        'preferred_support_language': {'required': True},
    }

    _attribute_map = {
        'first_name': {'key': 'firstName', 'type': 'str'},
        'last_name': {'key': 'lastName', 'type': 'str'},
        'preferred_contact_method': {'key': 'preferredContactMethod', 'type': 'str'},
        'primary_email_address': {'key': 'primaryEmailAddress', 'type': 'str'},
        'additional_email_addresses': {'key': 'additionalEmailAddresses', 'type': '[str]'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
        'preferred_time_zone': {'key': 'preferredTimeZone', 'type': 'str'},
        'country': {'key': 'country', 'type': 'str'},
        'preferred_support_language': {'key': 'preferredSupportLanguage', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ContactProfile, self).__init__(**kwargs)
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.preferred_contact_method = kwargs['preferred_contact_method']
        self.primary_email_address = kwargs['primary_email_address']
        self.additional_email_addresses = kwargs.get('additional_email_addresses', None)
        self.phone_number = kwargs.get('phone_number', None)
        self.preferred_time_zone = kwargs['preferred_time_zone']
        self.country = kwargs['country']
        self.preferred_support_language = kwargs['preferred_support_language']


class ExceptionResponse(msrest.serialization.Model):
    """The API error.

    :param error: The API error details.
    :type error: ~azure.mgmt.support.models.ServiceError
    """

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ServiceError'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ExceptionResponse, self).__init__(**kwargs)
        self.error = kwargs.get('error', None)


class Operation(msrest.serialization.Model):
    """The operation supported by Microsoft Support resource provider.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: Operation name: {provider}/{resource}/{operation}.
    :vartype name: str
    :param display: The object that describes the operation.
    :type display: ~azure.mgmt.support.models.OperationDisplay
    """

    _validation = {
        'name': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display': {'key': 'display', 'type': 'OperationDisplay'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Operation, self).__init__(**kwargs)
        self.name = None
        self.display = kwargs.get('display', None)


class OperationDisplay(msrest.serialization.Model):
    """The object that describes the operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar description: The description of the operation.
    :vartype description: str
    :ivar operation: The action that users can perform, based on their permission level.
    :vartype operation: str
    :ivar provider: Service provider: Microsoft Support.
    :vartype provider: str
    :ivar resource: Resource on which the operation is performed.
    :vartype resource: str
    """

    _validation = {
        'description': {'readonly': True},
        'operation': {'readonly': True},
        'provider': {'readonly': True},
        'resource': {'readonly': True},
    }

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'operation': {'key': 'operation', 'type': 'str'},
        'provider': {'key': 'provider', 'type': 'str'},
        'resource': {'key': 'resource', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationDisplay, self).__init__(**kwargs)
        self.description = None
        self.operation = None
        self.provider = None
        self.resource = None


class OperationsListResult(msrest.serialization.Model):
    """The list of operations supported by Microsoft Support resource provider.

    :param value: The list of operations supported by Microsoft Support resource provider.
    :type value: list[~azure.mgmt.support.models.Operation]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Operation]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(OperationsListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class ProblemClassification(msrest.serialization.Model):
    """ProblemClassification resource object.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Id of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of the resource 'Microsoft.Support/problemClassification'.
    :vartype type: str
    :param display_name: Localized name of problem classification.
    :type display_name: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProblemClassification, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.display_name = kwargs.get('display_name', None)


class ProblemClassificationsListResult(msrest.serialization.Model):
    """Collection of ProblemClassification resources.

    :param value: List of ProblemClassification resources.
    :type value: list[~azure.mgmt.support.models.ProblemClassification]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[ProblemClassification]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ProblemClassificationsListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class QuotaChangeRequest(msrest.serialization.Model):
    """This property is required for providing the region and new quota limits.

    :param region: Region for which the quota increase request is being made.
    :type region: str
    :param payload: Payload of the quota increase request.
    :type payload: str
    """

    _attribute_map = {
        'region': {'key': 'region', 'type': 'str'},
        'payload': {'key': 'payload', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QuotaChangeRequest, self).__init__(**kwargs)
        self.region = kwargs.get('region', None)
        self.payload = kwargs.get('payload', None)


class QuotaTicketDetails(msrest.serialization.Model):
    """Additional set of information required for quota increase support ticket for certain quota types, e.g.: Virtual machine cores. Get complete details about Quota payload support request along with examples at `Support quota request <https://aka.ms/supportrpquotarequestpayload>`_.

    :param quota_change_request_sub_type: Required for certain quota types when there is a sub
     type, such as Batch, for which you are requesting a quota increase.
    :type quota_change_request_sub_type: str
    :param quota_change_request_version: Quota change request version.
    :type quota_change_request_version: str
    :param quota_change_requests: This property is required for providing the region and new quota
     limits.
    :type quota_change_requests: list[~azure.mgmt.support.models.QuotaChangeRequest]
    """

    _attribute_map = {
        'quota_change_request_sub_type': {'key': 'quotaChangeRequestSubType', 'type': 'str'},
        'quota_change_request_version': {'key': 'quotaChangeRequestVersion', 'type': 'str'},
        'quota_change_requests': {'key': 'quotaChangeRequests', 'type': '[QuotaChangeRequest]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(QuotaTicketDetails, self).__init__(**kwargs)
        self.quota_change_request_sub_type = kwargs.get('quota_change_request_sub_type', None)
        self.quota_change_request_version = kwargs.get('quota_change_request_version', None)
        self.quota_change_requests = kwargs.get('quota_change_requests', None)


class Service(msrest.serialization.Model):
    """Object that represents a Service resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Id of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of the resource 'Microsoft.Support/services'.
    :vartype type: str
    :param display_name: Localized name of the Azure service.
    :type display_name: str
    :param resource_types: ARM Resource types.
    :type resource_types: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'resource_types': {'key': 'properties.resourceTypes', 'type': '[str]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(Service, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.display_name = kwargs.get('display_name', None)
        self.resource_types = kwargs.get('resource_types', None)


class ServiceError(msrest.serialization.Model):
    """The API error details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :param code: The error code.
    :type code: str
    :param message: The error message.
    :type message: str
    :param target: The target of the error.
    :type target: str
    :ivar details: The list of error details.
    :vartype details: list[~azure.mgmt.support.models.ServiceErrorDetail]
    """

    _validation = {
        'details': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[ServiceErrorDetail]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ServiceError, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.target = kwargs.get('target', None)
        self.details = None


class ServiceErrorDetail(msrest.serialization.Model):
    """The error details.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :param target: The target of the error.
    :type target: str
    """

    _validation = {
        'code': {'readonly': True},
        'message': {'readonly': True},
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
        super(ServiceErrorDetail, self).__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = kwargs.get('target', None)


class ServiceLevelAgreement(msrest.serialization.Model):
    """Service Level Agreement details for a support ticket.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar start_time: Time in UTC (ISO 8601 format) when the service level agreement starts.
    :vartype start_time: ~datetime.datetime
    :ivar expiration_time: Time in UTC (ISO 8601 format) when the service level agreement expires.
    :vartype expiration_time: ~datetime.datetime
    :ivar sla_minutes: Service Level Agreement in minutes.
    :vartype sla_minutes: int
    """

    _validation = {
        'start_time': {'readonly': True},
        'expiration_time': {'readonly': True},
        'sla_minutes': {'readonly': True},
    }

    _attribute_map = {
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'expiration_time': {'key': 'expirationTime', 'type': 'iso-8601'},
        'sla_minutes': {'key': 'slaMinutes', 'type': 'int'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ServiceLevelAgreement, self).__init__(**kwargs)
        self.start_time = None
        self.expiration_time = None
        self.sla_minutes = None


class ServicesListResult(msrest.serialization.Model):
    """Collection of Service resources.

    :param value: List of Service resources.
    :type value: list[~azure.mgmt.support.models.Service]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Service]'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(ServicesListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)


class SupportEngineer(msrest.serialization.Model):
    """Support engineer information.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar email_address: Email address of the Azure Support engineer assigned to the support
     ticket.
    :vartype email_address: str
    """

    _validation = {
        'email_address': {'readonly': True},
    }

    _attribute_map = {
        'email_address': {'key': 'emailAddress', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SupportEngineer, self).__init__(**kwargs)
        self.email_address = None


class SupportTicketDetails(msrest.serialization.Model):
    """Object that represents SupportTicketDetails resource.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Id of the resource.
    :vartype id: str
    :ivar name: Name of the resource.
    :vartype name: str
    :ivar type: Type of the resource 'Microsoft.Support/supportTickets'.
    :vartype type: str
    :param support_ticket_id: System generated support ticket Id that is unique.
    :type support_ticket_id: str
    :param description: Detailed description of the question or issue.
    :type description: str
    :param problem_classification_id: Each Azure service has its own set of issue categories, also
     known as problem classification. This parameter is the unique Id for the type of problem you
     are experiencing.
    :type problem_classification_id: str
    :ivar problem_classification_display_name: Localized name of problem classification.
    :vartype problem_classification_display_name: str
    :param severity: A value that indicates the urgency of the case, which in turn determines the
     response time according to the service level agreement of the technical support plan you have
     with Azure. Note: 'Highest critical impact', also known as the 'Emergency - Severe impact'
     level in the Azure portal is reserved only for our Premium customers. Possible values include:
     "minimal", "moderate", "critical", "highestcriticalimpact".
    :type severity: str or ~azure.mgmt.support.models.SeverityLevel
    :ivar enrollment_id: Enrollment Id associated with the support ticket.
    :vartype enrollment_id: str
    :param require24_x7_response: Indicates if this requires a 24x7 response from Azure.
    :type require24_x7_response: bool
    :param contact_details: Contact information of the user requesting to create a support ticket.
    :type contact_details: ~azure.mgmt.support.models.ContactProfile
    :param service_level_agreement: Service Level Agreement information for this support ticket.
    :type service_level_agreement: ~azure.mgmt.support.models.ServiceLevelAgreement
    :param support_engineer: Information about the support engineer working on this support ticket.
    :type support_engineer: ~azure.mgmt.support.models.SupportEngineer
    :ivar support_plan_type: Support plan type associated with the support ticket.
    :vartype support_plan_type: str
    :param title: Title of the support ticket.
    :type title: str
    :param problem_start_time: Time in UTC (ISO 8601 format) when the problem started.
    :type problem_start_time: ~datetime.datetime
    :param service_id: This is the resource Id of the Azure service resource associated with the
     support ticket.
    :type service_id: str
    :ivar service_display_name: Localized name of the Azure service.
    :vartype service_display_name: str
    :ivar status: Status of the support ticket.
    :vartype status: str
    :ivar created_date: Time in UTC (ISO 8601 format) when the support ticket was created.
    :vartype created_date: ~datetime.datetime
    :ivar modified_date: Time in UTC (ISO 8601 format) when the support ticket was last modified.
    :vartype modified_date: ~datetime.datetime
    :param technical_ticket_details: Additional ticket details associated with a technical support
     ticket request.
    :type technical_ticket_details: ~azure.mgmt.support.models.TechnicalTicketDetails
    :param quota_ticket_details: Additional ticket details associated with a quota support ticket
     request.
    :type quota_ticket_details: ~azure.mgmt.support.models.QuotaTicketDetails
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'problem_classification_display_name': {'readonly': True},
        'enrollment_id': {'readonly': True},
        'support_plan_type': {'readonly': True},
        'service_display_name': {'readonly': True},
        'status': {'readonly': True},
        'created_date': {'readonly': True},
        'modified_date': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'support_ticket_id': {'key': 'properties.supportTicketId', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'problem_classification_id': {'key': 'properties.problemClassificationId', 'type': 'str'},
        'problem_classification_display_name': {'key': 'properties.problemClassificationDisplayName', 'type': 'str'},
        'severity': {'key': 'properties.severity', 'type': 'str'},
        'enrollment_id': {'key': 'properties.enrollmentId', 'type': 'str'},
        'require24_x7_response': {'key': 'properties.require24X7Response', 'type': 'bool'},
        'contact_details': {'key': 'properties.contactDetails', 'type': 'ContactProfile'},
        'service_level_agreement': {'key': 'properties.serviceLevelAgreement', 'type': 'ServiceLevelAgreement'},
        'support_engineer': {'key': 'properties.supportEngineer', 'type': 'SupportEngineer'},
        'support_plan_type': {'key': 'properties.supportPlanType', 'type': 'str'},
        'title': {'key': 'properties.title', 'type': 'str'},
        'problem_start_time': {'key': 'properties.problemStartTime', 'type': 'iso-8601'},
        'service_id': {'key': 'properties.serviceId', 'type': 'str'},
        'service_display_name': {'key': 'properties.serviceDisplayName', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'created_date': {'key': 'properties.createdDate', 'type': 'iso-8601'},
        'modified_date': {'key': 'properties.modifiedDate', 'type': 'iso-8601'},
        'technical_ticket_details': {'key': 'properties.technicalTicketDetails', 'type': 'TechnicalTicketDetails'},
        'quota_ticket_details': {'key': 'properties.quotaTicketDetails', 'type': 'QuotaTicketDetails'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SupportTicketDetails, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.support_ticket_id = kwargs.get('support_ticket_id', None)
        self.description = kwargs.get('description', None)
        self.problem_classification_id = kwargs.get('problem_classification_id', None)
        self.problem_classification_display_name = None
        self.severity = kwargs.get('severity', None)
        self.enrollment_id = None
        self.require24_x7_response = kwargs.get('require24_x7_response', None)
        self.contact_details = kwargs.get('contact_details', None)
        self.service_level_agreement = kwargs.get('service_level_agreement', None)
        self.support_engineer = kwargs.get('support_engineer', None)
        self.support_plan_type = None
        self.title = kwargs.get('title', None)
        self.problem_start_time = kwargs.get('problem_start_time', None)
        self.service_id = kwargs.get('service_id', None)
        self.service_display_name = None
        self.status = None
        self.created_date = None
        self.modified_date = None
        self.technical_ticket_details = kwargs.get('technical_ticket_details', None)
        self.quota_ticket_details = kwargs.get('quota_ticket_details', None)


class SupportTicketsListResult(msrest.serialization.Model):
    """Object that represents a collection of SupportTicket resources.

    :param value: List of SupportTicket resources.
    :type value: list[~azure.mgmt.support.models.SupportTicketDetails]
    :param next_link: The URI to fetch the next page of SupportTicket resources.
    :type next_link: str
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[SupportTicketDetails]'},
        'next_link': {'key': 'nextLink', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(SupportTicketsListResult, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self.next_link = kwargs.get('next_link', None)


class TechnicalTicketDetails(msrest.serialization.Model):
    """Additional information for technical support ticket.

    :param resource_id: This is the resource Id of the Azure service resource (For example: A
     virtual machine resource or an HDInsight resource) for which the support ticket is created.
    :type resource_id: str
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(TechnicalTicketDetails, self).__init__(**kwargs)
        self.resource_id = kwargs.get('resource_id', None)


class UpdateContactProfile(msrest.serialization.Model):
    """Contact information associated with the support ticket.

    :param first_name: First name.
    :type first_name: str
    :param last_name: Last name.
    :type last_name: str
    :param preferred_contact_method: Preferred contact method. Possible values include: "email",
     "phone".
    :type preferred_contact_method: str or ~azure.mgmt.support.models.PreferredContactMethod
    :param primary_email_address: Primary email address.
    :type primary_email_address: str
    :param additional_email_addresses: Email addresses listed will be copied on any correspondence
     about the support ticket.
    :type additional_email_addresses: list[str]
    :param phone_number: Phone number. This is required if preferred contact method is phone.
    :type phone_number: str
    :param preferred_time_zone: Time zone of the user. This is the name of the time zone from
     `Microsoft Time Zone Index Values <https://support.microsoft.com/help/973627/microsoft-time-
     zone-index-values>`_.
    :type preferred_time_zone: str
    :param country: Country of the user. This is the ISO 3166-1 alpha-3 code.
    :type country: str
    :param preferred_support_language: Preferred language of support from Azure. Support languages
     vary based on the severity you choose for your support ticket. Learn more at `Azure Severity
     and responsiveness <https://azure.microsoft.com/support/plans/response/>`_. Use the standard
     language-country code. Valid values are 'en-us' for English, 'zh-hans' for Chinese, 'es-es' for
     Spanish, 'fr-fr' for French, 'ja-jp' for Japanese, 'ko-kr' for Korean, 'ru-ru' for Russian,
     'pt-br' for Portuguese, 'it-it' for Italian, 'zh-tw' for Chinese and 'de-de' for German.
    :type preferred_support_language: str
    """

    _attribute_map = {
        'first_name': {'key': 'firstName', 'type': 'str'},
        'last_name': {'key': 'lastName', 'type': 'str'},
        'preferred_contact_method': {'key': 'preferredContactMethod', 'type': 'str'},
        'primary_email_address': {'key': 'primaryEmailAddress', 'type': 'str'},
        'additional_email_addresses': {'key': 'additionalEmailAddresses', 'type': '[str]'},
        'phone_number': {'key': 'phoneNumber', 'type': 'str'},
        'preferred_time_zone': {'key': 'preferredTimeZone', 'type': 'str'},
        'country': {'key': 'country', 'type': 'str'},
        'preferred_support_language': {'key': 'preferredSupportLanguage', 'type': 'str'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UpdateContactProfile, self).__init__(**kwargs)
        self.first_name = kwargs.get('first_name', None)
        self.last_name = kwargs.get('last_name', None)
        self.preferred_contact_method = kwargs.get('preferred_contact_method', None)
        self.primary_email_address = kwargs.get('primary_email_address', None)
        self.additional_email_addresses = kwargs.get('additional_email_addresses', None)
        self.phone_number = kwargs.get('phone_number', None)
        self.preferred_time_zone = kwargs.get('preferred_time_zone', None)
        self.country = kwargs.get('country', None)
        self.preferred_support_language = kwargs.get('preferred_support_language', None)


class UpdateSupportTicket(msrest.serialization.Model):
    """Updates severity, ticket status, and contact details in the support ticket.

    :param severity: Severity level. Possible values include: "minimal", "moderate", "critical",
     "highestcriticalimpact".
    :type severity: str or ~azure.mgmt.support.models.SeverityLevel
    :param status: Status to be updated on the ticket. Possible values include: "open", "closed".
    :type status: str or ~azure.mgmt.support.models.Status
    :param contact_details: Contact details to be updated on the support ticket.
    :type contact_details: ~azure.mgmt.support.models.UpdateContactProfile
    """

    _attribute_map = {
        'severity': {'key': 'severity', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'contact_details': {'key': 'contactDetails', 'type': 'UpdateContactProfile'},
    }

    def __init__(
        self,
        **kwargs
    ):
        super(UpdateSupportTicket, self).__init__(**kwargs)
        self.severity = kwargs.get('severity', None)
        self.status = kwargs.get('status', None)
        self.contact_details = kwargs.get('contact_details', None)
