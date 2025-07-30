from src.entities.patient import Patient
from repositories.patient_interface import PatientRepositoryInterface


class PatientRepository(PatientRepositoryInterface):
    def __init__(self, db):
        self.collection = db.patients

    def save(self, patient: Patient):
        data = patient.__dict__.copy()
        if "id" in data:
            del data["id"]
        self.collection.update_one(
            {"_id": patient.id},
            {"$set": data},
            upsert=True
        )

    def delete_by_id(self, id: int):
        result = self.collection.delete_one({"_id": id})
        if result.deleted_count == 0:
            raise ValueError("Patient not found")

    def find_by_id(self, id: int) -> Patient:
        data = self.collection.find_one({"_id": id})
        if not data:
            raise ValueError("Patient not found")
        data["id"] = data.pop("_id")
        return Patient(**data)

    def find_all(self) -> list[Patient]:
            patients = []
            for doc in self.collection.find():
                doc["id"] = doc.pop("_id")
                patients.append(Patient(**doc))
            return patients

