lista = []

for _ in range(1, 6):
    valor = int(input("Digite o valor: "))
    lista.append(valor)

lista

soma = 0
for i in range(len(lista)):
    soma += lista[i]

print("Soma: ", soma)