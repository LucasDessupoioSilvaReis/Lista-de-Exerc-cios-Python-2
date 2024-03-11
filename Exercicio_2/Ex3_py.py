def substituir_valores(vetor):
    for i in range(len(vetor)):
        if vetor[i] < 0:
            vetor[i] = 0
        elif vetor[i] < 10:
            vetor[i] = 1
        else:
            vetor[i] = 2

def main():
    vetor = []

    for i in range(20):
        numero = float(input(f"Digite o {i + 1}º número: "))
        vetor.append(numero)

    print("\nVetor original:", vetor)

    substituir_valores(vetor)

    print("Vetor modificado:", vetor)

if __name__ == "__main__":
    main()
