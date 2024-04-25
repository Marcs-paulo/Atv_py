# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, utilizando um automóvel que faz 12 Km por litro.
# Para obter o cálculo, o usuário deve fornecer o tempo gasto na viagem e a velocidade média durante ela. 
# Desta forma, será possível obter a distância percorrida com a fórmula 
# DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a quantidade de litros de combustível 
# utilizada na viagem, com a fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os valores da velocidade média, 
# tempo gasto na viagem,a distância percorrida e a quantidade de litros utilizada na viagem


tempo = float(input("Quanto tempo o senhor(a) gastou em sua viagem? "))
velocidade= float(input("A quantos Km/H o senhor(a) estava?"))

distancia = tempo * velocidade

litros = distancia/12

print(f"O(a) senhor(a) demorou  {tempo} horas para percorrer uma distância de {distancia}Km. A uma velocidade media de {velocidade} Km/H e gastou {round(litros, 2)} litros de combustivel")