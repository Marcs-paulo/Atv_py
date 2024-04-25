# #Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. 
# A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em Fahrenheit e C é a temperatura em graus Celsius


# - Função para ler e retorna o valor da temperatura (não recebe parâmetro)
# - Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
# - Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a impressão


def ler_temperatura():
    a = float(input("Qual é a temperatura em graus C: "))
    return a

def converter_fahrenheit(c):
    f = (c * 9) / 5 + 32  
    return round(f, 2)

def  imprimir_resultado(f):
    print(f"A temperatura em °C corresponde a {f} °F.")

temperatura_c = ler_temperatura()
f = converter_fahrenheit(temperatura_c)
imprimir_resultado(f)