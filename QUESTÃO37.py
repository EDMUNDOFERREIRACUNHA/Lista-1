dias_total = int(input("Digite a idade total em dias: "))

anos = dias_total // 365

resto_dias = dias_total % 365

meses = resto_dias // 30

dias_finais = resto_dias % 30

print(f"{dias_total} dias correspondem a exatamente:")
print(f"{anos} ano(s), {meses} mês(es) e {dias_finais} dia(s).")