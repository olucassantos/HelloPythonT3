# Cria uma lista de nomes
nomes = ["Omar", "Wanderlei", "Fabiano", "Rafael"]
# Como acessar um elemento da lista
print(nomes[3])
# Alterar um valor da lista
nomes[3] = "Roseli"
print(nomes)
# Adicionar um valor na lista
nomes.append("Francis")
print(nomes)
# Remover um valor da lista
nomes.remove("Roseli") # Remove o primeiro valor encontrado
# Remover um valor da lista com base no índice
del nomes[2]
print(nomes)
# Contar o tamanho da lista
print(len(nomes))