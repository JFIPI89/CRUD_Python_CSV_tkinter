# utils/validation.py
def validate_sku(sku, data):
    """Verifica si el SKU ya existe en el archivo CSV."""
    return any(item['SKU'] == sku for item in data)

def validate_quantity(quantity, stock):
    """Verifica si la cantidad no supera el stock disponible."""
    return quantity <= stock
