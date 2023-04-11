"""
Faça um prog que leia o nome e preço de vários produtos em uma compra.
A cada produto cadastrado pergunte se deseja continuar cadastrando mais. No fim mostre:
1) - O total gasto
2) - Quantos produtos custam mais de R$1.000,00
3) - Quao o nome do produto mais barto
"""
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
totCusto = quantProd = prodCaro = precoBarato = 0
cont = nomeBarato = ''

while cont.upper() != 'N':
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    
    totCusto += preco
    
    if preco > 1000:
        prodCaro += 1
    
    if quantProd == 0:
        precoBarato = preco
    
    if precoBarato >= preco:
        precoBarato = preco
        nomeBarato = nome
        
        #print(f"O produto mais barato foi {nomeBarato} custando R${precoBarato:.2f}")
    
    cont = str(input('Deseja passar mais itens? [S/N]: '))
    
    quantProd += 1
    
    if cont.strip().upper()[0] == 'N':
        break
    
    while cont.strip().upper()[0] != ('S' or 'N'):
        print('Informação incorreta.')
        cont = str(input('Deseja passar mais itens? [S/N]: '))

print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

print(f"Foram passados {quantProd}, custando no total R${totCusto:.2f}")
print(f"Tivemos {prodCaro} produto(s) com preço(s) acima de R$1000,00.")
print(f"O produto mais barato foi {nomeBarato} custando R${precoBarato:.2f}")