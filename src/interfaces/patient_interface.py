from abc import ABC, abstractmethod
from typing import List
from entities.patient import Patient


class PatientRepositoryInterface(ABC):
    @abstractmethod
    def save(self, patient: Patient) -> Patient: pass

    @abstractmethod
    def delete_by_id(self, id: int) -> None: pass

    @abstractmethod
    def find_all(self) -> List[Patient]: pass

    @abstractmethod
    def find_by_id(self, id: int) -> Patient: pass
