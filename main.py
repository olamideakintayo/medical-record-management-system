from src.config.mongo_connection import db
from src.repositories.patient_repository import PatientRepository
from src.entities.patient import Patient

def main():
    patient_repo = PatientRepository(db)

    # Create and save a patient
    patient = Patient(id=1, name="Olamide Akintayo", date_of_birth="12-03-1999", contact_details="09087654321", medical_history="Asthma")
    patient_repo.save(patient)
    print("Patient saved.")

    # Find by ID
    retrieved = patient_repo.find_by_id(1)
    print("Retrieved Patient:", retrieved)

    # Find all
    all_patients = patient_repo.find_all()
    print("All Patients:")
    for p in all_patients:
        print(p)



if __name__ == "__main__":
    main()


