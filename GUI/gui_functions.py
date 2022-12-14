from datetime import datetime

from GUI.gui import treeview_movements, treeview_materials, code_entry, name_entry, price_entry, \
    quantity_material_entry, \
    type_entry, quantity_movement_entry, date_entry, buttons_frame, show_window, buttons_frame_movements
from MaterialsSystemCore.materials_system_impl import MaterialsSystem
from tkinter import END
from tkinter.ttk import Button

from Model.models import Material, Movement


class SelectedData:
    selected_material, selected_movement = None, None
    material_index, movement_index = 0, 0
    alert = False


def get_materials(connector):
    with connector as connection:
        query = """
                SELECT * FROM MATERIALS
                """
        cursor = connection.cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        materials = []

        for i in results:
            materials.append(Material(id=i[0], name=i[1], price=i[2], quantity=i[3]))
        return materials


def refresh_data(material_system):
    """
    Refresh the data in the tree views.
    """
    fill_treeview_materials(get_materials(material_system.connector))
    fill_treeview_movements(material_system.list_movements(), get_materials(material_system.connector))


def fill_treeview_materials(materials):
    for item in treeview_materials.get_children():
        treeview_materials.delete(item)

    count = 0
    for material in materials:
        _values = (
            material.id,
            material.name,
            material.price,
            material.quantity
        )
        if count % 2 == 0:
            treeview_materials.insert(parent='',
                                      index='end',
                                      iid=str(count),
                                      text='',
                                      values=_values,
                                      tags=('even-row',))
        else:
            treeview_materials.insert(parent='',
                                      index='end',
                                      iid=str(count),
                                      text='',
                                      values=_values,
                                      tags=('odd-row',))
        # Increment counter
        count += 1


def fill_treeview_movements(movements, materials):
    for item in treeview_movements.get_children():
        treeview_movements.delete(item)

    count = 0
    for movement in movements:
        material = [m for m in materials if m.id == movement.material_id]
        _values = (
            movement.date,
            movement.movement_type,
            material[0].name if material else "Elemento Eliminado",
            movement.material_quantity
        )
        if count % 2 == 0:
            treeview_movements.insert(parent='',
                                      index='end',
                                      iid=str(count),
                                      text='',
                                      values=_values,
                                      tags=('even-row',))
        else:
            treeview_movements.insert(parent='',
                                      index='end',
                                      iid=str(count),
                                      text='',
                                      values=_values,
                                      tags=('odd-row',))
        # Increment counter
        count += 1


def select_material_data(event):
    # Clear entry boxes.
    code_entry.delete(0, END)
    name_entry.delete(0, END)
    price_entry.delete(0, END)
    quantity_material_entry.delete(0, END)

    # Grab data Number
    selected = treeview_materials.focus()

    # Grab data Values
    values = treeview_materials.item(selected, 'values')

    if not values:
        return

    # Output to entry boxes

    code_entry.insert(0, values[0])
    name_entry.insert(0, values[1])
    price_entry.insert(0, values[2])
    quantity_material_entry.insert(0, values[3])

    # SelectedData.selected_material = RRHHSystem.employees[int(selected)]
    SelectedData.material_index = code_entry.get()
    print("Selected material code: " + str(SelectedData.material_index))


def new_material():
    return Material(
        id=code_entry.get(),
        name=name_entry.get(),
        price=price_entry.get(),
        quantity=quantity_material_entry.get())


def new_movement():

    if code_entry.get() is None:
        print("No material selected")
        return
    date = datetime(year=date_entry.get_date().year, month=date_entry.get_date().month, day=date_entry.get_date().day)

    return Movement(
        id=1,
        movement_type=type_entry.get(),
        material_quantity=quantity_movement_entry.get(),
        material_id=int(code_entry.get()),
        date=date
    )


def select_movement_data(e):
    # Clear entry boxes.
    date_entry.delete(0, END)
    type_entry.delete(0, END)
    quantity_movement_entry.delete(0, END)

    # Grab data Number
    selected = treeview_movements.focus()

    # Grab data Values
    values = treeview_movements.item(selected, 'values')
    if not values:
        return

    # Output to entry boxes
    date_entry.insert(0, values[0])
    type_entry.insert(0, values[1])
    quantity_movement_entry.insert(0, values[2])

    # SelectedData.selected_contract = RRHHSystem.contracts[int(selected)]
    # SelectedData.contract_index = int(selected)


def run_gui(materials_system: MaterialsSystem):
    # Capture click up event.
    treeview_materials.bind("<ButtonRelease-1>", select_material_data)
    treeview_movements.bind("<ButtonRelease-1>", select_movement_data)

    create_material_button = Button(buttons_frame, text="Crear",
                                    command=lambda: [materials_system.create_material(new_material()),
                                                     refresh_data(materials_system)])
    create_material_button.grid(row=0, column=0, padx=10, pady=10)

    update_material_button = Button(buttons_frame, text="Actualizar",
                                    command=lambda: [materials_system.edit_material(new_material(),
                                                                                    SelectedData.material_index),
                                                     refresh_data(materials_system)])
    update_material_button.grid(row=0, column=1, padx=10, pady=10)

    register_movement_button = Button(buttons_frame_movements, text="Registrar",
                                      command=lambda: [materials_system.register_movement(new_movement()),
                                                       refresh_data(materials_system)])
    register_movement_button.grid(row=0, column=0, padx=10, pady=10)

    fill_treeview_materials(get_materials(materials_system.connector))

    fill_treeview_movements(materials_system.list_movements(), get_materials(materials_system.connector))

    # Show GUI.
    show_window()
