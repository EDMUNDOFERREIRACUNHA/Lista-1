import math

raio = float(input("Digite o valor do raio da esfera: "))

volume = (4 * math.pi * (raio ** 3)) / 3

print(f" O volume da esfera é: {volume: .2f}")