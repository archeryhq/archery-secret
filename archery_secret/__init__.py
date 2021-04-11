from dotenv import load_dotenv
from os import getenv
from cryptography.fernet import Fernet
from argon2 import PasswordHasher
from argon2.exceptions import (
    InvalidHash,
    VerifyMismatchError
)


load_dotenv()


class Secret:
    """
        Responsible to generate and verify secrets.

    """
    __fernet = Fernet(
        getenv(
            'ARCHERY_PERSON_SECRET'
        )
    )
    __argon = PasswordHasher()
    __header = __argon.hash(
        getenv(
            'ARCHERY_PERSON_SECRET'
        )
    )[:32]

    @property
    def randomic(
        self: object
    ) -> str:
        """
            Generates randomic keys.
        """
        return self.__fernet.generate_key().decode()

    def generate(
        self: object,
        secret: str
    ) -> str:
        """
            Generates password keys from a hash.
        """
        return self.__argon.hash(
            secret
        ).replace(
            self.__header,
            ''
        )

    def verify(
        self: object,
        hash: str,
        secret: str,
    ) -> bool:
        """
            Verify password hash.
        """
        try:
            result = self.__argon.verify(
                self.__header + hash,
                secret
            )
        except InvalidHash:
            return False
        except VerifyMismatchError:
            return False
        return result

    def encrypt(
        self: object,
        message: str
    ) -> str:
        """
            Encrypt messages.
        """
        return self.__fernet.encrypt(
            str(
                message
            ).encode()
        ).decode()

    def decrypt(
        self: object,
        message: str
    ) -> str:
        """
            Decrypt messages.
        """
        return self.__fernet.decrypt(
            message if isinstance(
                message,
                bytes
            ) else message.encode()
        ).decode()

