warehouse_a = {"widgets": 50, "gadgets": 20, "gizmos": 15}
warehouse_b = {"gadgets": 30, "gizmos": 10, "sprockets": 25}

def merge_inventory(warehouse_a, warehouse_b):
    merged_warehouse = {}

    for key, value in warehouse_a.items():
        merged_warehouse[key] = value

    for key, value in warehouse_b.items():
        merged_warehouse[key] = merged_warehouse.get(key, 0) + value

    return merged_warehouse

def low_stock(inventory, threshold=20):
    low_items = []
    for key, value in inventory.items():
        if value < threshold:
            low_items.append(key)
    return low_items

def restock(inventory, item, amount):
    new_stock = {}
    for key, value in inventory.items():
        new_stock[key] = value

    new_stock[item] = new_stock.get(item, 0) + amount

    return new_stock

print(merge_inventory(warehouse_a, warehouse_b))
print(low_stock(warehouse_b, threshold=20))
print( restock({"widgets": 50}, "widgets", 10))