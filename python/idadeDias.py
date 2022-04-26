
numeroDias = int(input('Digite o numero de dias: '))

anos = numeroDias // 365
numeroDias = numeroDias - 365*anos
meses = numeroDias // 30 

dias = numeroDias - 30*meses


print(f'{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)')

