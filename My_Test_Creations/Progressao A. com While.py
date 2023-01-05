termo1 = int(input('Digite o primeiro termo da progressão artimética (DIGITE 0 PARA CANCELAR): '))
razao = int(input('Digite a razão da PA: '))
cont = 0
pa = termo1

while True:
    while cont < 10:
        cont += 1
        print(pa)
        pa += razao
