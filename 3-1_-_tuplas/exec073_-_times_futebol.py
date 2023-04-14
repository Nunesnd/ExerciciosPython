"""
Crie uma tupla com os 20 colocados do campeonato brasileiro, depois mostre:
1) - Os 5 primeiros colocados
2) - Os 4 últimos (zona de rebaixamento)
3) - Uma lista dos times em ordem alfabética
4) - A posição de um time passado pelo usuário
"""

times = ('Fluminense', 'Palmeiras', 'Botafogo', 'Figueirense', 'Coritiba', 'Atletico Mineiro', 'Gremio', 'Avai', 'Red Bull Bragantino', 'Corinthians', 'Santos', 'Sao Paulo', 'Chapecoense', 'Internacional', 'Athletico Paranaense', 'Fortaleza', 'Flamengo', 'Cruzeiro', 'America Mineiro', 'Atletico Goianiense')

classificacao = times[:5]

rebaixamento = times[-4:]

print(f'classificação {classificacao}\nRebaixamento {rebaixamento}\nOrganizados {sorted(times)}')

posicao = str(input('Informe o nome do time: '))


num = 0
while True:
    time = times[num]
    if posicao.upper() == time.upper():
        print(f'A posicao do {time} é {num+1}º')
        break
    num += 1