nota1 = float(input("Digite a primeira nota: "))
peso1 = float(input("Digite o peso da primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))
peso3 = float(input("Digite o peso da terceira nota: "))


superior_da_fracao = (nota1 * peso1) + (nota2 * peso2) + (nota3 * peso3)

soma_dos_pesos =peso1 + peso2 + peso3

media_ponderada = superior_da_fracao / soma_dos_pesos

print(f"A média ponderada do aluno é: {media_ponderada: .2f}")
