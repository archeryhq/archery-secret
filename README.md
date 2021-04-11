# Archery Secret

Generates, encrypt, decrypt and verify secrets.

[Github](https://github.com/archeryhq/archery-secret)

## How to use

Before using the module, it is necessary to create an environment variable *ARCHERY_PERSON_SECRET*, which can be inside an .env file inside the project.This key must be 32 url-safe base64-encoded bytes.

```python
>>> from archery_secret import Secret
>>>
>>>
>>> passphrase = 'My_most_hidden_secret'
>>> secret = Secret()
>>> secret.randomic
'etH-rDnCiroCDVt4TzgWl99cJV1jLQVt-JrBOAEmzbA='
>>> encrypt = secret.encrypt(passphrase)
>>> encrypt
'gAAAAABgbNDuhZqY16KlnXbl6X_F5PO0PgA2ExpSfTmw9szmzpR2FO1qz1YUE9rU84DU1q9jRszApSk58Vgvo5UVZwKgsFzvRgWHxI6YLuFNOVcsM2v0sQ8='
>>> secret.decrypt(encrypt)
'My_most_hidden_secret'
>>> hash = secret.generate(passphrase)
>>> hash
'$argon2id$v=19$m=102400,t=2,p=8$DxKq0YC4ICc6x6gsn5L6DA$2gFfRH6lYqIaI01nAwKcMQ'
>>> secret.verify(hash, passphrase)
True
```
