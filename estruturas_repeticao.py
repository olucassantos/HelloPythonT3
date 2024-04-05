# Exemplo Tabuada

# print("Insira a tabuada desejada: ")
# tabuada = int(input())

# numero = 0
# while(numero <= 10):
#     print(f"{tabuada} x {numero} = {numero * tabuada}")
#     numero += 1

# Exemplo For

for multiplicador in range(0, 11):
    texto = ""
    for numero in range(1, 11):
        texto += f"{numero} x {multiplicador} = {multiplicador * numero} | "

    print(texto)