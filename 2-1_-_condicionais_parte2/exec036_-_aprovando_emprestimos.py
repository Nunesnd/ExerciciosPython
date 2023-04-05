"""
Escreva um programa para aprovar um emprestimo bancário para a compra de uma casa.
O prog vai perguntar o valor da casa, o salario do comprador, e em quantos anos ele vai pagar

Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salario ou então o emprestimo será negado
"""

casa = int(input("Qual o valor ddo imovel? "))

salario = float(input("Qual o salário do comprador? "))

prazo_pagamento = int(input("Em quantos anos deseja realizar o pagamento? "))

prestacao = casa / (prazo_pagamento*12)

if(prestacao < (salario*0.3)):
    print(f'Com salário de R${salario:.2f}, a prestação pode ser de no máximo R${salario*0.3:.2f}, e está cotado em R${prestacao:.2f}')
    print('Liberado')
else:
    print(f'Com salário de R${salario:.2f}, a prestação pode ser de no máximo R${salario*0.3:.2f}, e está cotado em R${prestacao:.2f}')
    print('Seu cadastro não passou no sistema.')


print("---Fim---")
"""
if (prestacao > (salario*0.3)):
    print("Emprestimo supera margem permitida ao comprador.")
    aumenta = input("Deseja aumentar o prazo de pagamento? (S/N)")
    if (aumenta == 'S' or "s"):
        add_prazo = int(input("em quantos anos?"))
        prazo_pagamento = prazo_pagamento + add_prazo

        prestacao = casa / (prazo_pagamento * 12)

    elif (prestacao <= (salario*0.3)):
        print(f"Há condiçõs de compra, com parcelas de R${prestacao:.2f}, comprometendo o valor de R${(salario*0.3):.2f} no salário")
    else:
        print("Empréstimo não autorizado!")
    print("Saida1")
print("Saida2")
"""