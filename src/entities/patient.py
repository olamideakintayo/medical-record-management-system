from dataclasses import dataclass

@dataclass
class Patient:
    id: int
    name: str
    date_of_birth: str
    contact_details: str
    medical_history: str