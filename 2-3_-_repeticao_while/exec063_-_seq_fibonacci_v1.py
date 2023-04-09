"""
leia um número N inteiro qualquer e mostre esses N elementos da sequência de fibonacci


num1 = 0
num2 = 1

while num2 < 20:
    print(num2)
    num1 = num2
    num2 = num1+num2
  """  
a, b = 0, 1
n=0
termos = int(input("Quando números? "))

while n < termos:
    a, b = b, a + b
    print(a)
    
    n+=1