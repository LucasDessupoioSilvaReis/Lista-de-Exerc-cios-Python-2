def main():
    matriz = []
    for i in range(6):
        linha = []
        for j in range(6):
            numero = float(input(f"Digite o elemento ({i+1},{j+1}) da matriz: "))
            linha.append(numero)
        matriz.append(linha)

    diagonal_principal = [matriz[i][i] for i in range(6)]

    print("\nMatriz 6x6:")
    for linha in matriz:
        print(linha)

    print("\nVetor da diagonal principal:", diagonal_principal)

if __name__ == "__main__":
    main()
