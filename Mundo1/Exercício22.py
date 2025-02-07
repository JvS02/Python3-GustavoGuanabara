# Lê o nome completo da pessoa
nome_completo = input("Digite o seu nome completo: ")

# Exibe o nome em maiúsculas e minúsculas
print(f"Nome em maiúsculas: {nome_completo.upper()}")
print(f"Nome em minúsculas: {nome_completo.lower()}")

# Remove os espaços e conta o total de letras
nome_sem_espacos = nome_completo.replace(" ", "")
print(f"Total de letras (sem espaços): {len(nome_sem_espacos)}")

# Conta o número de letras do primeiro nome
primeiro_nome = nome_completo.split()[0]
print(f"Quantidade de letras do primeiro nome: {len(primeiro_nome)}")