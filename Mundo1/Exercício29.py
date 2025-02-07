# Lê a velocidade do carro
velocidade = float(input("Digite a velocidade do carro em km/h: "))

# Verifica se a velocidade ultrapassou o limite
if velocidade > 80:
    # Calcula o valor da multa
    excesso = velocidade - 80
    multa = excesso * 7
    print(f"Você foi multado! O valor da multa é R${multa:.2f}.")
else:
    print("Você está dentro do limite de velocidade. Não foi multado.")
