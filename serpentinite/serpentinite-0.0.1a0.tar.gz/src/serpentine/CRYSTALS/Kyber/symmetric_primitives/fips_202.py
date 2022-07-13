from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.hashes import SHAKE128, SHAKE256, SHA3_256, SHA3_512


def PRF(s, b):
    digest = hashes.Hash(SHAKE256(256))
    digest.update(s+b)
    return digest.finalize()


def XOF(rho, i, j):
    digest = hashes.Hash(SHAKE128(256))
    digest.update(rho+i+j)
    return digest.finalize()


def H(m):
    digest = hashes.Hash(SHA3_256())
    digest.update(m)
    return digest.finalize()


def G(m):
    digest = hashes.Hash(SHA3_512())
    digest.update(m)
    return digest.finalize()


def KDF(m):
    digest = hashes.Hash(SHAKE256(256))
    digest.update(m)
    return digest.finalize()
