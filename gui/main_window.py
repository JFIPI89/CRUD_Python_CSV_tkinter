import tkinter as tk
from tkinter import messagebox
from gui.add_item_window import AddItemWindow
from gui.update_item_window import UpdateItemWindow
from gui.delete_item_window import DeleteItemWindow
from gui.view_item_window import ViewItemWindow
from utils.csv_operations import read_csv
from utils.validation import validate_sku


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        self.geometry("400x300")
        
        tk.Label(self, text="SKU").pack(pady=10)
        self.sku_entry = tk.Entry(self)
        self.sku_entry.pack(pady=10)
        
        self.check_button = tk.Button(self, text="Verificar SKU", command=self.check_sku)
        self.check_button.pack(pady=10)
        
        self.buttons_frame = tk.Frame(self)
        self.buttons_frame.pack(pady=10)
    
    def check_sku(self):
        sku = self.sku_entry.get().strip()
        data = read_csv('data/items.csv')
        
        if validate_sku(sku, data):
            self.show_options(sku)
        else:
            self.show_add_form(sku)
    
    def show_options(self, sku):
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
        
        tk.Button(self.buttons_frame, text="Consultar", command=lambda: self.show_view_form(sku)).pack(side=tk.LEFT, padx=5)
        tk.Button(self.buttons_frame, text="Actualizar", command=lambda: self.show_update_form(sku)).pack(side=tk.LEFT, padx=5)
        tk.Button(self.buttons_frame, text="Eliminar", command=lambda: self.show_delete_form(sku)).pack(side=tk.LEFT, padx=5)
    
    def show_add_form(self, sku):
        AddItemWindow(self, sku)
    
    def show_update_form(self, sku):
        UpdateItemWindow(self, sku)
    
    def show_delete_form(self, sku):
        DeleteItemWindow(self, sku)
    
    def show_view_form(self, sku):
        ViewItemWindow(self, sku)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
