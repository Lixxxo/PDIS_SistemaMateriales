from abc import abstractmethod
from abc import ABCMeta


class IMaterialsSystem(metaclass=ABCMeta):

    @abstractmethod
    def create_material(self) -> bool:
        """Create a Material object and stores it in the database.
        """
        pass

    @abstractmethod
    def edit_material(self) -> bool:
        """Edit a Material object and persists it in the database.
        """
        pass

    @abstractmethod
    def register_movement(self) -> bool:
        """Create a Movement object and stores it in the database.
        """
        pass

    @abstractmethod
    def list_movements(self) -> list:
        """Get list of Movement objects from database.
        """
        pass
