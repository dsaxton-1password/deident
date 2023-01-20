import os
import hmac
import hashlib

key = os.environ.get("HMAC_SECRET")
if not key:
    raise RuntimeError("HMAC_SECRET environment variable must be set")
key = bytes(key, "utf-8")


def apply(messages: list) -> list:
    return [hmac.digest(key, bytes(m, "utf-8"), hashlib.sha256).hex() for m in messages]
