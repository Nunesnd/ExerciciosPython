"""
Faça um prog que compare dois numeros inteiros, qual o maior e se ambos são iguais.
"""

A = int(input('Primeiro número: '))
B = int(input('Segundo número: '))

if (A > B):
    print(f' o maior é {A}')
elif (B > A):
    print(f' o maior é {B}')
elif ( A == B):
    print("Valores iguais")