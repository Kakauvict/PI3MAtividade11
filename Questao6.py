def contar_divisiveis_por_5(n):
    contador = 0

    for i in range(1, n + 1):
        if i % 5 == 0:
            contador += 1

    return contador


numero = int(input("Digite um número: "))

print("Quantidade:", contar_divisiveis_por_5(numero))
