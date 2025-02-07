# Lê o nome da cidade
cidade = input("Digite o nome da cidade: ")

# Verifica se a cidade começa com "SANTO"
if cidade.strip().upper().startswith("SANTO"):
    print("A cidade começa com 'SANTO'.")
else:
    print("A cidade NÃO começa com 'SANTO'.")
