def calcular_raiz(n, x):
    r = n ** (1 / x)
    return r


n = float(input("Digite o radicando: "))
x = float(input("Digite a ordem da raiz: "))

print("Resultado:", calcular_raiz(n, x))
