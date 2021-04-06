from unittest import TestCase
from archery_secret import Secret


class TestSecret(TestCase):
    passphrase = 'My_most_hidden_secret'
    secret = Secret()

    def test_randomic_secret(self):
        assert type(
            self.secret.randomic
        ) == str

    def test_encrypt_and_decrypt_passphrase(self):
        assert self.secret.decrypt(
            self.secret.encrypt(
                self.passphrase
            )
        ) == self.passphrase

    def test_creation_and_verifying_password(self):
        assert self.secret.verify(
            self.secret.generate(
                self.passphrase
            ),
            self.passphrase
        )
