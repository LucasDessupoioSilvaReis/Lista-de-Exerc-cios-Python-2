def processar_valor(valor):
    if valor < 0:
        resultado = abs(valor)
        print(f"O módulo do valor é: {resultado}")
    elif valor > 10:
        novo_valor = float(input("Digite outro valor: "))
        diferenca = novo_valor - valor
        print(f"A diferença entre os valores é: {diferenca}")
    else:
        resultado = valor / 5
        print(f"O valor dividido por 5 é: {resultado}")

def main():
    valor = float(input("Digite um valor: "))
    processar_valor(valor)

if __name__ == "__main__":
    main()

