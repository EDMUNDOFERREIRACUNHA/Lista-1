segundos_total = int(input("Digite a quantidade total de segundos(inteiro): "))

horas = segundos_total // 3600

resto_segundos = segundos_total % 3600

minutos = resto_segundos // 60

segundo_finais = resto_segundos % 60

print(f"{segundos_total} segundos correspodem a: ")
print(f"{horas} hora(s), {minutos} minuto(s) e {segundos_finais} segundo(s)")