import math

# Lê os comprimentos dos catetos
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Calcula o comprimento da hipotenusa
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

# Exibe o resultado
print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")
