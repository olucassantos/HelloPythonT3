print("Seja bem vindo a classificação de notas!")
print("*" * 50)

# Solicita a nota do aluno
print("Digite a nota do aluno: ")
nota = int(input())

if nota < 0 or nota > 100:
    print("Nota inválida.")
elif nota < 60:
    nota_final = "F"
elif nota < 70:
    nota_final = "D"
elif nota < 80:
    nota_final = "C"
elif nota < 90:
    nota_final = "B"
else:
    nota_final = "A"

print(f"A nota final é: {nota_final}")
