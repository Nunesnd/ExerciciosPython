"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$1250,00, calcule aumento de 10%
Para salários inferiores ou iguais o aumento é de 15%
"""

salario = int(input("Informe seu salário base: "))

if salario > 1250:
    aum = (salario * 0.1)+salario
    print(f"Seu salário de R${salario:.2f} passou para R${aum:.2f}")
else:
    aum = (salario * 0.15)+salario
    print(f"Seu salário de R${salario:.2f} passou para R${aum:.2f}")