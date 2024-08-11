import tkinter as tk
from tkinter import messagebox
from utils.csv_operations import delete_from_csv, read_csv
from utils.validation import validate_sku


class DeleteItemWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Eliminar Ítem")
        self.geometry("300x150")
        
        tk.Label(self, text="SKU").pack(pady=10)
        self.sku_entry = tk.Entry(self)
        self.sku_entry.pack(pady=10)
        
        self.delete_button = tk.Button(self, text="Eliminar", command=self.delete_item)
        self.delete_button.pack(pady=10)
    
    def delete_item(self):
        sku = self.sku_entry.get().strip()
        
        if not validate_sku(sku, read_csv('data/items.csv')):
            messagebox.showwarning("Advertencia", "SKU no encontrado.")
            return
        
        if messagebox.askyesno("Confirmación", "¿Está seguro de que desea eliminar este ítem?"):
            delete_from_csv('data/items.csv', sku)
            messagebox.showinfo("Éxito", "Ítem eliminado exitosamente.")
            self.destroy()

