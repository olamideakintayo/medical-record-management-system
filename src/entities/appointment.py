from dataclasses import dataclass
from datetime import datetime

@dataclass
class Appointment:
    appointment_id: str
    patient_id: str
    doctor_id: str
    appointment_time: datetime = datetime.now()