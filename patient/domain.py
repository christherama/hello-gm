from dataclasses import dataclass


@dataclass
class Patient:
    id: int
    first_name: str
    last_name: str
