import math

def calcular_fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)

def processar_valor(valor):
    if valor in {1, 2}:
        resultado = valor ** 3
        print(f"O valor elevado ao cubo é: {resultado}")
    elif valor % 3 == 0:
        fatorial = calcular_fatorial(valor)
        print(f"O fatorial de {valor} é: {fatorial}")
    elif valor in {4, 5, 7, 8}:
        resultado = valor / 9
        print(f"O valor dividido por 9 é: {resultado}")
    else:
        print("Valor inválido.")

def main():
    valor = int(input("Digite um valor: "))
    processar_valor(valor)

if __name__ == "__main__":
    main()
