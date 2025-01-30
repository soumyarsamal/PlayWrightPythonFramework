import json
from enum import Enum


def load_credentials(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data["login_credentials"]

# Define an Enum for login credentials
class LoginCredentials(Enum):
    OPERATOR = "operator"
    SENIOR_OPERATOR = "senior_operator"

    # Add a method to fetch username and password
    @classmethod
    def initialize(cls, credentials):
        cls._credentials = credentials

    @property
    def username(self):
        return self._credentials[self.value]["username"]

    @property
    def password(self):
        return self._credentials[self.value]["password"]