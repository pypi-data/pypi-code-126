"""
Generated using https://signald.org/protocol.json
Version: '0.20.0-7-7d9179fd'
"""

from dataclasses import dataclass, field
import typing as typing_  # avoid conflict with the typing method

from aiosignald.error import SignaldException
from aiosignald.generated import *


class DuplicateMessageError(SignaldException):
    timestamp: int = None
    message: str = None


class UntrustedIdentityError(SignaldException):
    identifier: str = None
    message: str = None
    identity_key: "IdentityKeyv1" = None


class ProtocolInvalidMessageError(SignaldException):
    sender: str = None
    timestamp: int = None
    message: str = None
    sender_device: int = None
    content_hint: int = None
    group_id: str = None


class ProtocolInvalidKeyIdError(SignaldException):
    sender: str = None
    timestamp: int = None
    message: str = None
    sender_device: int = None
    content_hint: int = None
    group_id: str = None


class ProtocolNoSessionError(SignaldException):
    sender: str = None
    timestamp: int = None
    message: str = None
    sender_device: int = None
    content_hint: int = None
    group_id: str = None


class NoSuchAccountError(SignaldException):
    account: str = None
    message: str = None


class ServerNotFoundError(SignaldException):
    uuid: str = None
    message: str = None


class InvalidProxyError(SignaldException):
    message: str = None


class NoSendPermissionError(SignaldException):
    message: str = None


class InvalidAttachmentError(SignaldException):
    filename: str = None
    message: str = None


class InternalError(SignaldException):
    """
    an internal error in signald has occurred. typically these are things that "should never happen" such as issues saving to the local disk, but it is also the default error type and may catch some things that should have their own error type. If you find tht your code is depending on the exception list for any particular behavior, please file an issue so we can pull those errors out to a separate error type: https://gitlab.com/signald/signald/-/issues/new
    """

    exceptions: typing_.List[str] = field(default_factory=list)
    message: str = None


class InvalidRequestError(SignaldException):
    message: str = None


class UnknownGroupError(SignaldException):
    message: str = None


class RateLimitError(SignaldException):
    message: str = None


class InvalidRecipientError(SignaldException):
    message: str = None


class AttachmentTooLargeError(SignaldException):
    filename: str = None
    message: str = None


class AuthorizationFailedError(SignaldException):
    """
    Indicates the server rejected our credentials or a failed group update. Typically means the linked device was removed by the primary device, or that the account was re-registered. For group updates, this can indicate that we lack permissions.
    """

    message: str = None


class SQLError(SignaldException):
    message: str = None


class UnregisteredUserError(SignaldException):
    message: str = None
    e164_number: str = None


class OwnProfileKeyDoesNotExistError(SignaldException):
    message: str = None


class GroupPatchNotAcceptedError(SignaldException):
    """
    Indicates the server rejected our group update. This can be due to errors such as trying to add a user that's already in the group.
    """

    message: str = None


class GroupVerificationError(SignaldException):
    message: str = None


class InvalidGroupStateError(SignaldException):
    message: str = None


class InvalidInviteURIError(SignaldException):
    message: str = None


class GroupNotActiveError(SignaldException):
    message: str = None


class UnsupportedGroupError(SignaldException):
    """
    returned in response to use v1 groups, which are no longer supported
    """

    message: str = None


class InvalidBase64Error(SignaldException):
    message: str = None


class ProofRequiredError(SignaldException):
    token: str = None
    options: typing_.List[str] = field(default_factory=list)
    message: str = None
    retry_after: int = None


class ProfileUnavailableError(SignaldException):
    message: str = None


class NoKnownUUIDError(SignaldException):
    message: str = None


class NoSuchSessionError(SignaldException):
    message: str = None


class UserAlreadyExistsError(SignaldException):
    uuid: str = None
    message: str = None


class ScanTimeoutError(SignaldException):
    message: str = None


class CaptchaRequiredError(SignaldException):
    more: str = None
    message: str = None


class AccountHasNoKeysError(SignaldException):
    message: str = None


class AccountAlreadyVerifiedError(SignaldException):
    message: str = None


class AccountLockedError(SignaldException):
    more: str = None
    message: str = None


class FingerprintVersionMismatchError(SignaldException):
    message: str = None


class UnknownIdentityKeyError(SignaldException):
    message: str = None


class InvalidFingerprintError(SignaldException):
    message: str = None


class InvalidGroupError(SignaldException):
    message: str = None


class GroupLinkNotActiveError(SignaldException):
    message: str = None
