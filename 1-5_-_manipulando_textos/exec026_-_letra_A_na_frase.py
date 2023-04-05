"""
Faça que o prog leia uma frase pelo teclado e diga:
A) quantas vezes aparece a letra A na frase
B) Em qual posição aparece na primeira ocorrência
C) Em qual posição aparece na última ocorrência
"""

frase = input("Escreva uma frase: ")

print(f"A quantidade de vezes que a letra A aparece é: {frase.upper().count('A')}")
print(f"A primeira posiçaõ que a letra aparece é em {frase.upper().find('A')}")
print(f"A primeira posiçaõ que a letra aparece é em {frase.upper().rfind('A')}")