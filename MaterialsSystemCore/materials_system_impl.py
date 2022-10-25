from MaterialsSystemCore.materials_system import IMaterialsSystem
from Database.mssql_connector import MSSQLConnector
from Model.models import Material, Movement


def check_material(material: Material):
    # TODO: Convert price and quantity to int and verify that is not negative and integer.
    if material.id == "":
        print("No ID in material..")
        return False
    if material.name == "":
        print("No name in material..")
        return False
    if material.price == "":
        print("No price in material..")
        return False
    if material.quantity == "":
        print("No quantity in material..")
        return False
    return True


class MaterialsSystem(IMaterialsSystem):

    def __init__(self):
        self.connector = MSSQLConnector.cursor

    def create_material(self, material: Material) -> bool:
        """Overrides IMaterialsSystem.create_material()"""
        if not check_material(material):
            print("Material has invalid data..")
            return False

        print("The material to add: " + str(material))

        query = """
                INSERT INTO MATERIALS (NAME, PRICE, QUANTITY)
                VALUES('%s', %s, %s)
                """ % (material.name, material.price, material.quantity)

        print(query)

        with self.connector as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            cursor.commit()

        return True

    def edit_material(self, material: Material, material_id: int) -> bool:
        """Overrides IMaterialsSystem.edit_material()"""
        if not check_material(material):
            print("Material has invalid data..")
            return False

        print("The material to edit: " + str(material))

        return True

    def register_movement(self) -> bool:
        """Overrides IMaterialsSystem.register_movement()"""
        movement = Movement(movement_type="buy", material_quantity=5, )
        pass

    def list_movements(self) -> list:
        """Overrides IMaterialsSystem.list_movements()"""
        pass
