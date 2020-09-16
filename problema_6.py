n = int(input("Introduceti orice numar real mai mic ca 10000 "))
sum = 0
ultimul = n % 10
restul = n % 9
catul = n // 9

n2 = n // 10
penultcif = n2 % 10

def calcule(n):
    global sum
    while n > 0:
        cif = n % 10
        sum = sum + cif
        n = n // 10
    return sum

def intoarcere(n):
    tor = ""
    while n > 0:
        cif = n % 10
        tor = tor + str(cif)
        n = n // 10
    return tor


if  n < 10000:
    print(f'Ultima cifra a numarului {n} = {ultimul}')
    print(f'Restul si catul impartirii acestui numar la 9 este {restul} si {catul} respectiv')
    print(f'Suma tuturor cifrelor numarului {n} = {calcule(n)}')
    print(f'Pen ultima cifra a lui {n} = {penultcif}')
    print(f'Rasturnatul lui {n} = {intoarcere(n)}')