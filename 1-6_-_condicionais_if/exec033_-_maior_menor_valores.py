"""
Fazer um prog que leia três números e informe qual o menor e qual o maior
"""

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
c = int(input("Informe o terceiro número: "))

if (a>b):
    if (a>c):
        if (b > c):
            print(f"maior é {a} e menor é {c}")
    else:
        print(f"maior é {c} e menor é {b}")
else:
    if (b > c):
        if(a > c):
            print(f"maior é {b}e menor é {c}")
    else:
        print(f"maior é {c} e menor é {a}")