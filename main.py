from pyodbc import InterfaceError
from MaterialsSystemCore.materials_system_impl import MaterialsSystem
from GUI.gui_functions import run_gui


def run():
    ms = MaterialsSystem()

    run_gui(ms)


if __name__ == "__main__":
    run()
