import unittest
from unittest.mock import MagicMock
from datetime import datetime
from src.entities.appointment import Appointment
from src.repositories.appointment_impl import AppointmentRepository


class TestAppointmentRepository(unittest.TestCase):
    def setUp(self):
        self.mock_collection = MagicMock()
        self.mock_db = MagicMock()
        self.mock_db.appointments = self.mock_collection
        self.repo = AppointmentRepository(self.mock_db)

    def test_that_checks_save_inserts_or_updates_document(self):
        appointment = Appointment(
            appointment_id="1",
            patient_id="101",
            doctor_id="201",
            appointment_time=datetime(2024, 1, 1, 9, 0)
        )
        self.repo.save(appointment)

        expected_data = {
            "appointment_id": "1",
            "patient_id": "101",
            "doctor_id": "201",
            "appointment_time": datetime(2024, 1, 1, 9, 0)
        }

        self.mock_collection.update_one.assert_called_once_with(
            {"appointment_id": "1"},
            {"$set": expected_data},
            upsert=True
        )

    def test_that_checks_successful_deletion_by_id(self):
        self.mock_collection.delete_one.return_value.deleted_count = 1
        self.repo.delete_by_id("1")
        self.mock_collection.delete_one.assert_called_once_with({"_id": "1"})

    def test_that_checks_deletion_raises_error_when_id_not_found(self):
        self.mock_collection.delete_one.return_value.deleted_count = 0
        with self.assertRaises(ValueError):
            self.repo.delete_by_id("nonexistent")

    def test_that_checks_find_by_appointment_id_returns_valid_appointment(self):
        now = datetime(2025, 7, 29, 6, 56, 51, 889771)
        mock_doc = {
            "_id": "1",
            "doctor_id": "101",
            "patient_id": "201",
            "appointment_time": now.isoformat()
        }
        self.mock_collection.find_one.return_value = mock_doc
        result = self.repo.find_by_appointment_id("1")
        self.assertIsInstance(result, Appointment)
        self.assertEqual(result.appointment_id, "1")
        self.assertEqual(result.appointment_time, now)

    def test_that_checks_find_by_appointment_id_raises_error_if_not_found(self):
        self.mock_collection.find_one.return_value = None
        with self.assertRaises(ValueError):
            self.repo.find_by_appointment_id("missing_id")

    def test_that_checks_find_by_doctor_id_is_case_insensitive_and_filters_correctly(self):
        mock_docs = [
            {"_id": "1", "doctor_id": "DrX", "patient_id": "P1", "appointment_time": "2024-01-01T10:00:00"},
            {"_id": "2", "doctor_id": "DrY", "patient_id": "P2", "appointment_time": "2024-01-02T10:00:00"}
        ]
        self.mock_collection.find.return_value = mock_docs
        results = self.repo.find_by_doctor_id("drx")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].doctor_id, "DrX")
        self.assertEqual(results[0].appointment_id, "1")

    def test_that_checks_find_by_patient_id_is_case_insensitive_and_returns_correct_result(self):
        mock_docs = [
            {"_id": "1", "doctor_id": "Doc1", "patient_id": "abc123", "appointment_time": "2024-01-01T10:00:00"}
        ]
        self.mock_collection.find.return_value = mock_docs
        result = self.repo.find_by_patient_id("ABC123")
        self.assertEqual(result.patient_id, "abc123")
        self.assertEqual(result.appointment_id, "1")

    def test_that_checks_find_by_patient_id_raises_error_if_no_match(self):
        self.mock_collection.find.return_value = []
        with self.assertRaises(ValueError):
            self.repo.find_by_patient_id("nonexistent")

    def test_that_checks_find_by_doctor_id_and_datetime_returns_exact_matches(self):
        now = datetime(2025, 7, 29, 6, 56, 51, 981019)
        mock_docs = [
            {
                "_id": "1",
                "doctor_id": "777",
                "patient_id": "888",
                "appointment_time": now.isoformat()
            },
            {
                "_id": "2",
                "doctor_id": "777",
                "patient_id": "889",
                "appointment_time": "2024-01-01T09:00:00"
            }
        ]
        self.mock_collection.find.return_value = mock_docs

        results = self.repo.find_by_doctor_id_and_date_time("777", now)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].appointment_id, "1")
        self.assertEqual(results[0].appointment_time, now)
