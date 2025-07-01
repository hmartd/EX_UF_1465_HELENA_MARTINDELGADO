def print_comb(invertido=False):
    """Genera todas las combinaciones de tres dígitos (del 0 al 9) sin repetir dígitos, en orden ascendente.
    Si invertido=True, las muestra en orden descendente.
    """
    combinaciones = []

    for i in range(10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                combinaciones.append(f"{i}{j}{k}")     
    
    if invertido:
        for i in range(len(combinaciones) - 1, -1, -1):
            if i > 0:
                print(combinaciones[i], end=", ")
            else:
                print(combinaciones[i], end="")
    else:
        for i in range(len(combinaciones)):
            if i < len(combinaciones) - 1:
                print(combinaciones[i], end=", ")
            else:
                print(combinaciones[i], end="") 



def main():
    invertido = input("¿Quieres ver las combinaciones en orden invertido? (s/n): ").lower().strip()
    if invertido == "s":
        invertido = True
    elif invertido == "n":
        invertido = False
    else:
        print("Entrada no válida. Debes introducir 's' o 'n'.")
        return
    
    print_comb(invertido)


if __name__ == "__main__":
    main()