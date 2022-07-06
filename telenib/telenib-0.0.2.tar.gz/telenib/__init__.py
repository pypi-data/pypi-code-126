from enum import Enum
from gzip import GzipFile
from typing import Tuple
from nibabel import Nifti1Header, Nifti2Header

from .util import PartialBuffer, probe
from .exceptions import NotNiftiException

__version__="0.0.2"

NIFTI1_MAGIC_BYTES = 348
NIFTI2_MAGIC_BYTES = 540


class Endianness(Enum):
    LITTLE = 'little'
    BIG = 'big'


class NiftiTypes(Enum):
    NIFTI1 = 1
    NIFTI2 = 2


def check_bytes_magic(b: bytes) -> Tuple[Endianness, NiftiTypes]:

    magic_number = int.from_bytes(b[0:4], "little")
    if magic_number == NIFTI1_MAGIC_BYTES:
        return (Endianness.LITTLE, NiftiTypes.NIFTI1)
    if magic_number == NIFTI2_MAGIC_BYTES:
        return (Endianness.LITTLE, NiftiTypes.NIFTI2)

    magic_number = int.from_bytes(b[0:4], "big")
    if magic_number == NIFTI1_MAGIC_BYTES:
        return (Endianness.BIG, NiftiTypes.NIFTI1)
    if magic_number == NIFTI2_MAGIC_BYTES:
        return (Endianness.BIG, NiftiTypes.NIFTI2)
    
    raise NotNiftiException


def byte_to_header(b: bytes, endianness: Endianness, nifti_type: NiftiTypes) -> Nifti1Header:
    header_cls = None
    offset = None
    if nifti_type == NiftiTypes.NIFTI1:
        header_cls = Nifti1Header
        offset = NIFTI1_MAGIC_BYTES
    if nifti_type == NiftiTypes.NIFTI2:
        header_cls = Nifti2Header
        offset = NIFTI2_MAGIC_BYTES
    if header_cls is None:
        raise RuntimeError
    return header_cls(b[0:offset], endianness.value)
    


def get_nii_header(url: str, headers=None) -> Nifti1Header:
    output = probe(url, (0, 600), headers)
    try:
        endianness, niftitype = check_bytes_magic(output)
        return byte_to_header(output, endianness, niftitype)
    except NotNiftiException as e:
        pass

    partial_buffer = PartialBuffer(url, headers)
    fh = GzipFile(fileobj=partial_buffer)
    output = fh.peek(600)
    fh.close()

    endianness, niftitype = check_bytes_magic(output)
    return byte_to_header(output, endianness, niftitype)
