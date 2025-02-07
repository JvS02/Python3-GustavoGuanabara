# Lê o valor inserido pelo usuário
entrada = input("Digite algo: ")

# Exibe o tipo primitivo da entrada
print(f"O tipo primitivo de {entrada} é {type(entrada)}")

# Verifica e exibe outras informações
print("É um número? ", entrada.isdigit())
print("É um número decimal? ", entrada.replace('.', '', 1).isdigit())
print("É alfabético? ", entrada.isalpha())
print("É alfanumérico? ", entrada.isalnum())
print("Está em maiúsculas? ", entrada.isupper())
print("Está em minúsculas? ", entrada.islower())
print("Está capitalizado? ", entrada.istitle())
