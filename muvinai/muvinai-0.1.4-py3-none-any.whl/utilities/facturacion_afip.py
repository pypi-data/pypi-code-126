from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID

def generateKey(cuit:str,bits:int=2048,save_file=False):
    """ Funcion para generar una private key con python

    :param cuit: CUIT a generar la PK
    :type cuit: int
    :param bits: Bits de la clave privada (2048 por default)
    :type bits: int
    :param type_pk: tipo de clave, por default TYPE_RSA
    :type type_pk: crypto Type
    :param save_file: si se desea guardar la clave en un archivo, False por default
    :type save_file: boolean
    :return: key
    :rtype: Key de PyOpenSSL

    """

    pk = rsa.generate_private_key(public_exponent=65537, key_size=bits, backend=default_backend)
    
    if save_file:
        keyfile = 'pk_' + cuit + '.key'
        f = open(keyfile, "wb")
        pk_byte = pk.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        f.write(pk_byte)
        f.close()

    return pk

def generateCSR(cuit:str,razon_social:str,key,save_file=False):
    """ Funcion para generar el CSR

    :param cuit: CUIT a generar la PK
    :type cuit: int
    :param razon_social: Razon social del facturante
    :type razon_social: str
    :param save_file: si se desea guardar el certificado en un archivo, False por default
    :type save_file: boolean
    :return: CSR
    :rtype: string

    """
    
    CSR = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
        x509.NameAttribute(NameOID.COMMON_NAME, "muvi_facturacion"),
        x509.NameAttribute(NameOID.COUNTRY_NAME, "AR"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, razon_social),
        x509.NameAttribute(NameOID.SERIAL_NUMBER, "CUIT" + cuit)
    ])).sign(key, hashes.SHA256())
    
    if save_file:
        csrfile = f'cert_{str(cuit)}.csr'
        f = open(csrfile, "wb")
        f.write(CSR.public_bytes(serialization.Encoding.PEM))
        f.close()
    return CSR