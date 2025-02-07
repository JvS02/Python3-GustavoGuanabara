# Lê o salário do funcionário
salario = float(input("Digite o salário do funcionário: R$"))

# Calcula o aumento
if salario > 1250:
    aumento = salario * 0.10  # Aumento de 10%
else:
    aumento = salario * 0.15  # Aumento de 15%

# Exibe o aumento e o novo salário
novo_salario = salario + aumento
print(f"O aumento será de R${aumento:.2f}.")
print(f"O novo salário será R${novo_salario:.2f}.")
