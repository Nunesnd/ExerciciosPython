"""
faça umpro que leia no mínimo duas notas do aluno e diga conforme as médias:
    se nota <5 reprovado
    entre 5.0 e 6.9 recuperação
    igual ou maior que 7 aprovado
"""

nota1 = float(input("Informe a primeira nota do aluno: "))
nota2 = float(input("Informe a segunda nota do aluno: "))

media = (nota1+nota2)/2

if media < 5:
    print(f'A nota é {media}, REPROVADO')
elif (media>5 and media<6.9):
    print(f'A nota é {media}, RECUPERAÇÃO')
if media > 7:
    print(f'A nota é {media}, APROVADO!!!!!')