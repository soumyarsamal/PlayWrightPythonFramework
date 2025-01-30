from enum import Enum


class UserRole(Enum):
    OPERATOR = "operator"
    SENIOR_OPERATOR = "senior_operator"
    ADMIN = "admin"

    def __str__(self):
        return self.value