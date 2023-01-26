import os
import hmac
import hashlib

import boto3

key = os.environ.get("HMAC_SECRET")
if not key:
    secretsmanager = boto3.client("secretsmanager")
    key = secretsmanager.get_secret_value(SecretId="TODO")
key = bytes(key, "utf-8")


def apply(message: str) -> str:
    return hmac.digest(key, bytes(message, "utf-8"), hashlib.sha256).hex()
