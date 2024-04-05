print("Bem vindo ao sistema de calculo de IMC!")
print("*" * 50)

# Solicita o nome do usuário
print("Digite o seu nome:")
nome = input()

# Solicita o peso do usuário
print("Digite o seu peso:")
peso = float(input())

# Solicita a altura do usuário
print("Digite a sua altura:")
altura = float(input())

# Realiza o calculo do IMC
imc = peso / (altura ** 2)

# Imprime o resultado do IMC suprimindo as casas decimais
print(f"{nome}, seu IMC é de: {imc:.1f}")
