import inventory_management as im

def mostrar_menu():
    """Menú interactivo con 7 opcioness: 
    1. Añadir productos
    2. Consultar uno
    3. Eliminar uno
    4. Modificar cantidades
    5. Buscar por texto
    6. Mostrar inventario"
    7. Salir del programa
    """
    tienda = im.InventoryManagement()

    while True:
        print("\n-------- Menú --------\n")
        print("1. Añadir productos")
        print("2. Consultar uno")
        print("3. Eliminar uno")
        print("4. Modificar cantidades")
        print("5. Buscar por texto")
        print("6. Mostrar inventario")
        print("7. Salir del programa")
        print("\n----------------------")
        
        try:
            opcion = int(input("\n¿Qué desea hacer? Seleccione un número (1-7): "))
            if opcion < 1 or opcion > 7:
                raise ValueError()
        except ValueError:
            print("Por favor, introduzca un número válido entre 1 y 7.")
            continue
        
        if opcion == 1:
            product = input("\n¿Qué producto quiere añadir?: ").capitalize().strip() # Se eliminan los espacios del principio y final, y se pone la primera letra en Mayúscula
            try:
                quantity = int(input("Cantidad: "))
                tienda.add_product(product, quantity)
            except ValueError:
                print("ERROR: La cantidad debe ser un número entero positivo.")
        elif opcion == 2:
            product = input("\n¿Qué producto quiere consultar?: ").capitalize().strip()
            tienda.consult_product(product)
        elif opcion == 3:
            product = input("\n¿Qué producto quiere eliminar?: ").capitalize().strip()
            tienda.delete_product(product)
        elif opcion == 4:
            product = input("\n¿De qué producto quiere modificar las cantidades?: ").capitalize().strip()
            if product not in tienda._inventory:
                print(f"ERROR: {product} no existe en el inventario.")
                continue
            else:         
                try:           
                    quantity = int(input("Nueva cantidad: "))
                    tienda.mod_quantity(product, quantity)
                except ValueError:
                    print("ERROR: La cantidad ha de ser un número positivo entero.")
        elif opcion == 5:
            busqueda = input("\nBúsqueda por: ").strip()
            tienda.find_product(busqueda)
        elif opcion == 6:
            sort = input("¿Quiere ver el inventario ordenado? (s/n): ").lower().strip()
            if sort == 's':
                tienda.view_inventory(sort)
            elif sort == 'n':
                tienda.view_inventory()
            else:
                print("ERROR: Por favor, introduce un valor válido (s/n).")
                continue
        else:
            print("Saliendo...")
            break


if __name__ == "__main__":
    mostrar_menu()