from pyodbc import InterfaceError
from MaterialsSystemCore.materials_system_impl import MaterialsSystem
from GUI.gui_functions import run_gui


def run():
    materials_system = MaterialsSystem()

    run_gui(materials_system)


if __name__ == "__main__":
    run()
