# Lê o preço do produto
preco = float(input("Digite o preço do produto: R$"))

# Calcula o desconto de 5%
desconto = preco * 0.05

# Calcula o novo preço
novo_preco = preco - desconto

# Exibe o novo preço com desconto
print(f"O preço original do produto é R${preco:.2f}.")
print(f"Com 5% de desconto, o novo preço é R${novo_preco:.2f}.")
