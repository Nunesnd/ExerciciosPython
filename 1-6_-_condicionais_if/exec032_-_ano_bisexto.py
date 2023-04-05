"""
Faça um programa que leia um ano a ser inserido e identifique se é ou não um ano bisexto
"""

ano = int(input("Informe o ano: "))

if (ano%4)==0:
    print(f"o ano {ano} é bisexto" )
else:
    print(f"o ano {ano} NÃO é bisexto" )