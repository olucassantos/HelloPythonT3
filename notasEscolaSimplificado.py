import os

alunos = []
medias = []

print("NOTAS PRO PLY")
print("*" * 50)

resposta = "s"
while resposta == "s":
    nome = input("Digite o nome do aluno: ")
    qtdeNotas = int(input("Quantas notas este aluno possui: "))
    alunos.append(nome)

    # For para percorrer a quantidade de notas
    media = 0
    for index in range(qtdeNotas):
        nota = float(input(f"Digite a nota {index + 1}: ")) # Pede a nota ao usuário
        media += nota # Adiciona a nota na lista de notas do aluno

    media = media / qtdeNotas
    medias.append(media)

    print("Deseja adicionar mais um aluno? (S/N)")
    resposta = input()

    os.system("cls") # Limpa a tela

quantidadeAlunos = len(alunos)

for index in range(quantidadeAlunos):
    print(f"Aluno: {alunos[index]}")
    print(f"Media: {medias[index]:.2f}")

print("==" * 30)

print("Média geral da turma")
media = sum(medias) / len(medias)
print(f"Média geral: {media:.2f}")