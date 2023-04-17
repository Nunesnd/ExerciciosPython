"""
Crie uma tupla com várias palavras sem acentos.
Mostre para cada palavra quais são suas respectivas vogais
"""

palavras = ('gato', 'cachorro', 'elefante', 'leao', 'girafa', 'tigre', 'rinoceronte', 'gazela', 'hiena', 'hipopotamo', 'crocodilo', 'panda', 'macaco', 'jabuti', 'cobra')



for item in palavras:    
    print(f'\nna palavra {item.upper()} temos: ', end='') #end impede que quebre a linha
    for vogal in item:
        if vogal.upper() in 'AEIOU':
            print(vogal, end=' ') #end acrecenta o valor em aspas no final da string
    
    