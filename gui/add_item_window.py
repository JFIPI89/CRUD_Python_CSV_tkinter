import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from utils.csv_operations import write_csv, read_csv
from utils.validation import validate_sku

class AddItemWindow(tk.Toplevel):
    def __init__(self, parent, sku=None):
        super().__init__(parent)
        self.title("Agregar Ítem")
        self.geometry("400x350")

        # Campo SKU (solo lectura si se pasa un SKU)
        tk.Label(self, text="SKU").grid(row=0, column=0, padx=10, pady=5)
        self.sku_entry = tk.Entry(self)
        self.sku_entry.grid(row=0, column=1, padx=10, pady=5)
        if sku:
            self.sku_entry.insert(0, sku)
            self.sku_entry.config(state='readonly')
        
        # Otros campos de entrada
        tk.Label(self, text="Artículo").grid(row=1, column=0, padx=10, pady=5)
        self.item_entry = tk.Entry(self)
        self.item_entry.grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Marca").grid(row=2, column=0, padx=10, pady=5)
        self.brand_entry = tk.Entry(self)
        self.brand_entry.grid(row=2, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Modelo").grid(row=3, column=0, padx=10, pady=5)
        self.model_entry = tk.Entry(self)
        self.model_entry.grid(row=3, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Departamento").grid(row=4, column=0, padx=10, pady=5)
        self.department_entry = tk.Entry(self)
        self.department_entry.grid(row=4, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Clase").grid(row=5, column=0, padx=10, pady=5)
        self.class_entry = tk.Entry(self)
        self.class_entry.grid(row=5, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Familia").grid(row=6, column=0, padx=10, pady=5)
        self.family_entry = tk.Entry(self)
        self.family_entry.grid(row=6, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Cantidad").grid(row=7, column=0, padx=10, pady=5)
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.grid(row=7, column=1, padx=10, pady=5)
        
        tk.Label(self, text="Stock").grid(row=8, column=0, padx=10, pady=5)
        self.stock_entry = tk.Entry(self)
        self.stock_entry.grid(row=8, column=1, padx=10, pady=5)
        
        self.add_button = tk.Button(self, text="Agregar", command=self.add_item)
        self.add_button.grid(row=9, column=0, columnspan=2, pady=10)
    
    def add_item(self):
        sku = self.sku_entry.get().strip()
        item = self.item_entry.get().strip()
        brand = self.brand_entry.get().strip()
        model = self.model_entry.get().strip()
        department = self.department_entry.get().strip()
        class_ = self.class_entry.get().strip()
        family = self.family_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        stock = self.stock_entry.get().strip()
        
        # Validaciones
        if not all([sku, item, brand, model, department, class_, family, quantity, stock]):
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return
        
        if not quantity.isdigit() or not stock.isdigit():
            messagebox.showwarning("Advertencia", "Cantidad y Stock deben ser numéricos.")
            return
        
        quantity = int(quantity)
        stock = int(stock)
        
        if quantity > stock:
            messagebox.showwarning("Advertencia", "La cantidad no puede ser mayor al stock.")
            return
        
        data = read_csv('data/items.csv')
        
        if validate_sku(sku, data):
            messagebox.showwarning("Advertencia", "El SKU ya existe.")
            return
        
        new_item = {
            'SKU': sku,
            'Artículo': item,
            'Marca': brand,
            'Modelo': model,
            'Departamento': department,
            'Clase': class_,
            'Familia': family,
            'Cantidad': quantity,
            'Stock': stock
        }
        
        data.append(new_item)
        write_csv('data/items.csv', data)
        messagebox.showinfo("Éxito", "Ítem agregado exitosamente.")
        self.destroy()
