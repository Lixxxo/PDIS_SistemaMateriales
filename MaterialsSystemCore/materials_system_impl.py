from MaterialsSystemCore.materials_system import IMaterialsSystem
from Database.mssql_connector import MSSQLConnector
from Model.models import Material, Movement


class MaterialsSystem(IMaterialsSystem):

    def __init__(self):
        self.connector = MSSQLConnector.cursor

    def create_material(self) -> int:
        """Overrides IMaterialsSystem.create_material()"""
        material = Material(name="Metal", price=400_000, quantity=500)
        pass

    def edit_material(self) -> bool:
        """Overrides IMaterialsSystem.edit_material()"""
        pass

    def register_movement(self) -> bool:
        """Overrides IMaterialsSystem.register_movement()"""
        movement = Movement(movement_type="buy", material_quantity=5,)
        pass

    def list_movements(self) -> list:
        """Overrides IMaterialsSystem.list_movements()"""
        pass

