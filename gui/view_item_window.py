import tkinter as tk
from tkinter import ttk
from utils.csv_operations import read_csv

class ViewItemWindow(tk.Toplevel):
    def __init__(self, parent, sku):
        super().__init__(parent)
        self.title("Consultar Ítem")
        self.geometry("1000x400")

        self.sku = sku
        self.data = read_csv('data/items.csv')
        self.item_data = next((item for item in self.data if item['SKU'] == sku), None)
        
        if not self.item_data:
            tk.messagebox.showerror("Error", "SKU no encontrado.")
            self.destroy()
            return

        # Crear el Treeview para mostrar los datos en una tabla
        columns = ('Artículo', 'Marca', 'Modelo', 'Departamento', 'Clase', 'Familia', 'Cantidad', 'Stock')
        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True)

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor=tk.CENTER)

        # Insertar los datos en la tabla
        self.tree.insert('', tk.END, values=(
            self.item_data['Artículo'],
            self.item_data['Marca'],
            self.item_data['Modelo'],
            self.item_data['Departamento'],
            self.item_data['Clase'],
            self.item_data['Familia'],
            self.item_data['Cantidad'],
            self.item_data['Stock']
        ))
        
        # Agregar un botón para cerrar la ventana
        self.close_button = tk.Button(self, text="Cerrar", command=self.destroy)
        self.close_button.pack(pady=10)
