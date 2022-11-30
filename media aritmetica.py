# algoritmo que recebe valores e calcula uma media aritmetica
valores = []
value = 0
qntd = 0

print('MÉDIA ARITMÉTICA ->>>> DIGITE OS VALORES QUE DESEJAR >>>>>')

while True:
    entrada = float(input(f'DIGITE O {qntd + 1}º VALOR >>>>> para continuar digite o valor "0"\n'))
    value += entrada
    if entrada == 0:
        break
    qntd += 1
    print(qntd)
print(f'A media dos valores colocados é {value / qntd}')