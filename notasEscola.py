import os

alunos = []
notas = []

print("NOTAS PRO PLY")
print("*" * 50)

resposta = "s"

while resposta == "s":
    notas_aluno = [] # Cria uma lista vazia para armazenar as notas do aluno

    nome = input("Digite o nome do aluno: ")
    qtdeNotas = int(input("Quantas notas este aluno possui: "))
    alunos.append(nome)

    # For para percorrer a quantidade de notas
    for index in range(qtdeNotas):
        nota = float(input(f"Digite a nota {index + 1}: ")) # Pede a nota ao usuário
        notas_aluno.append(nota) # Adiciona a nota na lista de notas do aluno

    notas.append(notas_aluno) # Adiciona a lista de notas do aluno na lista de notas

    print("Deseja adicionar mais um aluno? (S/N)")
    resposta = input()

    os.system("cls") # Limpa a tela

quantidadeAlunos = len(alunos)

medias = []
for index in range(quantidadeAlunos):
    print(f"Aluno: {alunos[index]}")

    # Notas
    print("Notas: ", end="")
    for nota in notas[index]:
        print(f"{nota} ", end="")
    print()
    
    #media = soma das notas do aluno / quantidade de notas
    media = sum(notas[index]) / len(notas[index])
    medias.append(media)

    print(f"Media: {media:.2f}")

print("==" * 30)

print("Média geral da turma")
media = sum(medias) / len(medias)
print(f"Média geral: {media:.2f}")