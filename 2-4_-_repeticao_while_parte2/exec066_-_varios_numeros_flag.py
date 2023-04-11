"""
leia vários numeros inteiros, a condição de parada será o 999 (igual o exec 64)
"""

soma , num, quant = 0, 0, 0 
while True:
    
    num = int(input('Informe um número para somar: '))
    
    if (num == 999): 
        break
        
    soma+=num
    
    quant +=1

print(f'A soma ficou em {soma}, a quantidade de núemro foi de {quant}')