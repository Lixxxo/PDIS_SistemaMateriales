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


def check_movement(movement: Movement):
    # TODO: Convert price and quantity to int and verify that is not negative and integer.
    if movement.id == "":
        print("No ID in movement..")
        return False
    if movement.movement_type == "":
        print("No movement type in movement..")
        return False
    if movement.material_quantity == "":
        print("No material quantity in movement..")
        return False
    if movement.date == "":
        print("No date in movement..")
        return False
    if movement.material_id == "":
        print("No material id in movement..")
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

        query = """
                UPDATE MATERIALS 
                SET NAME = '%s', PRICE = %s, QUANTITY = %s
                WHERE ID = %s
                """ % (material.name, material.price, material.quantity, material_id)

        with self.connector as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            cursor.commit()

        return True

    def register_movement(self, movement: Movement) -> bool:
        """Overrides IMaterialsSystem.register_movement()"""
        if not check_movement(movement):
            print("Movement has invalid data..")
            return False

        print("The movement to add: " + str(movement))

        # TODO: Hacer la query para registrar un movimiento en la base de datos (Joel).

        query = """
                INSERT INTO MOVEMENTS (MOVEMENTTYPE, MATERIALQUANTITY, DATE, MOVEMENTID)
                VALUES('%s', %s, %s, %s)
                """ % (movement.movement_type, movement.material_quantity, movement.date, movement.id)

        with self.connector as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            cursor.commit()

        return True

    def list_movements(self) -> list:

        # TODO: Hacer este requerimiento (Joel).
        """Overrides IMaterialsSystem.list_movements()"""
        pass
