from abc import abstractmethod
from abc import ABCMeta

from Model.models import Material, Movement


class IMaterialsSystem(metaclass=ABCMeta):

    @abstractmethod
    def create_material(self, material: Material) -> bool:
        """Create a Material object and stores it in the database.
        """
        pass

    @abstractmethod
    def edit_material(self, material: Material, material_id: int) -> bool:
        """Edit a Material object and persists it in the database.
        """
        pass

    @abstractmethod
    def register_movement(self, movement: Movement) -> bool:
        """Create a Movement object and stores it in the database.
        """
        pass

    @abstractmethod
    def list_movements(self) -> list:
        """Get list of Movement objects from database.
        """
        pass
