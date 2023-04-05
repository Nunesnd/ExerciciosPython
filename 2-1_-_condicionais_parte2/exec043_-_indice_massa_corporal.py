"""
faça um prog que leia peso e medida de uma pessoa e calcule o IMC, conforme abaixo:
    até 18.5 abaixo do peso
    entre 18.5 e 25 peso ideal
    entre 25 e 30 sobrepeso
    entre 30 e 40 obesidade
    acima de 40, obesidade morbida
"""

altura = float(input("Informe a altura: "))
peso = int(input("Informe o peso: "))

imc = peso/(altura*altura)

if imc <= 18.5:
    print(f"Seu IMC é: {imc:.2f}\nAbaixo do peso")
elif imc > 18.5 and imc <= 25:
    print(f"Seu IMC é: {imc:.2f}\nPeso ideal")
elif imc > 25 and imc <= 30:
    print(f"Seu IMC é: {imc:.2f}\nSobrepeso")
elif imc > 30 and imc <= 40:
    print(f"Seu IMC é: {imc:.2f}\nobesidade")
elif imc > 40:
    print(f"Seu IMC é: {imc:.2f}\nObesidade morbida")