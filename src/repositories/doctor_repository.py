from src.entities.doctor import Doctor
from src.interfaces.doctor_interface import DoctorRepositoryInterface
from utils.string_utils import StringUtils


class DoctorRepository(DoctorRepositoryInterface):
    def __init__(self, db):
        self.collection = db.doctors

    def save(self, doctor: Doctor):
        data = doctor.__dict__.copy()
        if "id" in data:
            del data["id"]
        self.collection.update_one(
            {"_id": doctor.id},
            {"$set": data},
            upsert=True
        )

    def delete_by_id(self, id: int):
        result = self.collection.delete_one({"_id": id})
        if result.deleted_count == 0:
            raise ValueError("Doctor not found")

    def find_by_id(self, id: int) -> Doctor:
        data = self.collection.find_one({"_id": id})
        if not data:
            raise ValueError("Doctor not found")
        data["id"] = data.pop("_id")
        return Doctor(**data)

    def find_by_name(self, name: str) -> list[Doctor]:
        all_doctors = self.collection.find()
        matching = []
        for doc in all_doctors:
            if StringUtils.equals_ignore_case(doc["name"], name):
                doc["id"] = doc.pop("_id")
                matching.append(Doctor(**doc))
        return matching


    def find_by_specialty(self, specialty: str) -> list[Doctor]:
        all_doctors = self.collection.find()
        matching = []
        for doc in all_doctors:
            if StringUtils.equals_ignore_case(doc["specialty"], specialty):
                doc["id"] = doc.pop("_id")
                matching.append(Doctor(**doc))
        return matching

    def find_all(self) -> list[Doctor]:
        doctors = []
        for doc in self.collection.find():
            doc["id"] = doc.pop("_id")
            doctors.append(Doctor(**doc))
        return doctors