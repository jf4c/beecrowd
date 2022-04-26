b = int(input('digite um número: '))
a = int(input('digite um número: '))
c = int(input('digite um número: '))

maiorAB = (a + b + abs(a-b)) / 2
maiorABC = int((maiorAB + c + abs(maiorAB - c)) / 2) 

print(f'O maior é {maiorABC}')