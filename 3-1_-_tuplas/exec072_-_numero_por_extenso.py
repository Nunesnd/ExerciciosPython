"""
crie uma tupla preenchida com uma contagem por extenso de zero a vinte
o prog deverá ler um número inteiro passado pelo usuário e mostrar o mesmo por extenso
"""
numeros = ('um', 'dois','três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinte', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )

num = int(input('Informe um número de 1 à 20: '))

print(f'Você quer dizer {numeros[num-1]}')