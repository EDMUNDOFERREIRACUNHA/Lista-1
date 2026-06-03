numero = int(input("Digite um número inteiro de 3 dígitos (ex: 234): "))

centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10

inverso = (unidade * 100) + (dezena * 10) + centena

diferenca = abs(numero - inverso)


print(f"O número original é: {numero}")
print(f"O seu inverso é: {inverso}")
print(f"A diferença entre eles é: {diferenca}")