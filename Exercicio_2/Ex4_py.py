def forma_triangulo_retangulo(lados):
    lados.sort()  # Ordena os lados para facilitar a identificação dos catetos e da hipotenusa
    cateto1, cateto2, hipotenusa = lados

    # Verifica se os lados formam um triângulo
    if cateto1 + cateto2 > hipotenusa:
        # Verifica se é um triângulo retângulo usando o teorema de Pitágoras
        if cateto1**2 + cateto2**2 == hipotenusa**2:
            return True
        else:
            return False
    else:
        return False

def main():
    lados = []

    for i in range(3):
        lado = float(input(f"Digite o {i + 1}º lado do triângulo: "))
        lados.append(lado)

    if forma_triangulo_retangulo(lados):
        print("Os lados fornecidos formam um triângulo retângulo.")
    else:
        print("Os lados fornecidos não formam um triângulo retângulo.")

if __name__ == "__main__":
    main()
