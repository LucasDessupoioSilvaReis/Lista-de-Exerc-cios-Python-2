import random

def criar_matriz():
    return [[random.randint(0, 99) for _ in range(5)] for _ in range(5)]

def encontrar_segundo_maior_valor(matriz):
    flatten_matriz = [valor for linha in matriz for valor in linha]
    valores_unicos = sorted(set(flatten_matriz), reverse=True)

    # Se houver pelo menos dois valores únicos
    if len(valores_unicos) >= 2:
        segundo_maior_valor = valores_unicos[1]
        return segundo_maior_valor
    else:
        return None

def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)

def main():
    matriz = criar_matriz()

    print("Matriz 5x5:")
    exibir_matriz(matriz)

    segundo_maior_valor = encontrar_segundo_maior_valor(matriz)

    if segundo_maior_valor is not None:
        print("\nSegundo maior valor na matriz:", segundo_maior_valor)
    else:
        print("\nNão foi possível encontrar o segundo maior valor (matriz vazia).")

if __name__ == "__main__":
    main()
