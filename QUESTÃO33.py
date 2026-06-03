numero = int(input("Digite um número inteiro de 3 dígitos (ex: 532): "))

centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10

inverso = (unidade * 100) + (dezena * 10) + centena

soma = numero + inverso


print(f"O número original é: {numero}")
print(f"O seu inverso é: {inverso}")
print(f"A soma entre eles é: {soma}")