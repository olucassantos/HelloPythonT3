# Lista para armazenar os números
lista_numeros = []

print("Digite os números para adicionar à lista (0 para terminar):")
while True:
    numero = int(input())
    if numero == 0:
        break
    lista_numeros.append(numero)

# Solicita ao usuário a ordem de ordenação
ordem = input("Deseja a lista em ordem crescente ou decrescente? (Digite 'c' para crescente e 'd' para decrescente): ")

# Realiza a ordenação
for i in range(len(lista_numeros) - 1):
    for j in range(i + 1, len(lista_numeros)):
        # Verifica a condição de troca para ordem crescente ou decrescente
        troca = (ordem == 'c' and lista_numeros[i] > lista_numeros[j]) or (ordem == 'd' and lista_numeros[i] < lista_numeros[j])
        
        if troca:
            # Troca os elementos
            lista_numeros[i], lista_numeros[j] = lista_numeros[j], lista_numeros[i]

# Exibe a lista ordenada
print("Lista ordenada:", lista_numeros)