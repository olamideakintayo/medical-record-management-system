from dataclasses import dataclass

@dataclass
class Doctor:
    id: int
    name: str
    specialty: str
    contact_details: str