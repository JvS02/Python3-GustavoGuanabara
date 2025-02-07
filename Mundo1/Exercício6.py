import math

# Lê um número
numero = float(input("Digite um número: "))

# Calcula o dobro, triplo e raiz quadrada
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = math.sqrt(numero)

# Exibe os resultados
print(f"O dobro de {numero} é {dobro}.")
print(f"O triplo de {numero} é {triplo}.")
print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}.")