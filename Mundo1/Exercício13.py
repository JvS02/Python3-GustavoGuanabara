# Lê o salário do funcionário
salario = float(input("Digite o salário do funcionário: R$"))

# Calcula o aumento de 15%
aumento = salario * 0.15

# Calcula o novo salário
novo_salario = salario + aumento

# Exibe o novo salário com aumento
print(f"O salário original do funcionário é R${salario:.2f}.")
print(f"Com 15% de aumento, o novo salário é R${novo_salario:.2f}.")
