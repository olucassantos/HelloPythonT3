import os

texto = "Bem vindo ao sistema de reservar de Voo!"
print(texto)
print("=" * len(texto))

nomes = [] # Lista de nomes dos passageiros
destinos = [] # Lista de destinos dos passageiros

# Código do programa
while True:
    print("Qual o nome do passageiro?")
    nome = input()

    print("Qual o destino desejado?")
    destino = input()

    nomes.append(nome) # Adiciona o nome do passageiro na lista de nomes
    destinos.append(destino) # Adiciona o destino do passageiro na lista de destinos

    print("Deseja adicionar mais uma reserva? (s/n)")
    resposta = input()

    if resposta == "n":
        break # Sai do loop while imediatamente

os.system("cls" if os.name == "nt" else "clear") # Limpa a tela do terminal

print("Reservas realizadas com sucesso!")

print("Lista de passageiros e destinos reservados:")

for index in range(len(nomes)):
    print(f"Passageiro: {nomes[index]} - Destino: {destinos[index]}")