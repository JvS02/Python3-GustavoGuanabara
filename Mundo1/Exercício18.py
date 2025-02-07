import math

# Lê o ângulo em graus
angulo = float(input("Digite o valor do ângulo em graus: "))

# Converte o ângulo para radianos
angulo_radianos = math.radians(angulo)

# Calcula o seno, cosseno e tangente
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Exibe os resultados
print(f"O seno de {angulo}° é: {seno:.2f}")
print(f"O cosseno de {angulo}° é: {cosseno:.2f}")
print(f"A tangente de {angulo}° é: {tangente:.2f}")
