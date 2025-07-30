from abc import ABC, abstractmethod
from src.entities.appointment import Appointment
from datetime import datetime

class AppointmentRepositoryInterface(ABC):

    @abstractmethod
    def save(self, appointment: Appointment) -> Appointment:
        pass

    @abstractmethod
    def delete_by_id(self, appointment_id: str) -> None:
        pass

    @abstractmethod
    def find_by_appointment_id(self, appointment_id: str) -> Appointment:
        pass

    @abstractmethod
    def find_by_doctor_id(self, doctor_id: str) -> list[Appointment]:
        pass

    @abstractmethod
    def find_by_patient_id(self, patient_id: str) -> Appointment:
        pass

    @abstractmethod
    def find_by_doctor_id_and_date_time(self, doctor_id: str, date_time: datetime) -> list[Appointment]:
        pass