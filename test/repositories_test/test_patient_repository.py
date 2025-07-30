import unittest
from unittest.mock import MagicMock
from src.entities.patient import Patient
from src.repositories.patient_repository import PatientRepository

class TestPatientRepository(unittest.TestCase):
    def setUp(self):
        self.mock_collection = MagicMock()
        self.mock_db = MagicMock()
        self.mock_db.patients = self.mock_collection
        self.repo = PatientRepository(self.mock_db)

    def test_that_checks_if_patients_are_being_saved_successfully(self):
        patient = Patient(id=1, name="Jane", date_of_birth="12-3-1999", contact_details="09023234565", medical_history="Cold")
        self.repo.save(patient)
        expected_data = patient.__dict__.copy()
        expected_data.pop("id")

        self.mock_collection.update_one.assert_called_once_with(
            {"_id": patient.id}, {"$set": expected_data}, upsert=True
        )

    def test_checks_if_you_can_find_by_id(self):
        mock_data = {
            "_id": 1,
            "name": "Jane",
            "date_of_birth":"12-3-1999",
            "contact_details":"09023234565",
            "medical_history": "Cold"
        }
        self.mock_collection.find_one.return_value = mock_data

        found = self.repo.find_by_id(1)

        self.assertEqual(found.name, "Jane")
        self.assertEqual(found.date_of_birth, "12-3-1999")
        self.assertEqual(found.contact_details, "09023234565")
        self.assertEqual(found.medical_history, "Cold")
        self.mock_collection.find_one.assert_called_once_with({"_id": 1})

    def test_that_raises_value_error_if_an_invalid_id_is_inputted(self):
        self.mock_collection.find_one.return_value = None
        with self.assertRaises(ValueError):
            self.repo.find_by_id(1)

    def test_that_checks_if_you_can_find_all_data(self):
        mock_docs = [
            {
                "_id": 1,
                "name": "Alice",
                "date_of_birth": "01-01-1990",
                "contact_details": "1234567890",
                "medical_history": "Fever"
            },
            {
                "_id": 2,
                "name": "Bob",
                "date_of_birth": "02-02-1992",
                "contact_details": "0987654321",
                "medical_history": "Cough"
            }
        ]
        self.mock_collection.find.return_value = mock_docs

        patients = self.repo.find_all()
        self.assertEqual(len(patients), 2)
        self.assertEqual(patients[0].name, "Alice")
        self.assertEqual(patients[1].name, "Bob")

    def test_that_checks_if_you_can_delete_by_id_successfully(self):
        self.mock_collection.delete_one.return_value.deleted_count = 1
        self.repo.delete_by_id(1)
        self.mock_collection.delete_one.assert_called_once_with({"_id": 1})

    def test_that_raises_value_error_if_an_invalid_id_is_inputted_when_you_want_to_delete_by_id(self):
        self.mock_collection.delete_one.return_value.deleted_count = 0
        with self.assertRaises(ValueError):
            self.repo.delete_by_id(99)

