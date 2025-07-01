def print_comb(invertido):
    """Genera todas las combinaciones de tres dígitos (del 0 al 9) sin repetir dígitos"""
    result = ""

    if invertido == False:
        for i in range(10):
            for j in range (i+1, 10):
                for k in range (j+1, 10):
                    result += (f'{i}{j}{k}, ')      
    else:
        for k in range(9, -1, -1):
            for j in range (k-1, -1, -1):
                for i in range (j-1, -1, -1):
                    result += (f'{i}{j}{k}, ')
    
    # eliminar el último ', '
    result = result[:-2]
    print(result)


def main():
    invertido = input("¿Quieres ver las combinaciones en orden invertido? (s/n): ")
    if invertido == "s":
        invertido = True
    elif invertido == "n":
        invertido = False
    else:
        print("ERROR -> Los valores válidos son: s/n")
        return
    
    print_comb(invertido)


if __name__ == "__main__":
    main()