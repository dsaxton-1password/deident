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
        print(f"WARNING: {err}")
        print(f"WARNING: HMAC key set to empty string")
        key = ""
key = bytes(key, "utf-8")


def apply(message: str, key: bytes = key) -> str:
    return hmac.digest(key, bytes(message, "utf-8"), hashlib.sha256).hex()
