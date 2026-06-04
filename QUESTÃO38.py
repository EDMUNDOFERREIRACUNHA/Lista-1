import math




print("---PRIMEIRA FRAÇÃO---")
num1 = int(input("Digite o numerador da 1ª fração: "))
den1 = int(input("Digite o denominador da 1ª fração: "))


print("\n---SEGUNDA FRAÇÃO---")
num2 = int(input("Digite o numerador da 2ª fração: "))
den2 = int(input("Digite o denominador da 2ª fração: "))


numerador_final = (num1 * den2) + (num2 * den1)
denominador_final = den1 * den2


divisor_comum = math.gcd(numerador_final, denominador_final)


num_simplificado = numerador_final // divisor_comum
den_simplificado = denominador_final // divisor_comum



print("\n---RESULTADO---")
print(f"A soma das frações é: {num1}/{den1} + {num2}/{den2} = {num_simplificado}/{den_simplificado}")
