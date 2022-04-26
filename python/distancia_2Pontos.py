import math

x1 = float(input("digite um valor para x1: "))
y1 = float(input("digite um valor para y1: "))
x2 = float(input("digite um valor para x2: "))
y2 = float(input("digite um valor para y2: "))

distancia = float(math.sqrt((x2 - x1)**2 + (y2 - y1)**2))

print(f'A distância é de: {distancia:,.4f}')