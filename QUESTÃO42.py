custo_fabrica = float(input("Digite o custo de fábrica do carro(R$): "))


valor_distribuidor = custo_fabrica * 0.28

valor_impostos = custo_fabrica * 0.45

custo_consumidor = custo_fabrica + valor_distribuidor + valor_impostos


print("\n--- DETALHAMENTO DO PREÇO FINAL  ---")
print(f"Custo de Fábrica original: R$ {custo_fabrica: .2f}")
print(f"Parcela do Distribuidor (28%): R$ {valor_distribuidor: .2f}")
print(f"Impostos Governamentais  (45%): R$ {valor_impostos: .2f}")
print("----------------------------------------")
print(f"Custo Final ao Consumidor: R$ {custo_consumidor: .2f}")