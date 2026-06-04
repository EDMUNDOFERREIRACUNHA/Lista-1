distancia = float(input("Digite a distância total percorrida (km): "))
combustivel = float(input("Digite o total de combustível gasto(litros): "))

consumo_medio = distancia / combustivel

print("\n--- RELATÓRIO DE CONSUMO ---")
print(f"Distância: {distancia: .1f} km")
print(f"Combustível: {combustivel: .1f} L")
print("------------------------------")
print(f"O consumo médio do veículo foi de: {consumo_medio: .2f} km/l")
