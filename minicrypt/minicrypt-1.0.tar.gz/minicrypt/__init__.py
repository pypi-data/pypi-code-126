import uuid


def encrypt(message: str, key: str) -> str:  # Encrypt message
    encoded_text = ''

    key_id = 0
    for letter in message:
        l_code = ord(letter)
        if key_id >= len(key):
            key_id = 0
        key_code = ord(key[key_id])

        encoded_text += chr(l_code + key_code)

        key_id += 1

    return encoded_text


def decrypt(message: str, key: str) -> str:  # Decrypt message
    decoded_text = ''

    key_id = 0
    for letter in message:

        l_code = ord(letter)
        if key_id >= len(key):
            key_id = 0
        key_code = ord(key[key_id])

        decoded_text += chr(l_code - key_code)

        key_id += 1

    return decoded_text


def generate_key() -> str:  # Generate random key
    return uuid.uuid4().hex