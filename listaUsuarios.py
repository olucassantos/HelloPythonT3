import os # Importa a biblioteca para limpar a tela

# Cria uma lista para os usuários
nomes = []

print("Bem vindo ao sistema de cadastro de pessoas!")
print("*" * 60)

resposta = "s"
# Enquanto a resposta for "s" o programa continua
while resposta == "s":
    print("Qual o nome da pessoa?")
    nome = input()
    # Adiciona o nome na lista
    nomes.append(nome)

    print("Deseja adicionar mais um nome? (s/n)")
    resposta = input()

    os.system("cls") # Limpa a tela

'''
    Poderiamos ter feito a leitura dos nomes da seguinte forma:
    for nome in nomes:
        print(nome)

    Mas, como queremos mostrar a posição do nome na lista, utilizamos a função range
'''

# Percorre a lista de nomes com indexação
print("Os nomes cadastrados foram:")
for item in range(len(nomes)): # 
    print(f"{item + 1} - {nomes[item]}")

# Imprime a quantidade de nomes cadastrados
print("Quantidade:", len(nomes))