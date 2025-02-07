# Lê a quantidade de quilômetros percorridos e os dias de aluguel
km_percorridos = float(input("Digite a quantidade de quilômetros percorridos: "))
dias_alugado = int(input("Digite a quantidade de dias que o carro foi alugado: "))

# Define os valores de custo
custo_por_dia = 60
custo_por_km = 0.15

# Calcula o preço total
preco_total = (dias_alugado * custo_por_dia) + (km_percorridos * custo_por_km)

# Exibe o preço a pagar
print(f"O preço total a pagar pelo aluguel do carro é R${preco_total:.2f}.")
