import base64

def encode_email(email):
    encoded_email = base64.b64encode(email.encode()).decode()
    return encoded_email

def decode_email(encoded_email):
    decoded_email = base64.b64decode(encoded_email).decode()
    return decoded_email


