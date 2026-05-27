def verificar_palindromo(texto):
    if texto == texto[::-1]:
        return True
    else:
        return False


palavra = input("Digite uma palavra: ")

if verificar_palindromo(palavra):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
