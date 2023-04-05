"""
Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""


diasLocacao = int(input('Informe por quantos dias o veículo foi alugado? '))
kmPercorrido = float(input('Quantos quilômetros percorreram? '))

diaria = 60
precoKm = 0.15

valor = (diasLocacao * diaria) + (kmPercorrido * precoKm)

print(f"A custo da locação foi de R${valor:0.2f}. \nVolte Sempre!")