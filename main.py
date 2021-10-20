def citireLista():
    l = []
    givenString = input("dati mlista, cu elementele separate prin virgula: ")
    numbersAsString= givenString.split(",")
    for x in numbersAsString:
        l.append(int(x))
    return l

def nrNegNenule(l):
    '''
    Determina numerele negative nenule dintr-o lista
    :param l: lista de numere intregi
    :return: nr. negative nenule din l
    '''
    rezultat = []
    for x in l:
        if x < 0:
            rezultat.append(x)
    return rezultat

def testNrNegNenule():
    assert nrNegNenule([2, 3, 35, 0]) == []
    assert nrNegNenule([-1, 23, -17, 0, 41]) == [-1, -17]

def minimNrCuUltCifraEgalaCu(l, k):
    '''
    determina cel mai mic nr. dintr-o lista al carui ultima cifre este egala cu un nr. dat
    :param l: lista de numere intregi
    :param k: un numar intreg
    :return: cel mai mic nr. din l al carui ultime cifre este egala cu cu un nr. dat,
    sau None daca nu exista
    '''
    min = None
    for x in l:
        if (x%10) == k and (min is None or x < min):
            min = x
    return min

def testMinimNrCuUltCifraEgalaCu():
    assert minimNrCuUltCifraEgalaCu([-25, 4, -61, 87], 6) is None
    assert minimNrCuUltCifraEgalaCu([59, -32, 19, 64], 9) == 19

def isPrime(x):
    '''
    determina daca un numar este prim
    :param x: un numar intreg
    :return: True, daca nr. este prim sau False in caz contrar
    '''
    if x < 2:
        return False
    for i in range (2, x//2 + 1):
        if x % i == 0:
            return False
    return True

def testIsPrime():
    assert isPrime(6) is False
    assert isPrime(-3) is False
    assert isPrime(5) is True

def nrSuperprime(l):
    '''
    determina nr. dintr-o lista care sunt superprime
    :param l: lista de numere intregi
    :return: determina nr. din l care sunt superprime
    '''
    rezultat = []
    for x in l:
        if x > 0:
            copie = x
            while copie != 0 and isPrime(copie):
                copie = copie / 10
                c = copie
        if c == x:
            rezultat.append(x)
    return rezultat

def celMaiMareDivComun(m, n):
    '''
    determina cmmdc dintre m si n
    :param m: un nr. intreg
    :param n: un nr. intreg
    :return: cmmdc dintre m si n
    '''
    while n != m:
        if m > n:
            m =m -n
        else:
            n = n - m
    return m

def testCelMaiMareDivComun():
    assert celMaiMareDivComun(12, 10) == 2

def procesareLista(l):
    '''
    Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
    CMMDC-ul lor și numerele negative au cifrele în ordine inversă
    :param l: lista de nr. intregi
    :return: lista obtinuta din l în care numerele pozitive și nenule au fost înlocuite cu
    CMMDC-ul lor și numerele negative au cifrele în ordine inversă
    '''
    rezultat = []
    c = 0
    for x in l:
        if x > 0:
            cmmdc = celMaiMareDivComun(c, x)
            rezultat.append(cmmdc)
        elif x < 0:
            rezultat.append(str(x)[::-1])
    return rezultat

def testProcesareLista():
    assert procesareLista([-76, 12, 24, -13, 144]) == [-67, 12, 12, -31, 12]


def main():
    testNrNegNenule()
    testMinimNrCuUltCifraEgalaCu()
    testIsPrime()
    testCelMaiMareDivComun()
    l = []
    while True:
        print("1. Citire lista")
        print("2.Afisare nr. negative nenule din lista")
        print("3. Afisare cel mai mic mr. al carui ultima cifra este egala cu un nr. dat")
        print("4. Afișarea numerelor care sunt superprime")
        print("5. Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu"
              "CMMDC-ul lor și numerele negative au cifrele în ordine inversă")
        print("a. Afisare lista")
        print("x. Iesire")

        optiune = input("dati optiune: ")

        if optiune == "1":
            l = citireLista()
        elif optiune == "2":
            print(nrNegNenule(l))
        elif optiune == "3":
            k = int(input("dati un nr.:"))
            min = minimNrCuUltCifraEgalaCu(l, k)
            if min is None:
                print("nu exista")
            else:
                print(min)
        elif optiune == "4":
            print(nrSuperprime(l))
        elif optiune == "5":
            print(procesareLista(l))
        elif optiune == "a":
            print(l)
        elif optiune == "x":
            break
        else:
            print("optiune gresita! reincercati: ")

main()