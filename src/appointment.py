from datetime import datetime

class Appointment:

    def __init__(self, patient_id: int, doctor_id: str, appointment_date: datetime):
        self.__patient_id = patient_id
        self.__doctor_id = doctor_id
        self.__appointment_date = appointment_date
        self.__count: int = 0
        self.__appointment_id = f"Appointment {self.__count}"

    @property
    def get_appointment_id(self):
        return self.__appointment_id

    @get_appointment_id.setter
    def get_appointment_id(self, appointment_number: int):
        self.__count = appointment_number
        self.__appointment_id = f"Appointment {self.__count}"

    @property
    def get_patient_id(self):
        return self.__patient_id

    @property
    def get_doctor_id(self):
        return self.__doctor_id

    @property
    def get_appointment_date(self):
        return self.__appointment_date

    def __str__(self):
        message = (f"Patient ID: {self.__patient_id}\n Doctor ID: {self.__doctor_id}\n Appointment Date: {self.__appointment_date}\n")
        return message
