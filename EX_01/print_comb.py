def print_comb(invertido=False):
    """Genera todas las combinaciones de tres dígitos (del 0 al 9) sin repetir dígitos"""
    result = ""

    for i in range(10):
        for j in range (i+1, 10):
            for k in range (j+1, 10):
                result += (f'{i}{j}{k}, ')
    
    # eliminar el último ', '
    result = result[:-2]
    print(result)




def main():
    print_comb()


if __name__ == "__main__":
    main()