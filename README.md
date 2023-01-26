# `deident`

A simple Python module that provides a single function `deident.hmac.apply` to handle transformation of a list of string values using SHA256 HMAC. On import `deident` will attempt to grab an HMAC secret either from the environment variable `HMAC_SECRET`, or from AWS SecretsManager using the environment variable `SECRET_NAME` as the secret ID if `HMAC_SECRET` isn't provided.

Example:

```shell
> export HMAC_SECRET="secret"
```

```python
>>> from deident import hmac
>>> hmac.apply("a")
'4048c44911916043ff626895ff78c5262764685b6cb9a03ce07886a9effb924c'
>>> hmac.apply("b")
'8caf295837e09c876c0c5ef729581d5e75ef93adc10420ce71aab05636ac63ed'
>>> hmac.apply("b")
'8caf295837e09c876c0c5ef729581d5e75ef93adc10420ce71aab05636ac63ed'
>>> hmac.apply("c")
'ef006b65b8ce49c891479554278e47e7d76735e7ddd6392fc68342322f39e3c4'
```
