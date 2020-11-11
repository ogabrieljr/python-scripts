import hashlib
import sys

import requests


def request_api(query):
    res = requests.get(f"https://api.pwnedpasswords.com/range/{query}")
    if res.status_code != 200:
        raise RuntimeError(res.status_code)
    return res


def hash_password(password):
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    res = request_api(first5_char)
    hashes = [line.split(":") for line in res.text.splitlines()]
    for h, count in hashes:
        if h == tail:
            return count
    return 0


def main(args):
    for password in args:
        count = hash_password(password)
        if count:
            print(f"{password} count: {count}")
        else:
            print(f"{password} not found")
    return "done"


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
