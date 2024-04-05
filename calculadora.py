print("Bem vindo a Calculadora 5000 Pro Max Ultra")
print("*" * 50)

# Solicita o primeiro número
print("Digite o primeiro número: ")
numero_um = float(input())

# Solicita o segundo número
print("Digite o segundo número: ")
numero_dois = float(input())

# Solicita a operação desejada
print("Digite a operação desejada: ")
print("+ - Soma")
print("- - Subtração")
print("* - Multiplicação")
print("/ - Divisão")
operacao = input()

if operacao == "+":
    print(f"O resultado da soma é: {numero_um + numero_dois}")
elif operacao == "-":
    print(f"O resultado da subtração é: {numero_um - numero_dois}")
elif operacao == "*":
    print(f"O resultado da multiplicação é: {numero_um * numero_dois}")
elif operacao == "/":
    if numero_dois == 0:
        print("Não é possível dividir por zero.")
    else:
        print(f"O resultado da divisão é: {numero_um / numero_dois}")
else:
    print("Operação inválida.")