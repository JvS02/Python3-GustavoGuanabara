import random

# Lê os nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Coloca os nomes em uma lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Embaralha a ordem dos alunos
random.shuffle(alunos)

# Exibe a ordem sorteada
print("A ordem sorteada para apresentação dos trabalhos é:")
for i, aluno in enumerate(alunos, 1):
    print(f"{i}. {aluno}")
