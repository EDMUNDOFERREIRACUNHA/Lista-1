numero = int(input("Digite um número inteiro de 3 dígitos(ex:532): "))

centena_antiga = numero // 100

resto = numero % 100

dezena = resto // 10

unidade_antiga = resto % 10

numero_inverso = (unidade_antiga * 100) + (dezena * 10) + centena_antiga

print(f"O inverso do número {numero} é: {numero_inverso}")