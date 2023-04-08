"""
leia um número inteiro e diga se ele é primo ou não
"""

import sympy

numero = int (input("Informe um número: "))

print(sympy.isprime(numero))
