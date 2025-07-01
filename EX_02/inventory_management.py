
class InventoryManagement:
    def __init__(self, inventory=None):
        """Iniciliza los atributos
        Argumentos posicionales:
        inventory - diccionario que almacena {producto: cantidad} 
        """
        if inventory is None:
            self._inventory = {}
        else:
            self._inventory = inventory
    
    def add_product(self, product, quantity):
        if quantity < 0 :
            raise ValueError()

        if product in self._inventory:
            self._inventory[product] += quantity
            print(f"{product} ya existe. Se ha añadido {quantity} más.")
        else:
            self._inventory[product] = quantity
            print(f"Se ha añadido correctamente.")
    
    def delete_product(self, product):
        if product in self._inventory:
            self._inventory.pop(product)
            print(f"{product} se ha eliminado correctamente.")
        else:
            print(f"ERROR: {product} no encontrado para eliminar.")

    def consult_product(self, product):
        if product in self._inventory:
            print(f"La cantidad de {product} es {self._inventory.get(product)}")
        else:
            print(f"ERROR: {product} no existe en el inventario.")

    def mod_quantity(self, product, new_quantity):
        if new_quantity < 0:
            raise ValueError()
        if product in self._inventory:
            self._inventory[product] = new_quantity
            print(f"Se ha modificado correctamente.")
        else:
           raise KeyError()

    def find_product(self, text):
        text = text.lower().strip()
        found = False
        print("------------------")
        for elem in self._inventory:
            if text in elem.lower():
                print(f'{elem}: {self._inventory[elem]}')
                found = True
        if not found:
            print(f"No se han encontrado resultados para '{text}'.")

    def view_inventory(self, sort=False):
        print("\n--- Inventario ---")
        keys = sorted(self._inventory.keys()) if sort else self._inventory.keys()
        for elem in keys:
            print(f'{elem}: {self._inventory[elem]}')
        print("------------------")





