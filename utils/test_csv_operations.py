from utils.csv_operations import read_csv, write_csv, update_csv, delete_from_csv

def test_csv_operations():
    filename = 'test.csv'
    # Datos de prueba
    data = [
        {'SKU': '001', 'Name': 'Item 1', 'Stock': '100'},
        {'SKU': '002', 'Name': 'Item 2', 'Stock': '200'}
    ]

    # Escribir datos en el archivo CSV
    write_csv(filename, data)

    # Leer datos del archivo CSV
    read_data = read_csv(filename)
    assert read_data == data, f"Expected {data}, but got {read_data}"

    # Actualizar datos
    update_csv(filename, '001', {'Name': 'Updated Item 1', 'Stock': '150'})
    updated_data = read_csv(filename)
    assert updated_data[0]['Name'] == 'Updated Item 1', "Update failed"

    # Eliminar datos
    delete_from_csv(filename, '002')
    remaining_data = read_csv(filename)
    assert len(remaining_data) == 1, "Delete failed"

    print("CSV operations test passed.")

if __name__ == "__main__":
    test_csv_operations()
