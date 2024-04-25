nota = media = soma = 0

for _ in range(0, 5):
    nota = float(input("Digite uma nota: "))
    soma += nota

print (soma)

media = soma/5
print(f"Sua media é {media}")

if media <= 4.0:
    print("Você está reprovado")

elif 4.1 <= media < 6.0:
    print("Você está de Recuperação!")

elif 6.0 <= media:
    print("Parabéns! Você está aprovado")

                    