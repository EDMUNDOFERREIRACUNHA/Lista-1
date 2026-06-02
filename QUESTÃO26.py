dias_total = int(input("Digite a quantidade total de dias(inteiro): "))

semanas = dias_total // 7

dias_restantes = dias_total % 7

print(f"{dias_total} dias correspondem a:{semanas} semana(s) e {dias_restantes} dia(s).")