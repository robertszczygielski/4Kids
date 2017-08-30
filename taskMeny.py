# -*- coding:utf8 -*-
def allTasks():
    odpowiedz = -1                  # najlepiej ujemna bo "kto wstawia ujemne", a 0 wychodzi z programu
    while not dobraOdp(odpowiedz):
        print '1. Idz do lasu'
        print '2. Idz do wioski'
        # print '3. Idz do jaskinji'# może się uda ;)
        print '0. Exit'

        zKlawiatury = raw_input('Co robisz?: ')

        if zKlawiatury.isdigit():   # is digit - czy jest liczbą
            odpowiedz = int(zKlawiatury)
        else:
            odpowiedz = -1

        if not dobraOdp(odpowiedz):
            print 'Chyba wcisneles cos nie tak?'

    print                           # wstawia pustą linie
    return odpowiedz


def dobraOdp(odpowiedz):            # pierwsze podejscie do, gdy odpowiedź jest w zakresie 0 - 2
    return odpowiedz > -1 and odpowiedz < 3

def zlaOdp(odpowiedz):              # inne podejście, zakres od nn do -1 i od 3 do nn
    return odpowiedz < 0 or odpowiedz > 2