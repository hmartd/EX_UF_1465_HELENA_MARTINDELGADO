
class InventoryManagement:
    def __init__(self, inventory={}):
        """Iniciliza los atributos
        Argumentos posicionales:
        inventory - diccionario que almacena {product: quantity} 
        """
        self._inventory = inventory
    
    def add_product(self, product, quantity):
        print(f"\nAñadir al inventario {product}-> Cantidad {quantity}:")
        if quantity < 0 or type(quantity) != int:
            print("ERROR: La cantidad debe ser un número entero positivo")
            return

        if product in self._inventory:
            self._inventory[product] += quantity
            print(f"{product} ya existe. Se ha añadido {quantity} más")
        else:
            self._inventory[product] = quantity
            print(f"Se ha añadido correctamente")
    
    def delete_product(self, product):
        print(f"\nEliminar {product}:")
        if product in self._inventory:
            self._inventory.pop(product)
            print(f"{product} se ha eliminado correctamente")
        else:
            print(f"ERROR: {product} no encontrado para eliminar")

    def consult_product(self, product):
        print(f"\nConsultar {product}:")
        if product in self._inventory:
            print(f"La cantidad de {product} es {self._inventory.get(product)}")
        else:
            print(f"ERROR: {product} no existe en el inventario")

    def mod_quantity(self, product, new_quantity):
        print(f"\nModificar cantidad de {product} por {new_quantity}:")
        if new_quantity <0 or type(new_quantity) != int:
            print("ERROR: la cantidad ha de ser un número positivo entero")
            return
        if product in self._inventory:
            self._inventory[product] = new_quantity
            print(f"Se ha modificado correctamente")
        else:
            print(f"ERROR: {product} no existe en el inventario")

    def find_product(self, text):
        print(f"")
        pass

    def view_inventory(self, sort=False):
        print("\n--- Inventario ---")
        for elem in self._inventory:
            print(f'{elem}: {self._inventory[elem]}')
        print("------------------")


tienda = InventoryManagement()

print("\nInventario inicial:")
tienda.view_inventory() 

# Añadir Producto
tienda.add_product("Manzanas", 10)
tienda.view_inventory()

tienda.add_product("Peras", 5)
tienda.view_inventory()

tienda.add_product("Manzanas", 5)  
tienda.view_inventory()

# Consultar Producto
tienda.consult_product("Manzanas")

# Eliminar Producto
tienda.delete_product("Peras")
tienda.view_inventory()

# Modificar cantidad de Producto
tienda.mod_quantity("Manzanas", 50)
tienda.view_inventory()

