# `deident`

A simple Python module that provides a single function `deident.hmac.apply` to handle transformation of a list of string values using SHA256 HMAC. On import `deident` will attempt to grab an HMAC secret either from the environment variable `HMAC_SECRET` or from AWS SecretsManager (if both fail then an error will be raised).

Example:

```shell
> export HMAC_SECRET="secret"
```

```python
>>> from deident import hmac
>>> hmac.apply(["a", "b", "c", "c", "b"])
['4048c44911916043ff626895ff78c5262764685b6cb9a03ce07886a9effb924c', '8caf295837e09c876c0c5ef729581d5e75ef93adc10420ce71aab05636ac63ed', 'ef006b65b8ce49c891479554278e47e7d76735e7ddd6392fc68342322f39e3c4', 'ef006b65b8ce49c891479554278e47e7d76735e7ddd6392fc68342322f39e3c4', '8caf295837e09c876c0c5ef729581d5e75ef93adc10420ce71aab05636ac63ed']
```

If `HMAC_SECRET` isn't set and can't be found in SecretsManager:

```python
>>> from deident import hmac
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/deident-venv/lib/python3.8/site-packages/deident/hmac.py", line 7, in <module>
    raise RuntimeError("Could not find HMAC key in either HMAC_SECRET environment variable or SecretsManager")
RuntimeError: Could not find HMAC key in either HMAC_SECRET environment variable or SecretsManager
```

In order to install `deident` from a GitLab CI runner use the following command:

```shell
pip install deident --extra-index-url https://gitlab-ci-token:${CI_JOB_TOKEN}@gitlab.1password.io/api/v4/projects/1152/packages/pypi/simple
```
