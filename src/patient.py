class Patient:
    def __init__(self, name: str, contact_detail:str, date_of_birth: str, medical_history: str) -> None:
        self.__name = name
        self.__contact_detail = contact_detail
        self.__date_of_birth = date_of_birth
        self.__id = 0

    def get_name(self) -> str:
        return self.__name

    def get_contact_detail(self) -> str:
        return self.__contact_detail

    def get_date_of_birth(self) -> str:
        return self.__date_of_birth

    def get_id(self) -> int:
        return self.__id

    def set_id(self, id: int) -> None:
        self.__id = int(id)

    def __str__(self) -> str:
        message = (f" patient id: {self.__id}\n Patient Name: {self.__name}\n Contact Detail: {self.__contact_detail}\n Date of Birth: {self.__date_of_birth}\n Medical History: {self.__medical_history}\n")
        return message