import random

def criar_matriz():
    return [[random.randint(10, 50) for _ in range(10)] for _ in range(10)]

def calcular_media_diagonal_secundaria(matriz):
    tamanho = len(matriz)
    diagonal_secundaria = [matriz[i][tamanho - i - 1] for i in range(tamanho)]
    media = sum(diagonal_secundaria) / tamanho
    return media

def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)

def main():
    matriz = criar_matriz()

    print("Matriz 10x10:")
    exibir_matriz(matriz)

    media_diagonal_secundaria = calcular_media_diagonal_secundaria(matriz)
    print("\nMédia dos elementos da diagonal secundária:", media_diagonal_secundaria)

if __name__ == "__main__":
    main()
