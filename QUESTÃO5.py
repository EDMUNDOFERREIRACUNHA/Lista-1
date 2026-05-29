numero = int(input("Digite um número inteiro de 3 dígitos: "))

centena = numero // 100

resto = numero % 100

dezena = resto // 10

unidade = resto % 10

soma = centena + dezena + unidade

print(f"A soma dos elementos({centena} + {dezena} + {unidade} é igual a: {soma})")