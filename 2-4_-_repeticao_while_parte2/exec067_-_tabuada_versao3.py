"""
Faça um prog mostrando a tabuada de vários números, um por vez, para cada valor digitdo pelo usuário
O prog será interrompido quando o número solicitado for negativo
"""

while True:
    multi = int(input("Informe um número: "))
    
    if multi < 0:
        break
    
    tab = 1
    while tab <= 10:
        print(f'{multi} X {tab} = {multi * tab}')
        tab+=1
    