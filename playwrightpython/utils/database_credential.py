import json
from enum import Enum


def load_db_credentials(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data["db_details"]


# Define an Enum for db credentials
class DBDetails(Enum):
    HOST = "host"
    PORT = "port"
    DBNAME = "dbname"

    @classmethod
    def initialize(cls, db_data):
        # Initialize the db details to a class variable
        cls._db_details = db_data

    @property
    def db_value(self):
        return self._db_details.get(self.value, None)


class DBCredDetails(Enum):
    USER = "user"
    PASSWORD = "password"

    # Add a method to initialize db details
    @classmethod
    def initialize(cls, db_data):
        # Initialize the db details to a class variable
        cls._db_cred_details = db_data

    # Properties to fetch db detail values dynamically
    @property
    def db_cred_value(self):
        return self._db_cred_details.get(self.value, None)
