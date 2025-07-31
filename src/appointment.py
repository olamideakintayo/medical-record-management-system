from doctor import Doctor
from patient import Patient
from datetime import datetime

class Appointment:

    def __init__(self, patient: Patient, doctor: Doctor, appointment_date: datetime, description: str)->None:
        self.__patient = patient
        self.__doctor = doctor
        self.__appointment_date = appointment_date
        self.__description = description

        def patient(self):
            return self.__patient

        def doctor(self):
            return self.__doctor

        @appointment_date.setter
        def appointment_date(self, appointment_date):
            self._appointment_date = appointment_date

        def get_appointment_date(self):
            return self._appointment_date

        @description.setter
        def description(self, description):
            self.__description = description

        def get_description(self):
            return self.__description

