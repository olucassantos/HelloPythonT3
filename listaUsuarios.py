import os

# Cria uma lista para os usuários
nomes = []

print("Bem vindo ao sistema de cadastro de pessoas!")
print("*" * 60)

resposta = "s"
while resposta == "s":
    print("Qual o nome da pessoa?")
    nome = input()
    # Adiciona o nome na lista
    nomes.append(nome)

    print("Deseja adicionar mais um nome? (s/n)")
    resposta = input()

    os.system("cls") # Limpa a tela

print("Os nomes cadastrados foram:")

# Percorre a lista de nomes com indexação
for item in range(len(nomes)): # 
    print(f"{item + 1} - {nomes[item]}")

# Imprime a quantidade de nomes cadastrados
print("Quantidade:", len(nomes))