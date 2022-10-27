from MaterialsSystemCore.materials_system import IMaterialsSystem
from Database.mssql_connector import MSSQLConnector
from Model.models import Material, Movement
from MaterialsSystemCore import utils


def check_material(material: Material):
    if not material.price.isnumeric():
        print("NaN price in material")
        return False
    if not material.quantity.isnumeric():
        print("NaN quantity in material")
        return False
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

    if not movement.material_quantity.isnumeric():
        print("NaN quantity in movement")
        return False
    if movement.movement_type == "":
        print("No movement type in movement..")
        return False
    if movement.movement_type.lower() not in ["compra", "venta"]:
        print(movement.movement_type.lower(), "Invalid movement_type, use one from:\n\t\t", ["compra", "venta"])
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
        math_operator = ""
        if movement.movement_type.lower() == "compra":
            math_operator = '+'
        elif movement.movement_type.lower() == "venta":
            math_operator = '-'

        query = """
                UPDATE MATERIALS 
                SET QUANTITY = QUANTITY %s %s
                WHERE ID = %s
                """ % (math_operator, movement.material_quantity, movement.material_id)

        with self.connector as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            cursor.commit()

        query = """
                INSERT INTO MOVEMENTS (MOVEMENTTYPE, MATERIALQUANTITY, DATE, MATERIALID)
                VALUES('%s', %s, CONVERT(DATE, '%s'), %s)
                """ % (movement.movement_type, movement.material_quantity, movement.date.date(), movement.material_id)

        with self.connector as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            cursor.commit()

        return True

    def list_movements(self) -> list:

        """Overrides IMaterialsSystem.list_movements()"""
        query = """
                SELECT ID, MOVEMENTTYPE, MATERIALQUANTITY, DATE, MATERIALID
                FROM MOVEMENTS;
                """
        with self.connector as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()

            movements = []

            for i in results:
                movements.append(Movement(id=i[0], movement_type=i[1],
                                          material_quantity=i[2], date=i[3], material_id=i[4]))
            return movements

