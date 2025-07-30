from src.entities.appointment import Appointment
from repositories.appointment_interface import AppointmentRepositoryInterface
from utils.string_utils import StringUtils
from datetime import datetime


class AppointmentRepository(AppointmentRepositoryInterface):
    def __init__(self, db):
        self.collection = db.appointments

    def save(self, appointment: Appointment) -> Appointment:
        data = appointment.__dict__.copy()
        data.pop("_id", None)
        self.collection.update_one(
            {"appointment_id": data["appointment_id"]},
            {"$set": data},
            upsert=True
        )
        return appointment

    def delete_by_id(self, appointment_id: str) -> None:
        result = self.collection.delete_one({"_id": appointment_id})
        if result.deleted_count == 0:
            raise ValueError("Appointment not found")

    def find_by_appointment_id(self, appointment_id: str) -> Appointment:
        data = self.collection.find_one({"_id": appointment_id})
        if not data:
            raise ValueError("Appointment not found")
        data["appointment_id"] = data.pop("_id")
        data["appointment_time"] = datetime.fromisoformat(data["appointment_time"])
        return Appointment(**data)

    def find_by_doctor_id(self, doctor_id: str) -> list[Appointment]:
        docs = self.collection.find()
        result = []
        for doc in docs:
            if StringUtils.equals_ignore_case(doc["doctor_id"], doctor_id):
                doc["appointment_id"] = doc.pop("_id")
                result.append(Appointment(**doc))
        return result

    def find_by_patient_id(self, patient_id: str) -> Appointment:
        docs = self.collection.find()
        for doc in docs:
            if StringUtils.equals_ignore_case(doc["patient_id"], patient_id):
                doc["appointment_id"] = doc.pop("_id")
                return Appointment(**doc)
        raise ValueError("Appointment for given patient not found")

    def find_by_doctor_id_and_date_time(self, doctor_id: str, date_time: datetime) -> list[Appointment]:
        docs = self.collection.find()
        result = []
        for doc in docs:
            if (
                    StringUtils.equals_ignore_case(doc["doctor_id"], doctor_id) and
                    datetime.fromisoformat(doc["appointment_time"]) == date_time
            ):
                doc["appointment_id"] = doc.pop("_id")
                doc["appointment_time"] = datetime.fromisoformat(doc["appointment_time"])
                result.append(Appointment(**doc))
        return result


