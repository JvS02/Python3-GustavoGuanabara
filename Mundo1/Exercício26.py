# Lê a frase
frase = input("Digite uma frase: ").upper()  # Converte a frase para maiúsculas

# Conta quantas vezes "A" aparece na frase
quantidade_a = frase.count("A")

# Encontra a posição da primeira ocorrência de "A"
primeira_posicao = frase.find("A") + 1  # A função find retorna o índice, somamos 1 para mostrar em formato de posição

# Encontra a posição da última ocorrência de "A"
ultima_posicao = frase.rfind("A") + 1  # A função rfind retorna o índice da última ocorrência

# Exibe os resultados
print(f"A letra 'A' aparece {quantidade_a} vezes.")
if quantidade_a > 0:
    print(f"A primeira ocorrência de 'A' está na posição {primeira_posicao}.")
    print(f"A última ocorrência de 'A' está na posição {ultima_posicao}.")
