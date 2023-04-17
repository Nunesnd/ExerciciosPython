"""
Crie um programa onde o usuário digite uma expressão qualquer USANDO parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
"""

cont = 0 
contA = 0 
contF = 0 

expressao = str(input("Escreva uma espressão matemática: "))

print(expressao)

while cont < len(expressao):
    if expressao[cont] == '(':
        contA += 1
    if expressao[cont] == ')':
        contF += 1
    
    cont += 1
    
if contA == contF:
    print('Expressão com parênteses válidos')
else:    
    print('Expressão com parênteses inválidos')