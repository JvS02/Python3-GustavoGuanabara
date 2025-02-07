import random

# Lê os nomes dos alunos
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")

# Coloca os nomes em uma lista
alunos = [aluno1, aluno2, aluno3, aluno4]

# Sorteia um aluno
escolhido = random.choice(alunos)

# Exibe o nome do aluno sorteado
print(f"O aluno sorteado para apagar o quadro é: {escolhido}")
