# -*- coding:utf8 -*-
from random import randint

# na początku jedno zwierzę
liczbaBestjiWLesie = {'wilk': 100,
                'niedźwiedź': 70,
                'wilkołak': 1}

silaBestjiWLesie = {'wilk': 5,
                'niedźwiedź': 7,
                'wilkołak': 50}

jedzenie = {'ryba': 5,
            'jablko': 3}


def policzBestje():
    liczna = 0
    for bestja in liczbaBestjiWLesie:
        liczna = liczna + liczbaBestjiWLesie[bestja]
    return liczna


def walkaZ(bestja):                 # jedna z pierwszych, wymagana nawet 1 zwierzę
    hpBestji = silaBestjiWLesie[bestja]
    twojaRana = 0
    while (hpBestji > 0):
        ranaBestji = randint(2, 10)
        hpBestji = hpBestji - ranaBestji
        print 'Zadaleś bestji:', ranaBestji, 'rany'

        if hpBestji > 0:
            twojaRana = twojaRana + randint(0, hpBestji)
            print 'Twoje rany:', twojaRana

    return twojaRana, 1



def spotkanaBestja(bestja):
    print 'spotkaleś ', bestja
    czyWalczysz = raw_input("Chesz walczyć? T/N: ")
    if czyWalczysz == 'T' or czyWalczysz == 't':
        return walkaZ(bestja)
    else:
        return 0, 0


def las():
    wszystkieBestje = policzBestje()
    znaleziona = randint(0, wszystkieBestje + 20)
    wilkiINiedzwiedzie = liczbaBestjiWLesie['niedźwiedź'] + liczbaBestjiWLesie['wilk']

    if znaleziona <= liczbaBestjiWLesie['wilk']:
        return spotkanaBestja('wilk')
    elif znaleziona > liczbaBestjiWLesie['wilk'] and znaleziona <= wilkiINiedzwiedzie:
        return spotkanaBestja('niedźwiedź')
    elif znaleziona > wilkiINiedzwiedzie and znaleziona <= wilkiINiedzwiedzie + liczbaBestjiWLesie['wilkołak']:
        return spotkanaBestja('wilkołak')
    else:
        print 'nic nie znalazles'
        return 0, 0


def wioska():
    odnowaZycia = []
    index = 1

    for doKupienia in jedzenie:
        print index, ' ', doKupienia, " cena: ", jedzenie[doKupienia]
        index = index + 1
        odnowaZycia.append(jedzenie[doKupienia])

    odp = raw_input('Co kupujsze? : ')

    tyleOdzyskasz = odnowaZycia[int(odp)]
    tyleOdzyskasz = tyleOdzyskasz * (-1)
    return tyleOdzyskasz, tyleOdzyskasz


def idzieszDo(miejsce):
    if miejsce == 1:
        return las()
    if miejsce == 2:
        return wioska()