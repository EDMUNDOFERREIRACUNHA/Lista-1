idade_a = int(input("Digite a idade da pessoa A: "))
idade_b = int(input("Digite a idade da pessoa B: "))


media_idades = (idade_a + idade_b) / 2

diferenca_idades = abs(idade_a - idade_b)

print("\n---  ANÁLISE DAS IDADES  ---")
print(f"Idade da Pessoa A: {idade_a} anos" )
print(f"Idade da Pessoa B: {idade_b} anos")
print("----------------------------")
print(f"A média das idades é: {media_idades: .1f} anos")
print(f"A diferença de idade entre elas é de: {diferenca_idades} anos")