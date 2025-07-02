
class InventoryManagement:
    def __init__(self, inventory=None):
        """Iniciliza los atributos
        Argumentos posicionales:
        inventory - diccionario que almacena {producto: cantidad} 
        """
        if inventory is None:
            self._inventory = {} # Inventario por defecto {}
        else:
            self._inventory = inventory
    
    def add_product(self, product, quantity):
        """Añade un nuevo producto. Si ya existe se suma la cantidad a la que ya tenía"""
        if quantity < 0 : # La cantidad ha de ser un número positivo
            raise ValueError()

        if product in self._inventory: # Si el producto ya existe, se suma la cantidad.
            self._inventory[product] += quantity
            print(f"{product} ya existe. Se ha añadido {quantity} más.")
        else:
            self._inventory[product] = quantity
            print(f"Se ha añadido correctamente.")
    
    def delete_product(self, product):
        """Elimina un producto. Si no existe printa un mensaje de error"""
        if product in self._inventory:
            self._inventory.pop(product) # elimina el producto del inventario
            print(f"{product} se ha eliminado correctamente.")
        else:
            print(f"ERROR: {product} no encontrado para eliminar.")

    def consult_product(self, product):
        """Consulta un producto del inventario (producto y cantidad). Si no existe printa un error"""
        if product in self._inventory:
            print(f"La cantidad de {product} es {self._inventory.get(product)}")
        else:
            print(f"ERROR: {product} no existe en el inventario.")

    def mod_quantity(self, product, new_quantity): 
        """Modifica la cantidad de un producto"""
        if new_quantity < 0: # La nueva cantidad ha de ser positiva
            raise ValueError()
        if product in self._inventory:
            self._inventory[product] = new_quantity
            print(f"Se ha modificado correctamente.")
        else:
           raise KeyError() # Si no está el producto lanza un KeyError

    def find_product(self, text):
        """Busca productos que contengan el fragmento de texto"""
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
        """Muestra por pantalla el inventario con los los produtos y sus respectivas cantidades"""
        print("\n--- Inventario ---")
        keys = sorted(self._inventory.keys()) if sort else self._inventory.keys()
        for elem in keys:
            print(f'{elem}: {self._inventory[elem]}')
        print("------------------")





