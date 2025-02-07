# Lê a distância da viagem em Km
distancia = float(input("Digite a distância da viagem em Km: "))

# Calcula o preço da passagem
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

# Exibe o valor da passagem
print(f"O preço da passagem será R${preco:.2f}.")
