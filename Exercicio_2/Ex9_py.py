import math

def operacoes_com_valor(numero):
    if numero in {1, 2, 3}:
        resultado = numero ** 2
        print(f"O valor elevado ao quadrado é: {resultado}")
    elif numero in {4, 9}:
        resultado = math.sqrt(numero)
        print(f"A raiz quadrada do número é: {resultado}")
    elif numero in {6, 7, 8}:
        resultado = numero / 9
        print(f"O valor dividido por 9 é: {resultado}")
    else:
        print("O valor fornecido não corresponde a nenhuma operação específica.")

def main():
    valor = float(input("Digite um valor: "))
    operacoes_com_valor(valor)

if __name__ == "__main__":
    main()
