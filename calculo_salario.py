print("Seja bem vindo ao calculo de salário!")
print("*" * 50)

# Solicitação de dados
print("Qual o seu salário?")
salario = float(input())

print("Por quanto tempo trabalhou? (em anos)")
tempoServico = float(input())

# Cálculo de aumento de salário
if tempoServico > 5:
    novoSalario = salario * 1.05
    print(f"Seu novo salário é: {novoSalario}")
else:
    print("Não é possivel aplicar o aumento de salário.")
    print("Seu salário é de: ", salario)