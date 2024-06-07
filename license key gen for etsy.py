import string
import secrets

def generate_license_key(length=16, with_cert_number=True):
    """Generates a license key with hyphens every 4 characters and an optional certificate number in curly braces."""
    key_chars = ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
    formatted_key = '-'.join(key_chars
                             [i:i+4] for i in range(0, len(key_chars), 4))

    if with_cert_number:
        cert_number = ''.join(secrets.choice(string.digits) for _ in range(5))
        return f"{formatted_key}-{{{cert_number}}}"  # Enclose in curly braces
    else:
        return formatted_key

# Example usage
for _ in range(20):
    license_key_with_cert = generate_license_key(with_cert_number=True)
    print(license_key_with_cert)

