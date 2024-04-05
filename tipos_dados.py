print("Bem vindo ao sistema de calculo de parcelas!")
print("=" * 50)

# Solicita o valor total de uma compra
print("Digite o valor total da compra:")
valor_total = input()
valor_total = float(valor_total)

# Solicita a quantidade de parcelas
print("Digite a quantidade de parcelas:")
parcelas = int(input())

# Calcula o valor de cada parcela e imprime na tela
resultado = valor_total / parcelas
print(f"O valor de cada parcela é: {resultado}")