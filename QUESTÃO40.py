from math import sqrt



print("---  COORDENADAS DO PONTO 1  ---")
x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))

print("\n--- COORDENADAS DO PONTO 2  ---")
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor da y2: "))


diferenca_x = (x2 - x1) ** 2
diferenca_y = (y2 - y1) ** 2

distancia = sqrt(diferenca_x + diferenca_y)


print("\n--- RESULTADO ---")
print(f"A distância entre os pontos P1({x1}, {y1}) e P2({x2}, {y2}) é: {distancia: .2f}")
