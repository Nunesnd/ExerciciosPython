"""
calcule o valor a ser pago em um produto considerando, seu preço normal e condição de pagamento
    - a vista dinheiro ou pix - 10% desconto
    - a vista cartão - 5% desconto
    - em até 2X no cartão crédito - preço normal
    - 3X ou mais no crédito - add 20% juros
"""

valor = float(input("Valor a ser pago: "))

cond_pag = int(input('Qual a forma de pagamento? \n1 - A vista \n2 - A prazo\n'))

if cond_pag == 1:
    pag_vista = int(input("Pagamento será:\n1 - Dinheiro/Pix\n2 - Cartão débito\n"))
    if(pag_vista == 1):
        desconto = valor * 0.9
        print(f'Pagamento a vista no pix ou dinheiro, com desconto de 10% fica R${desconto:.2f}')
    elif(pag_vista == 2):
        desconto = valor * 0.95
        print(f'Pagamento no débito, com desconto de 5% fica R${desconto:.2f}')
    elif (cond_pag != 1) and (cond_pag != 2):
        print('Por favor informe uma opção correta!')
elif cond_pag == 2:
    print("A prazo")
    prazo = int(input("Em quantas vezes? "))
    if prazo <= 2:
        parcela = valor / prazo
        print(f'Total de pagamento de {prazo}X no valor de R${parcela:.2f} por parcela.\nTotalizando o valor de R${valor:.2f}')
    else:
        valor_juros = valor*1.2
        parcela = (valor_juros) / prazo
        print(f'Total de pagamento de {prazo}X no valor de R${parcela:.2f} por parcela.\nTotalizando o valor de R${valor_juros:.2f}')

elif (cond_pag != 1) and (cond_pag != 2):
    print("Opção errada")

print('Volte Sempre')