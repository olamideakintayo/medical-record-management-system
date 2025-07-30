import unittest
from unittest.mock import MagicMock
from src.entities.doctor import Doctor
from src.repositories.doctor_repository import DoctorRepository


class TestDoctorRepository(unittest.TestCase):
    def setUp(self):
        self.mock_collection = MagicMock()
        self.mock_db = MagicMock()
        self.mock_db.doctors = self.mock_collection
        self.repo = DoctorRepository(self.mock_db)

    def test_save_doctor(self):
        doctor = Doctor(id=1, name="Dr.Smith", specialty="Cardiology", contact_details="09034567890")
        self.repo.save(doctor)

        expected_data = doctor.__dict__.copy()
        expected_data.pop("id")

        self.mock_collection.update_one.assert_called_once_with(
            {"_id": doctor.id}, {"$set": expected_data}, upsert=True
        )

    def test_that_you_can_find_by_id(self):
        mock_data = {
            "_id": 1,
            "name": "Dr.Smith",
            "specialty": "Cardiology",
            "contact_details": "09034567890"
        }
        self.mock_collection.find_one.return_value = mock_data

        found = self.repo.find_by_id(1)

        self.assertEqual(found.name, "Dr.Smith")
        self.assertEqual(found.specialty, "Cardiology")
        self.assertEqual(found.contact_details, "09034567890")
        self.mock_collection.find_one.assert_called_once_with({"_id": 1})

    def test_that_raises_value_error_if_an_invalid_id_is_inputted(self):
        self.mock_collection.find_one.return_value = None
        with self.assertRaises(ValueError):
            self.repo.find_by_id(1)

    def test_that_checks_if_you_can_find_by_name(self):
        mock_docs = [
            {
                "_id": 1,
                "name": "Dr.Smith",
                "specialty": "Cardiology",
                "contact_details": "09034567890"
            },
            {
                "_id": 2,
                "name": "Dr.Jane",
                "specialty": "Neurology",
                "contact_details": "09012345678"
            }
        ]
        self.mock_collection.find.return_value = mock_docs

        found = self.repo.find_by_name("Dr.Smith")
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].name, "Dr.Smith")

        self.mock_collection.find.return_value = mock_docs  # reassign for next call
        found2 = self.repo.find_by_name("Dr.Jane")
        self.assertEqual(len(found2), 1)
        self.assertEqual(found2[0].name, "Dr.Jane")

        self.assertEqual(self.mock_collection.find.call_count, 2)

    def test_that_checks_if_you_can_find_by_specialty(self):
        mock_docs = [
            {
                "_id": 1,
                "name": "Dr.Smith",
                "specialty": "Cardiology",
                "contact_details": "09034567890"
            },
            {
                "_id": 2,
                "name": "Dr.Jones",
                "specialty": "Cardiology",
                "contact_details": "09012345678"
            }
        ]
        self.mock_collection.find.return_value = mock_docs

        found = self.repo.find_by_specialty("Cardiology")
        self.assertEqual(len(found), 2)
        self.assertEqual(found[0].specialty.lower(), "cardiology")
        self.assertEqual(found[1].specialty.lower(), "cardiology")

        self.mock_collection.find.assert_called_once_with()

    def test_that_checks_if_you_can_find_all_doctors(self):
        mock_docs = [
            {
                "_id": 1,
                "name": "Dr.Smith",
                "specialty": "Cardiology",
                "contact_details": "09034567890"
            },
            {
                "_id": 2,
                "name": "Dr.Jones",
                "specialty": "Neurology",
                "contact_details": "09012345678"
            }
        ]
        self.mock_collection.find.return_value = mock_docs

        doctors = self.repo.find_all()
        self.assertEqual(len(doctors), 2)
        self.assertEqual(doctors[0].name, "Dr.Smith")
        self.assertEqual(doctors[1].name, "Dr.Jones")

        self.mock_collection.find.assert_called_once_with()

    def test_that_checks_if_you_can_delete_by_id_successfully(self):
        self.mock_collection.delete_one.return_value.deleted_count = 1
        self.repo.delete_by_id(1)
        self.mock_collection.delete_one.assert_called_once_with({"_id": 1})

    def test_that_delete_by_id_raises_if_not_found(self):
        self.mock_collection.delete_one.return_value.deleted_count = 0
        with self.assertRaises(ValueError):
            self.repo.delete_by_id(99)

    def test_find_by_name_is_case_insensitive_using_string_utils(self):
        mock_docs = [
            {
                "_id": 1,
                "name": "Dr.Smith",
                "specialty": "Cardiology",
                "contact_details": "09034567890"
            },
            {
                "_id": 2,
                "name": "Dr.Jane",
                "specialty": "Neurology",
                "contact_details": "09012345678"
            }
        ]
        self.mock_collection.find.return_value = mock_docs

        found = self.repo.find_by_name("dr.smith")
        self.assertEqual(len(found), 1)
        self.assertEqual(found[0].name, "Dr.Smith")

        found2 = self.repo.find_by_name("DR.JANE")
        self.assertEqual(len(found2), 1)
        self.assertEqual(found2[0].name, "Dr.Jane")

    def test_find_by_specialty_is_case_insensitive_using_string_utils(self):
        mock_docs = [
            {
                "_id": 1,
                "name": "Dr.Smith",
                "specialty": "Cardiology",
                "contact_details": "09034567890"
            },
            {
                "_id": 2,
                "name": "Dr.Jane",
                "specialty": "cardiology",  # lowercase on purpose
                "contact_details": "09012345678"
            },
            {
                "_id": 3,
                "name": "Dr.Tom",
                "specialty": "Neurology",
                "contact_details": "09000000000"
            }
        ]
        self.mock_collection.find.return_value = mock_docs

        found = self.repo.find_by_specialty("CARDIOLOGY")
        self.assertEqual(len(found), 2)
        self.assertEqual(found[0].specialty, "Cardiology")
        self.assertEqual(found[1].specialty, "cardiology")







