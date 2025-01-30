from dataclasses import dataclass, field
from typing import List

# {
#     "name": "John Doe",
#     "job": "Software Developer",
#     "address": {
#         "city": "New York",
#         "state": "NY",
#         "zip": "10001"
#     },
#     "skills": ["Python", "Java", "JavaScript"]
# }


@dataclass
class Address:
    city: str
    state: str
    zip: str

@dataclass
class User:
    name: str
    job: str
    address: Address
    skills: List[str] = field(default_factory=list)

    def to_dict(self):
        """Convert the dataclass to a dictionary."""
        from dataclasses import asdict
        return asdict(self)