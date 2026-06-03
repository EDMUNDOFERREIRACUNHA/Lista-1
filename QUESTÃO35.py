numero = int(input("Digite um número inteiro de 4 dígitos(ex:9534): "))

milhar = numero // 1000
resto1 = numero % 1000

centena = resto1 // 100
resto2 = resto1 % 100

dezena = resto2 // 10
unidade = resto2 % 10

soma_elementos = milhar + centena + dezena + unidade


print(f" O número digitado foi: {numero}")
print(f"A soma dos seus dígitos ({milhar} + {centena} + {dezena} + {unidade}) é: {soma_elementos}")