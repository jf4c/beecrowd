tempoViagem = int(input('Digite o tempo de viagem em horas: '))
velocidadeMedia = int(input('digite a velocidade media em km/h: '))

distancia = velocidadeMedia * tempoViagem
litros = float(distancia / 12)

print(f'a quantidade de litros para a viagem é {litros:,.3f}')
