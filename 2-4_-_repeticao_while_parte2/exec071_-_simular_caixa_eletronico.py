"""
Prog de caixa eletrônico. No início pergunte a quantia a ser sacada (inteiro).
O programa vai informar quantas cédulas de cada nota serão entregues
Considere que haverão as cédulas de R$50,00, R$20,00, R$10,00 e R$1,00
"""
saque = conta50 = conta20 = conta10 = conta1 = 0


saque = int(input('Informe quanto deseja retirar: '))

while saque >= 50:
    saque -= 50
    conta50 += 1
    
while saque >= 20:
    saque -= 20
    conta20 += 1
    
while saque >= 10:
    saque -= 10
    conta10 += 1

while saque >= 1:
    saque -= 1
    conta1 += 1
        
print(f'Foram sacadas:\n  - {conta50} notas de R$50,00\n  - {conta20} notas de R$20,00\n  - {conta10} notas de R$10,00\n  - {conta1} notas de R$1,00')
print(f'Sendo um total de {conta50+conta20+conta10+conta1} notas emitidas')