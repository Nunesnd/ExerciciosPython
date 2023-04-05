"""
Complementando o exec 35 dos triangulos, dessa vez analise qual o tipo de triangulo será formado
    Equilatero - todos os lados iguais
    Isósceles - dois lados iguais
    Escaleno - todos os lados diferentes
"""

retaA = int(input("Informe o valor da reta A: "))
retaB = int(input("Informe o valor da reta B: "))
retaC = int(input("Informe o valor da reta C: "))

if (retaA+retaB) > retaC and (retaB+retaC) > retaA and (retaA+retaC) > retaB:
    print(f"reta A: {retaA}")
    print(f"reta B: {retaB}")
    print(f"reta C: {retaC}")
    print("Teremos um triângulo")

    if retaA == retaB == retaC:
        print('Teremos um Triângulo Equilatero')
    elif (retaA==retaB) or (retaA==retaC) or (retaB==retaC):
        print('Teremos um Triângulo Isósceles')
    elif retaA != retaB != retaC:
        print('Teremos um Triângulo Escaleno')

else:
    print(f"reta A: {retaA}")
    print(f"reta B: {retaB}")
    print(f"reta C: {retaC}")
    print("Não é possível ter uma reta")
