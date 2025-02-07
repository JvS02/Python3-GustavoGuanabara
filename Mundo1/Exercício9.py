# Lê um número inteiro
numero = int(input("Digite um número inteiro: "))

# Exibe a tabuada do número
print(f"Tabuada de {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")