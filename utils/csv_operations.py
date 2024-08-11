import csv
import os

def read_csv(filename):
    """Lee el contenido del archivo CSV y devuelve los datos como una lista de diccionarios."""
    if not os.path.exists(filename):
        # Si el archivo no existe, devuelve una lista vacía
        return []
    
    with open(filename, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)

def write_csv(filename, data):
    """Escribe los datos en el archivo CSV."""
    if not data:
        return
    
    with open(filename, mode='w', newline='') as file:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def update_csv(filename, search_key, updated_data):
    """Actualiza un registro existente en el archivo CSV."""
    data = read_csv(filename)
    for item in data:
        if item['SKU'] == search_key:
            item.update(updated_data)
            break
    write_csv(filename, data)

def delete_from_csv(filename, search_key):
    """Elimina un registro del archivo CSV."""
    data = read_csv(filename)
    data = [item for item in data if item['SKU'] != search_key]
    write_csv(filename, data)
