# utils/procedures.py
from utils.csv_operations import read_csv, write_csv

def add_item(filename, item_data):
    """Agrega un nuevo ítem al archivo CSV."""
    data = read_csv(filename)
    data.append(item_data)
    write_csv(filename, data)

def update_item(filename, sku, updated_data):
    """Actualiza un ítem existente en el archivo CSV."""
    data = read_csv(filename)
    for item in data:
        if item['SKU'] == sku:
            item.update(updated_data)
            break
    write_csv(filename, data)

def delete_item(filename, sku):
    """Elimina un ítem del archivo CSV."""
    data = read_csv(filename)
    data = [item for item in data if item['SKU'] != sku]
    write_csv(filename, data)

