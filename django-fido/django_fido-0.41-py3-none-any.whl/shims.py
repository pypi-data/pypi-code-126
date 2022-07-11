"""Compatibility shims for older versions."""
try:
    from fido2.webauthn import AttestationObject
except ImportError:
    from fido2.ctap2 import AttestationObject


def AttestationObjectFactory():
    """Create AttestationObject fixed so it works with both versions of the library."""

    class DFAttestationObject(AttestationObject):
        pass

    if hasattr(DFAttestationObject, 'att_stmt'):
        DFAttestationObject.att_stmt = property(lambda x: getattr(x, 'att_stmt'))
    else:
        DFAttestationObject.att_stmt = property(lambda x: getattr(x, 'att_statement'))
    return DFAttestationObject


DFAttestationObject = AttestationObjectFactory()
