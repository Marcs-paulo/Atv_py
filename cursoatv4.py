M1 = float(input("Qual foi sua primeira nota? "))
M2 = float(input("Qual foi sua segunda nota? "))
M3 = float(input("Qual foi sua terceira nota? "))

media = (M1 + M2 + M3) / 3

if media <= 4.0:
    print("Você está reprovado")

elif 4.1 <= media <= 6.0:
    print("Você pegou o exame!")
    exame = float(input("Qual foi sua nota no exame? "))
    if exame > 6.0:
        print("Aprovado")
    else:
        print("Reprovado")

elif 6.1 <= media:
    print("Parabéns! Você está aprovado")
