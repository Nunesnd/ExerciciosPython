"""
Faça um programa que leia o comprimento de três segmentos de retas e analise se elas podem ou não forma um triângulo
"""

retaA = int(input("Informe o valor da reta A: "))
retaB = int(input("Informe o valor da reta B: "))
retaC = int(input("Informe o valor da reta C: "))

if (retaA+retaB) > retaC and (retaB+retaC) > retaA and (retaA+retaC) > retaB:
    print(f"reta A: {retaA}")
    print(f"reta B: {retaB}")
    print(f"reta C: {retaC}")
    print("Teremos um triângulo")
else:
    print(f"reta A: {retaA}")
    print(f"reta B: {retaB}")
    print(f"reta C: {retaC}")
    print("Não é possível ter uma reta")
