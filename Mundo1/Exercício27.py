# Lê o nome completo
nome_completo = input("Digite o seu nome completo: ")

# Divide o nome completo em partes (separadas por espaços)
nome_dividido = nome_completo.split()

# O primeiro nome é o primeiro da lista
primeiro_nome = nome_dividido[0]

# O último nome é o último da lista
ultimo_nome = nome_dividido[-1]

# Exibe o primeiro e o último nome
print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
