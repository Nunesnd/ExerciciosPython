"""
Escreva um programa que leia a velocidade de um carro.
Se ultrapassar 80km/h mostre uma mensgem dizendo que ele foi multado
A multa vai custar R$7,00 por cada km acima do limite
"""

vel = int(input("Velocidade registrada foi: "))

if vel>80:
    multa = (vel-80)*7
    print(f"Você foi multado por trafegar a {vel}km/h. Sua multa é de R${multa},00")
else:
    print("Parabéns por seguir as normas de trânsito")