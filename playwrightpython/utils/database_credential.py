import json
from enum import Enum


def load_db_credentials(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
        return data["db_details"]

# Define an Enum for login credentials
class DBDetails(Enum):
    HOST = "host"
    PORT = "port"
    USER = "user"
    PASSWORD = "password"
    DBNAME= "dbname"

    # Add a method to initialize db details
    @classmethod
    def initialize(cls, db_data):
        # Initialize the db details to a class variable
        cls._db_details = db_data

    # Properties to fetch db detail values dynamically
    @property
    def db_value(self):
        return self._db_details.get(self.value, None)
