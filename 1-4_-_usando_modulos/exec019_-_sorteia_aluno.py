"""
um professor quer sortear um dos seus quatro alunos para apagar o quadro. faça um programa que sorteie o nome do escolhido
"""
import random

alunos = ["Diego", "Sara", "Alef", "Bia"]

print(f'valor sorteado {random.choice(alunos)}')