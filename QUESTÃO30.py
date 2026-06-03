minutos_total = int(input("Digite a quantidade total de minutos(inteiro): "))

dias = minutos_total // 1440

resto_minutos = minutos_total % 1440

horas = resto_minutos % 60

minutos_finais = resto_minutos % 60

print(f"{minutos_total} minutos correspondem a; ")
print(f"{dias} dia(s), {horas} hora(s) e {minutos_finais} minuto(s)")
