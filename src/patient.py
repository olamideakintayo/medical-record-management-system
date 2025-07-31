class Patient:

    def __init__(self, name: str, date_of_birth: str, contact_details: str, medical_details: str)->None:
        self.__name = name
        self.__date_of_birth = date_of_birth
        self.__contact_details = contact_details
        self.__medical_details = medical_details
        self.__count = 0

    def count(self):
        self.__count += 1

    def get_name(self):
       return self.__name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_contact_details(self):
        return self.__contact_details

    def get_medical_details(self):
        return self.__medical_details


    def __str__(self):
        message = (f"Patient Name: {self.__name}\n"
                   f"Date of birth: {self.__date_of_birth}\n"
                   f"Contact Details: {self.__contact_details}\n"
                   f"Medical Details: {self.__medical_details}")
        return message




helen = Patient("<NAME>", "2020-02-03", "080", "Head de pain me")
print(helen.__str__())