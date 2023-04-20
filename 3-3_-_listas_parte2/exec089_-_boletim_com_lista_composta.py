"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

hist = list() #será o histórico do aluno
turma = []
continua = ''
contador = 0

while True:
    hist.append(str(input("Nome: ")))
    hist.append(float(input("Nota 1: ")))
    hist.append(float(input("Nota 2: ")))
    
    turma.append(hist[:])
    
    hist.clear()

    continua = input('Deseja continuar [S/N]? ')
    if continua in 'Nn':
        break

print('- '*20, end='-\n')

while contador < len(turma):
    media = (turma[contador][1]+turma[contador][2])/2
    print(f"nº: {contador} - Aluno: {turma[contador][0]}, média {media:.2f}") 

    contador += 1

while True:
    
    ver_aluno = int(input('Deseja ver notas do aluno [999 p/ sair]? '))
    
    if ver_aluno == 999:
        break
    
    print(f"Notas de {turma[ver_aluno][0]} são: {turma[ver_aluno][1]} e {turma[ver_aluno][2]}")
    
print('<<<  VOLTE SEMPRE >>>')

#for a in turma:
#    media = (a[1]+a[2])/2
#    print(f"nº: {a} - Aluno: {a[0]}, média {media:.2f}")    

print(len(turma))