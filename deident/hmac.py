import os
import hmac
import hashlib

import boto3

key = os.environ.get("HMAC_SECRET")
if not key:
    secretsmanager = boto3.client("secretsmanager")
    key = secretsmanager.get_secret_value(SecretId="TODO")
    if not key:
        raise RuntimeError(
            "Could not find HMAC key in either HMAC_SECRET environment variable or SecretsManager"
        )
key = bytes(key, "utf-8")


def apply(messages: list) -> list:
    return [hmac.digest(key, bytes(m, "utf-8"), hashlib.sha256).hex() for m in messages]
