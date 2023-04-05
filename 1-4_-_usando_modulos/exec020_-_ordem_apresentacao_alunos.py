"""
faça um programa que sorteie uma ordem de apresentação de trabalhos dos mesmos alunos, que leia o nome e mostre a ordem sorteada
"""

import random
from typing import List

alunos: list[str] = ["Diego", "Sara", "Alef", "Bia"]

random.shuffle(alunos)

print(', '.join('\n' + nome for nome in alunos))