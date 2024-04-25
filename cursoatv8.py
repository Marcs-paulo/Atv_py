dicionario = {}

for _ in range(0, 3):
    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))
    dicionario[nome] = nota

print(dicionario)

soma = 0

for nota in dicionario.values():
    soma += nota

print("A media dos alunos é: ", soma/3)