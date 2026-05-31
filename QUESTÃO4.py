cotacao_dolar = float(input("Digite o valor do dólar hoje(cotação em R$): "))
valor_dolar = float(input("Digite a quantidade de dólares que deseja converter ($): "))

valor_real = valor_dolar * cotacao_dolar

print(f"O valor equivalente em Real é: R$ {valor_real: .2f}")