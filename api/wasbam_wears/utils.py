import string
import secrets


alphabet = string.ascii_letters + string.digits


def generate_slug(length):
    slug = ''.join(
        secrets.choice(alphabet) for i in range(length)
    )

    return slug
