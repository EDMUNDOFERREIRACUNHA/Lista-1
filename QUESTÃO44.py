velocidade_kmh = float(input("Digite a velocidade do veículo em km/h: "))


velocidade_ms = velocidade_kmh / 3.6


print("\n--- CONVERSÃO DE VELOCIDADE ---")
print(f"Velocidade original: {velocidade_kmh: .1f} km/h")
print(f"Velocidade convertida: {velocidade_ms: .2f} m/s")