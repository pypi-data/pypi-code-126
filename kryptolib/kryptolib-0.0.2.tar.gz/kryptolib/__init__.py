from .EdDSA import *

def krypto_obj(name):
    if name == "Ed25519": return Ed25519
    if name == "Ed25519ctx": return Ed25519ctx
    if name == "Ed25519ph": return Ed25519ph
    if name == "Ed448": return Ed448
    if name == "Ed448ph": return Ed448ph
    raise NotImplementedError("Algorithm not implemented")