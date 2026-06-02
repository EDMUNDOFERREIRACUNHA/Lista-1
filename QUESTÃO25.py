metros_total = int(input("Digite a quantidade total de metros(inteiro): "))

km = metros_total // 1000

metros_restantes = metros_total % 1000

print(f"{metros_total} metros correspondem a: {km} km e {metros_restantes} metros.")