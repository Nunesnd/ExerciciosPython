"""
18 - faca um prog que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
"""
import math

angulo = int(input('Informe um ângulo qualquer: '))

print(f"O ângulo é {angulo}\nSeno: {math.sin(angulo)}\nCosseno: {math.cos(angulo)}\nTangente {math.tan(angulo)}")