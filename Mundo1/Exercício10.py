# Lê o valor em reais que a pessoa tem na carteira
dinheiro_reais = float(input("Digite quanto dinheiro você tem na carteira (em reais): "))

# Taxa de câmbio (1 real = X dólares)
taxa_cambio = 5.25  # Exemplo: 1 real = 5.25 dólares (ajuste conforme necessário)

# Calcula quantos dólares a pessoa pode comprar
quantidade_dolares = dinheiro_reais / taxa_cambio

# Exibe o resultado
print(f"Com R${dinheiro_reais:.2f}, você pode comprar U${quantidade_dolares:.2f} dólares.")
