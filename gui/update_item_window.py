import tkinter as tk
from tkinter import messagebox
from utils.csv_operations import read_csv, update_csv
from utils.validation import validate_sku

class UpdateItemWindow(tk.Toplevel):
    def __init__(self, parent, sku):
        super().__init__(parent)
        self.title("Actualizar Ítem")
        self.geometry("700x400")
        
        self.sku = sku
        self.data = read_csv('data/items.csv')
        self.item_data = next((item for item in self.data if item['SKU'] == sku), None)
        
        if not self.item_data:
            messagebox.showerror("Error", "SKU no encontrado.")
            self.destroy()
            return
        
        # Crear campos para cada dato
        tk.Label(self, text="SKU").grid(row=0, column=0, padx=10, pady=5)
        self.sku_entry = tk.Entry(self, state='readonly')
        self.sku_entry.grid(row=0, column=1, padx=10, pady=5)
        self.sku_entry.insert(0, self.item_data['SKU'])
        
        tk.Label(self, text="Artículo").grid(row=1, column=0, padx=10, pady=5)
        self.item_entry = tk.Entry(self)
        self.item_entry.grid(row=1, column=1, padx=10, pady=5)
        self.item_entry.insert(0, self.item_data['Artículo'])
        
        tk.Label(self, text="Marca").grid(row=2, column=0, padx=10, pady=5)
        self.brand_entry = tk.Entry(self)
        self.brand_entry.grid(row=2, column=1, padx=10, pady=5)
        self.brand_entry.insert(0, self.item_data['Marca'])
        
        tk.Label(self, text="Modelo").grid(row=3, column=0, padx=10, pady=5)
        self.model_entry = tk.Entry(self)
        self.model_entry.grid(row=3, column=1, padx=10, pady=5)
        self.model_entry.insert(0, self.item_data['Modelo'])
        
        tk.Label(self, text="Departamento").grid(row=4, column=0, padx=10, pady=5)
        self.department_entry = tk.Entry(self)
        self.department_entry.grid(row=4, column=1, padx=10, pady=5)
        self.department_entry.insert(0, self.item_data['Departamento'])
        
        tk.Label(self, text="Clase").grid(row=5, column=0, padx=10, pady=5)
        self.class_entry = tk.Entry(self)
        self.class_entry.grid(row=5, column=1, padx=10, pady=5)
        self.class_entry.insert(0, self.item_data['Clase'])
        
        tk.Label(self, text="Familia").grid(row=6, column=0, padx=10, pady=5)
        self.family_entry = tk.Entry(self)
        self.family_entry.grid(row=6, column=1, padx=10, pady=5)
        self.family_entry.insert(0, self.item_data['Familia'])
        
        tk.Label(self, text="Cantidad").grid(row=7, column=0, padx=10, pady=5)
        self.quantity_entry = tk.Entry(self)
        self.quantity_entry.grid(row=7, column=1, padx=10, pady=5)
        self.quantity_entry.insert(0, self.item_data['Cantidad'])
        
        tk.Label(self, text="Stock").grid(row=8, column=0, padx=10, pady=5)
        self.stock_entry = tk.Entry(self)
        self.stock_entry.grid(row=8, column=1, padx=10, pady=5)
        self.stock_entry.insert(0, self.item_data['Stock'])
        
        self.update_button = tk.Button(self, text="Actualizar", command=self.update_item)
        self.update_button.grid(row=9, column=0, columnspan=2, pady=10)
    
    def update_item(self):
        item = self.item_entry.get().strip()
        brand = self.brand_entry.get().strip()
        model = self.model_entry.get().strip()
        department = self.department_entry.get().strip()
        class_ = self.class_entry.get().strip()
        family = self.family_entry.get().strip()
        quantity = self.quantity_entry.get().strip()
        stock = self.stock_entry.get().strip()
        
        if not all([item, brand, model, department, class_, family, quantity, stock]):
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
        
        updated_data = {
            'Artículo': item,
            'Marca': brand,
            'Modelo': model,
            'Departamento': department,
            'Clase': class_,
            'Familia': family,
            'Cantidad': quantity,
            'Stock': stock
        }
        
        update_csv('data/items.csv', self.sku, updated_data)
        messagebox.showinfo("Éxito", "Ítem actualizado exitosamente.")
        self.destroy()
