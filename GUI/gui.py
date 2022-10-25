from tkinter import Tk, LEFT, X, RIGHT, Y, NO, W, StringVar
from tkinter.ttk import Button, Treeview, Frame, LabelFrame, Scrollbar, Label, Entry, OptionMenu
from tkcalendar import DateEntry

# Declare the window.
root = Tk()

# Lock the size of the window.
root.resizable(width=False, height=False)

# Set iconbitmap
root.iconbitmap("resources/wood.ico")

# Set the window title
root.title('Gestión de materiales y movimientos')

# Handle header.
header = Frame(root)
header.pack()

# Declare container for both treeview (employees and contracts).
upper_container = Frame(header)
upper_container.pack(pady=10, padx=10)

# Handle Treeview of employees

# Declare left frame.
left_frame = LabelFrame(upper_container, text="Materiales")
left_frame.pack(pady=10, padx=10, side=LEFT)

# Declare Treeview Frame.
treeview_frame = Frame(left_frame)
treeview_frame.pack(pady=10, fill=X)

# Declare Treeview Scrollbar.
treeview_scroll = Scrollbar(treeview_frame)
treeview_scroll.pack(fill=Y, side=RIGHT)

# Declare Employees Treeview.
treeview_materials = Treeview(treeview_frame, yscrollcommand=treeview_scroll.set, selectmode="extended", padding="5px")
treeview_materials.pack(fill=X, padx=10)

# Configure the Scrollbar.
treeview_scroll.config(command=treeview_materials.yview)

# Define Columns
treeview_materials['columns'] = ('code',
                                 'name',
                                 'price',
                                 'quantity')

# Format Columns
treeview_materials.column('#0', width=0, stretch=NO)
treeview_materials.column("code", anchor=W, width=50)
treeview_materials.column("name", anchor=W, width=200)
treeview_materials.column("price", anchor=W, width=100)
treeview_materials.column("quantity", anchor=W, width=100)

# Creating Headings
treeview_materials.heading("#0", text="", anchor=W)
treeview_materials.heading("code", text="Código", anchor=W)
treeview_materials.heading("name", text="Nombre", anchor=W)
treeview_materials.heading("price", text="Precio", anchor=W)
treeview_materials.heading("quantity", text="Cantidad", anchor=W)

# Add striped row tags.
treeview_materials.tag_configure('odd-row', background="White")
treeview_materials.tag_configure('even-row', background="lightblue")

# Add data entry boxes.
data_frame = LabelFrame(left_frame, text="Material")
data_frame.pack(fill="both", expand=True, padx=10, pady=10)

code_label = Label(data_frame, text="Código")
code_label.grid(row=0, column=0, padx=10, pady=10)
code_entry = Entry(data_frame)
code_entry.grid(row=0, column=1, padx=10, pady=10)

name_label = Label(data_frame, text="Nombre")
name_label.grid(row=0, column=2, padx=10, pady=10)
name_entry = Entry(data_frame)
name_entry.grid(row=0, column=3, padx=10, pady=10)

price_label = Label(data_frame, text="Precio")
price_label.grid(row=1, column=0, padx=10, pady=10)
price_entry = Entry(data_frame)
price_entry.grid(row=1, column=1, padx=10, pady=10)

quantity_material_label = Label(data_frame, text="Cantidad")
quantity_material_label.grid(row=1, column=2, padx=10, pady=10)
quantity_material_entry = Entry(data_frame)
quantity_material_entry.grid(row=1, column=3, padx=10, pady=10)

# Add buttons.
buttons_frame = LabelFrame(left_frame, text="Acciones")
buttons_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Handle Treeview of contracts.

# Declare right Frame.
right_frame = LabelFrame(upper_container, text="Movimientos")
right_frame.pack(pady=10, padx=10, side=RIGHT, fill=Y)

# Declare Treeview Frame.
treeview_frame = Frame(right_frame)
treeview_frame.pack(pady=10, fill=X)

# Declare Treeview Scrollbar.
treeview_scroll = Scrollbar(treeview_frame)
treeview_scroll.pack(pady=10, side=RIGHT, fill=Y)

# Declare Contracts Treeview.
treeview_movements = Treeview(treeview_frame, yscrollcommand=treeview_scroll.set, selectmode="extended", padding="5px")
treeview_movements.pack(fill=X, padx=10)

# Configure the Scrollbar.
treeview_scroll.config(command=treeview_movements.yview)

# Define Columns
treeview_movements['columns'] = ('date',
                                 'type',
                                 'quantity')
# Format Columns
treeview_movements.column('#0', width=0, stretch=NO)
treeview_movements.column("date", anchor=W, width=100)
treeview_movements.column("type", anchor=W, width=150)
treeview_movements.column("quantity", anchor=W, width=100)

# Creating Headings
treeview_movements.heading("#0", text="", anchor=W)
treeview_movements.heading("date", text="Fecha", anchor=W)
treeview_movements.heading("type", text="Tipo de movimiento", anchor=W)
treeview_movements.heading("quantity", text="Cantidad", anchor=W)

# Add striped row tags.
treeview_movements.tag_configure('odd-row', background="White")
treeview_movements.tag_configure('even-row', background="lightblue")

# Add data entry boxes.
data_frame = LabelFrame(right_frame, text="Movimiento")
data_frame.pack(fill="both", expand=True, padx=10, pady=10)

date_label = Label(data_frame, text="Fecha")
date_label.grid(row=0, column=0, padx=10, pady=10)
date_entry = DateEntry(data_frame, selectmode='day', date_pattern='dd-MM-yyyy')
date_entry.grid(row=0, column=1, padx=10, pady=10)

type_label = Label(data_frame, text="Tipo de movimiento")
type_label.grid(row=0, column=2, padx=10, pady=10)
type_entry = Entry(data_frame)
type_entry.grid(row=0, column=3, padx=10, pady=10)

quantity_movement_label = Label(data_frame, text="Cantidad")
quantity_movement_label.grid(row=1, column=0, padx=10, pady=10)
quantity_movement_entry = Entry(data_frame)
quantity_movement_entry.grid(row=1, column=1, padx=10, pady=10)

bottom = LabelFrame(header, text="Lectura y escritura de archivos")
bottom.pack(fill="both", padx=20, pady=20)

# Add buttons.
buttons_frame_movements = LabelFrame(right_frame, text="Acciones")
buttons_frame_movements.pack(fill="both", expand=False, padx=10, pady=10)


def show_window():
    root.mainloop()
