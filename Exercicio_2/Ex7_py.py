import random

def criar_matriz():
    return [[random.randint(10, 50) for _ in range(10)] for _ in range(10)]

def encontrar_maior_valor(matriz):
    maior_valor = None

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i != j:  # Desconsidera os elementos da diagonal principal
                valor_atual = matriz[i][j]
                if maior_valor is None or valor_atual > maior_valor:
                    maior_valor = valor_atual

    return maior_valor

def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)

def main():
    matriz = criar_matriz()

    print("Matriz 10x10:")
    exibir_matriz(matriz)

    maior_valor = encontrar_maior_valor(matriz)
    
    if maior_valor is not None:
        print("\nMaior valor desconsiderando a diagonal principal:", maior_valor)
    else:
        print("\nNão foi possível encontrar um maior valor (matriz vazia).")

if __name__ == "__main__":
    main()
