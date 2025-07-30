from abc import ABC, abstractmethod
from entities.doctor import Doctor

class DoctorRepositoryInterface(ABC):
    @abstractmethod
    def save(self, doctor: Doctor) -> Doctor: pass

    @abstractmethod
    def delete_by_id(self, id: int): ...

    @abstractmethod
    def find_by_id(self, id: int) -> Doctor: ...

    @abstractmethod
    def find_by_name(self, name: str) -> list[Doctor]: ...

    @abstractmethod
    def find_by_specialty(self, specialty: str) -> list[Doctor]: ...

    @abstractmethod
    def find_all(self) -> list[Doctor]: ...