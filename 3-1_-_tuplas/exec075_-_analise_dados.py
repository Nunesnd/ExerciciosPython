"""
Leia quatro valores pelo teclado e guarde-os eum uma tupla. Depois mostre:
1) - Quantas vezes apareceu o valor 9
2) - Em que posição foi digitado o primeiro valor 3
3) - Quais foram os números pares
"""
nove = 0
pares = pos = ''

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))
num4 = int(input('Informe o quarto número: '))
num5 = int(input('Informe o quinto número: '))

seq = [num1, num2, num3, num4, num5]

for c in range (0,5):
    
    if seq[c] == 9:
        nove += 1
        
    if seq[c] == 3 and pos == '':
        pos = str(c+1)
    
    if (seq[c] % 2) == 0:
        par = str(seq[c])
        pares += par + ' '
    
print(f'O nove apareceu {nove} vezes')
if pos == '':
    print('O número três não apareceu na sequência.')
else:
    print(f'O três aparece pela primeira vez na posição {pos}')
print(f'O números pares são: {pares}')