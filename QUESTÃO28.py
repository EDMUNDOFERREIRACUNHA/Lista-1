horas_total = int(input("Digite a quantidade total de horas(inteiro): "))

semanas = horas_total // 168

resto_horas = horas_total % 168

dias = resto_horas // 24

horas_finais = resto_horas % 24

print(f"{horas_total} horas correspondem a: ")
print(f"{semanas} samana(s), {dias} dia(s) e {horas_finais} horas(s).")