"""
Fazer um prog que leia varios números inteiros, a condição de parada será o número 999.
No final mostre a quantidade de números digitados e a soma dos mesmos (desconsiderando o 999)
"""

soma , num, quant = 0, 0, 0 
while num != 999:
    
    num = int(input('Informe um número para somar: '))
    
    if (num == 999): 
        break
        
    soma+=num
    
    quant +=1

print(f'A soma ficou em {soma}, a quantidade de núemro foi de {quant}')