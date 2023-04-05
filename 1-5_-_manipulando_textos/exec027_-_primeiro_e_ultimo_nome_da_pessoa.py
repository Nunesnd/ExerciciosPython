"""
Faça o programa ler o nome completo de uma pessoa e mostrar o primeiro e o último nome separadamente
"""

nomeCompleto = input("Informe o nome completo: ")

nomeDividido = nomeCompleto.split()

print(nomeCompleto.split())

print(f"Primeiro Nome: {nomeDividido[0]}")
print(f"Último Nome: { nomeDividido[len(nomeDividido)-1]}")