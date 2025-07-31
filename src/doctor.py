class Doctor:
    def __init__(self, doctor_name: str, speciality: str, contact: str, details: str)->None:
        self.__doctor_name = doctor_name
        self.__speciality = speciality
        self.__contact = contact
        self.__details = details

        def get_doctor_name(self):
            return self.__doctor_name

        def get_speciality(self):
            return self.__speciality

        def get_contact(self):
            return self.__contact

        def get_details(self):
            return self.__details


