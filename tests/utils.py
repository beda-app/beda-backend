import random
import string


def random_string(length: int) -> str:
    return "".join(random.sample(string.digits + string.ascii_lowercase, length))


def generate_random_email():
    return random_string(8) + "@" + random_string(8) + "." + random_string(3)


def generate_random_password():
    return "".join(random.sample(string.digits + string.ascii_letters, 8))
