# Lê a largura e a altura da parede
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

# Calcula a área da parede
area = largura * altura

# Calcula a quantidade de tinta necessária (1 litro de tinta cobre 2 metros quadrados)
quantidade_tinta = area / 2

# Exibe os resultados
print(f"A área da parede é {area} metros quadrados.")
print(f"A quantidade de tinta necessária para pintar a parede é {quantidade_tinta} litros.")
