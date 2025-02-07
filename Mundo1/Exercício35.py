# Lê o comprimento das três retas
reta1 = float(input("Digite o comprimento da primeira reta: "))
reta2 = float(input("Digite o comprimento da segunda reta: "))
reta3 = float(input("Digite o comprimento da terceira reta: "))

# Verifica se as retas podem formar um triângulo
if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print("As retas podem formar um triângulo.")
else:
    print("As retas NÃO podem formar um triângulo.")
