"""
Calcule a soma entre todos os números ímpares, multiplos de 3 entre o intervalo de 1-500
"""
soma=0

for c in range(0,500):
    if (c%2) != 0:
        if (c%3)==0:
            soma=soma+c
print(f"Resultado => {soma}")
print("FIM")