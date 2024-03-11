def calcular_serie(n):
    soma = 0.0

    for i in range(2, n + 2, 1):
        m = 2 * i - 1
        termo = i / m
        soma += termo

    return soma

def obter_valor_n():
    while True:
        n = int(input("Digite um valor positivo para n: "))
        if n > 0:
            return n
        else:
            print("Por favor, digite um valor positivo.")

def main():
    n = obter_valor_n()
    resultado = calcular_serie(n)
    print(f"O valor da expressão para n = {n} é: {resultado}")

if __name__ == "__main__":
    main()
