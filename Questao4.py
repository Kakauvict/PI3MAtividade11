def numero_perfeito(numero):
    soma = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma += i

    if soma == numero:
        return True
    else:
        return False


n = int(input("Digite um número inteiro: "))

if numero_perfeito(n):
    print("O número é perfeito.")
else:
    print("O número não é perfeito.")
