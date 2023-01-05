total = 10
termo1 = int(input('Digite o primeiro termo da progressão artimética (DIGITE 0 PARA CANCELAR): '))
razao = int(input('Digite a razão da PA: '))
cont = 0
pa = termo1

while True:

    while cont < total:
        cont += 1
        print(pa)
        pa += razao

    num = int(input('Quantos termos você desejar ver a mais? '))
    total += num
    if num == 0:
        break
