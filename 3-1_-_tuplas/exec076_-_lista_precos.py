"""
Crie uma lista de nomes de produtos e seus respectivos preços na sequência.
Mostre os dados organizados de forma tabular
"""
cont = 0
produtos = ( 
    ('Pokan', 10.99),
    ('Maçã', 19.99),
    ('Pera', 7.50),
    ('Laranja', 29.99),
    ('Abacaxi', 15.899),
    ('Melancia', 12.49),
    ('Manga', 8.99),
    ('Carambola', 5.876),
    ('Caju', 21.50)
)

print('#'*31)
print('{:^31}'.format('Lista de compras'))
print('='*31)

while cont < len(produtos):
    print(f'{produtos[cont][0]:.<20}R$ {produtos[cont][1]:>7.2f}!')
    cont += 1

print('#'*31)