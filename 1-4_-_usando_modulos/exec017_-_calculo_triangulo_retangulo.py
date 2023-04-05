"""
17 - faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo, calcule e mostre o comprimento da hipotenusa
"""
import math
cat_op = int(input('Informe o valor do cateto oposto: '))
cat_ad = int(input('Informe o valor do cateto adjacente: '))

hip = math.hypot(cat_op, cat_ad)

print(f'Cateto oposto é: {cat_op}\nCateto adjacente é:{cat_ad}\nHipotenuza é: {hip}')