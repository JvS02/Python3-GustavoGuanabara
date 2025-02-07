import random

# O computador escolhe um número aleatório entre 0 e 5
numero_computador = random.randint(0, 5)

# O usuário tenta adivinhar o número
numero_usuario = int(input("Tente adivinhar o número escolhido pelo computador (entre 0 e 5): "))

# Verifica se o usuário acertou
if numero_usuario == numero_computador:
    print("Parabéns! Você acertou!")
else:
    print(f"Você errou. O número escolhido pelo computador foi {numero_computador}.")
