idade = int(input("Qual sua idade? "))

if  0 <= idade <= 12:
    print("Você é uma criança")
elif 12 < idade <= 17:
    print("Você é um adolescente")
elif 18 < idade:
    print("Você é um adulto")
else:
    print("Idade inválida!")