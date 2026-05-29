minutos_totais = int(input("Digite a quantidade total de minutos: "))

horas = minutos_totais // 60
minutos_restantes = minutos_totais % 60
print(f"O equivalente é: {horas}h e {minutos_restantes}min.")
