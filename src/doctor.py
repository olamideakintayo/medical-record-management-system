from itertools import count

class Doctor:

    def __init__(self, name, specialisation, contact):
        self.__name = name
        self.__specialisation:str = specialisation
        self.__contact_details: str = contact
        self.__count: int = 0
        self.__id:str = f"Dr {self.__count}"

    @property
    def get_name(self):
        return self.__name

    @property
    def get_specialisation(self):
        return self.__specialisation

    @property
    def get_contact_details(self):
        return self.__contact_details

    def set_count(self, doctors_number:int):
        self.__count = doctors_number
        self.__id = f"Dr {self.__count}"

    @property
    def get_id(self):
        return self.__id

    def __str__(self):
        message = (f"Doctor Name: {self.__name}\n Specialisation: {self.__specialisation}\n Contact Details: {self.__contact_details}\n")
        return message


