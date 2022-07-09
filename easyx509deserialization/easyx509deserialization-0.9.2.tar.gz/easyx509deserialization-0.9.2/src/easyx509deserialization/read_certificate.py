import cryptography.hazmat.primitives.serialization
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import pkcs7
import os
import sys


def load_cert_object(cert_as_base64_or_der):
    #Pass in a string containing a base 64 certificate
    #or a binary der object
    
    #Returns a cryptography certificate object
    if type(cert_as_base64_or_der) == str:
        cert_bytes = bytes(cert_as_base64_or_der, 'utf-8')
        x509_cert_object = x509.load_pem_x509_certificate(cert_bytes)
    elif type(cert_as_base64_or_der) == bytes:
        x509_cert_object = x509.load_der_x509_certificate(cert_as_base64_or_der)
    else:
        print("Could not convert the object to an x509 certificate object")
        sys.exit(1)
    return x509_cert_object


def convert_cert_object_to_base64(x509_cert_object):
    #Pass in a cryptography x509 certificate object
    #Returns the certificate as a certificate string

    try:
        certificate_bytes = x509_cert_object.public_bytes(cryptography.hazmat.primitives.serialization.Encoding.PEM)
        certificate_string = bytes_to_string(certificate_bytes)
    except:
        print("Unable to convert the object to a string")
        certificate_string = ""

    return certificate_string


def bytes_to_string(bytes_var):
    return bytes_var.decode('utf-8')


def get_subject_name(cert):
    #Returns the subject name as a string

    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    try:
        subject_name = cert_object.subject
        subject_name = subject_name.rfc4514_string()
    except:
        print("Could not identify the subject name.")
        subject_name = ""
    return subject_name


def get_common_name(cert):
    #Returns the common name as a string

    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert
    try:
        common_name_list = cert_object.subject.get_attributes_for_oid(x509.oid.NameOID.COMMON_NAME)
        common_name = common_name_list[0].value

    except:
        print("Could not identify the common name.")
        common_name = ""

    return common_name


def get_serial_number_hex(cert):
    #tested
    #Returns the hex serial number as a string
    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert
    try:
        decimal_serial_number = cert_object.serial_number
        hex_serial_number = hex(decimal_serial_number)
    except:
        print("Could not get the hex serial number from the certificate")
        hex_serial_number = ""
    return str(hex_serial_number)


def get_serial_number_decimal(cert):
    #Tested
    #Returns the decimal serial number as a string

    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert
    try:
        decimal_serial_number = cert_object.serial_number
    except:
        print("Could not get the decimal serial number from the certificate")
        decimal_serial_number = ""

    return str(decimal_serial_number)


def get_valid_from(cert):
    #return a datetime object
    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert
    try:
        valid_from = cert_object.not_valid_before
    except:
        print("Count not get the valid from date from the certificate")
        valid_from = ""
    return valid_from


def get_valid_to(cert):
    #return a datetime object

    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    try:
        valid_to = cert_object.not_valid_after
    except:
        print("Count not get the valid to date from the certificate")
        valid_to = ""

    return valid_to


def get_issuer(cert):
    #return a string
    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    try:
        issuer_name = cert_object.issuer
        issuer_name = issuer_name.rfc4514_string()
    except:
        print("Could not identify the issuer name.")
        issuer_name = ""
    return issuer_name


def get_signature_algorithm(cert):
    #return a string
    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert
    signature_algorithm = cert_object.signature_hash_algorithm.name
    return signature_algorithm


def get_public_key_algorithm(cert):
    #return a string
    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert
    try:
        public_key = cert_object.public_key()
        public_key_algorithm = str(public_key.key_size) + "-bit "

        if isinstance(public_key, cryptography.hazmat.primitives.asymmetric.rsa.RSAPublicKey):
            public_key_algorithm += "RSA key"
        elif isinstance(public_key, cryptography.hazmat.primitives.asymmetric.dsa.DSAPublicKey):
            public_key_algorithm += "DSA key"
        elif isinstance(public_key, cryptography.hazmat.primitives.asymmetric.ec.EllipticCurvePublicKey):
            public_key_algorithm += "Elliptic Curve key"
        elif isinstance(public_key, cryptography.hazmat.primitives.asymmetric.ed25519.Ed25519PublicKey):
            public_key_algorithm += "ED25519 key"
        elif isinstance(public_key, cryptography.hazmat.primitives.asymmetric.ed448.Ed448PublicKey):
            public_key_algorithm += "ED448 key"
        elif isinstance(public_key, cryptography.hazmat.primitives.asymmetric.x25519.X25519PublicKey):
            public_key_algorithm += "X25519 key"
        elif isinstance(public_key, cryptography.hazmat.primitives.asymmetric.x448.X448PublicKey):
            public_key_algorithm += "X448 key"
    except:
        print("Could not get the public key algorithm")
        public_key_algorithm = ""
    return public_key_algorithm


def get_thumbprint_sha1(cert):
    #return a string
    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    thumbprint_as_bytes = cert_object.fingerprint(hashes.SHA1())
    thumbprint = thumbprint_as_bytes.hex()
    return str(thumbprint)


def get_thumbprint_md5(cert):
    #tested
    #return a string
    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    thumbprint_as_bytes = cert_object.fingerprint(hashes.MD5())
    thumbprint = thumbprint_as_bytes.hex()
    return str(thumbprint)


def get_subject_key_identifier(cert):
    #Tested
    #return a string
    #A certificate might not have a subject key identifier

    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    try:
        ski = cert_object.extensions.get_extension_for_oid(x509.oid.ExtensionOID.SUBJECT_KEY_IDENTIFIER)
        subject_key_identifier = str(ski.value.digest.hex())
    except:
        subject_key_identifier = ""
    return subject_key_identifier


def get_authority_key_identifier(cert):
    #Tested
    #return a string
    #A certificate might not have an authority key identifier
    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    try:
        aki = cert_object.extensions.get_extension_for_oid(x509.oid.ExtensionOID.AUTHORITY_KEY_IDENTIFIER)
        authority_key_identifier = str(aki.value.key_identifier.hex())
    except:
        authority_key_identifier = ""
    return authority_key_identifier


def get_crl_list(cert):
    #Tested
    #returns a list of strings
    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    crl_url_list = []

    try:
        crl_ext = cert_object.extensions.get_extension_for_oid(x509.oid.ExtensionOID.CRL_DISTRIBUTION_POINTS)
        for distribution_point in crl_ext.value._distribution_points:
            for full_name in distribution_point._full_name:
                if "http" in full_name._value:
                    crl_url_list.append(full_name._value)
        #for url in crl_url_list:
        #    print ("CRL URL: " + url )
    except:
        print("Can't identify the CRL URL")
    return crl_url_list


def get_subject_information_access_list(cert):
    #returns a list

    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    sia_url_list = []

    try:
        sia_ext = cert_object.extensions.get_extension_for_oid(x509.oid.ExtensionOID.SUBJECT_INFORMATION_ACCESS)
        for description in sia_ext.value._descriptions:
            if "http" in description._access_location.value:
                sia_url_list.append(description._access_location.value)

    except:
        print("Could not identify the Subject Information Access extension")

    return sia_url_list


def get_authority_information_access_list(cert):
    #returns a list of strings

    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    aia_url_list = []

    try:
        aia_ext = cert_object.extensions.get_extension_for_oid(x509.oid.ExtensionOID.AUTHORITY_INFORMATION_ACCESS)
        for description in aia_ext.value._descriptions:
            if "http" in description._access_location.value:
                aia_url_list.append(description._access_location.value)
    except:
        print("Could not identify the Authority Information Access extension")

    return aia_url_list


def get_subject_alternative_names(cert):
    #returns a list of strings

    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    san_list = []
    try:
        san_ext = cert_object.extensions.get_extension_for_oid(x509.oid.ExtensionOID.SUBJECT_ALTERNATIVE_NAME)
        for dns_name in san_ext._value._general_names:
            san_list.append(dns_name._value)
    except:
        print("Could not read subject alternative names")

    return san_list


def get_certificate_version(cert):
    #returns a string

    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    try:
        version = cert_object.version.name
    except:
        version = ""
        print("Could not determine certificate version")

    return version


def get_basic_constraint_ca(cert):
    #returns a boolean

    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    try:
        constraint_ext = cert_object.extensions.get_extension_for_oid(x509.oid.ExtensionOID.BASIC_CONSTRAINTS)
        return constraint_ext._value.ca


    except:
        print("Could not read the basic constraints extension for CA")
        return None


def get_basic_constraint_path_length(cert):
    #returns a list of strings

    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    try:
        constraint_ext = cert_object.extensions.get_extension_for_oid(x509.oid.ExtensionOID.BASIC_CONSTRAINTS)
        return constraint_ext._value.path_length

    except:
        print("Could not read the basic constraint extensions for path length")
        return None


def get_extended_key_usage(cert):
    #returns a string of concatenated usages

    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    all_usages = ""

    try:
        extended_key_usage = cert_object.extensions.get_extension_for_oid(x509.oid.ExtensionOID.EXTENDED_KEY_USAGE)
        usages = extended_key_usage.value._usages
        for usage in usages:
            if usage == x509.oid.ExtendedKeyUsageOID.CLIENT_AUTH:
                if all_usages == "":
                    all_usages += "Client Auth"
                else:
                    all_usages += ", Client Auth"
            elif usage == x509.oid.ExtendedKeyUsageOID.SERVER_AUTH:
                if all_usages == "":
                    all_usages += "Server Auth"
                else:
                    all_usages += ", Server Auth"
            elif usage == x509.oid.ExtendedKeyUsageOID.CODE_SIGNING:
                if all_usages == "":
                    all_usages += "Code Signing"
                else:
                    all_usages += ", Code Signing"
            elif usage == x509.oid.ExtendedKeyUsageOID.OCSP_SIGNING:
                if all_usages == "":
                    all_usages += "OCSP Signing"
                else:
                    all_usages += ", OCSP Signing"
            elif usage == x509.oid.ExtendedKeyUsageOID.EMAIL_PROTECTION:
                if all_usages == "":
                    all_usages += "Email Protection"
                else:
                    all_usages += ", Email Protection"
            elif usage == x509.oid.ExtendedKeyUsageOID.TIME_STAMPING:
                if all_usages == "":
                    all_usages += "Time Stamping"
                else:
                    all_usages += ", Time Stamping"
            elif usage == x509.oid.ExtendedKeyUsageOID.ANY_EXTENDED_KEY_USAGE:
                if all_usages == "":
                    all_usages += "Any Extended Key Usage"
                else:
                    all_usages += ", Any Extended Key Usage"
    except:
        print("Could not get extended key usages")

    return all_usages

def get_key_usage(cert):
    #returns a string of concatenated usages

    if type(cert) == str or type(cert) == bytes:
        #Load the certificate raw text into a cryptography x509 certificate object
        cert_object = load_cert_object(cert)
    else:
        #The variable was passed in as a certificate object
        cert_object = cert

    key_usage = cert_object.extensions.get_extension_for_oid(x509.oid.ExtensionOID.KEY_USAGE)

    all_usages = "digital_signature=" + str(key_usage.value._digital_signature)
    all_usages += ", content_commitment=" + str(key_usage.value._content_commitment)
    all_usages += ", key_encipherment=" + str(key_usage.value._key_encipherment)
    all_usages += ", data_encipherment=" + str(key_usage.value._data_encipherment)
    all_usages += ", key_agreement=" + str(key_usage.value._key_agreement)
    all_usages += ", key_cert_sign=" + str(key_usage.value._key_cert_sign)
    all_usages += ", crl_sign=" + str(key_usage.value._crl_sign)
    all_usages += ", encipher_only=" + str(key_usage.value._encipher_only)
    all_usages += ", decipher_only=" + str(key_usage.value._decipher_only)

    return all_usages


def get_certs_from_pkcs7(pkcs7_filename):
    #Pass in a pkcs7 file
    #Returns a list of cryptopgraphy certificate objects

    if not os.path.exists(pkcs7_filename):
        return []
    file1 = open(pkcs7_filename, "rb")
    p7b_bytes = file1.read()
    file1.close()

    #get a list of certificates from the p7b that are type cryptography x509 certificates
    x509_certs = pkcs7.load_der_pkcs7_certificates(p7b_bytes)
    return x509_certs

