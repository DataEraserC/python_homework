import random
import string


def gen_random_password(times, length):
    passwords = []
    for i in range(times):
        password = ""
        for j in range(length):
            password = ''.join(random.sample(
                string.ascii_letters + string.digits, 8))
        passwords.append(password)
    return passwords


print(gen_random_password(10, 8))
