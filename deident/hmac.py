import os
import hmac
import hashlib

import boto3

key = os.environ.get("HMAC_SECRET")
if not key:
    client = boto3.client("secretsmanager")
    try:
        key = client.get_secret_value(SecretId=os.environ.get("SECRET_NAME"))
    except Exception as err:
        key = ""
key = bytes(key, "utf-8")


def apply_string(input: str, key: bytes = key) -> str:
    return hmac.digest(key, bytes(input, "utf-8"), hashlib.sha256).hex()


def apply_int(input: int, key: bytes = key, num_bytes: int = 7, endianness: str = "big") -> str:
    return int.from_bytes(hmac.digest(key, bytes(input), hashlib.sha256)[:num_bytes], endianness)
