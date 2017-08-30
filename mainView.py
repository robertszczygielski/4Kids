# -*- coding:utf8 -*-
from helloForPlayer import powitanie
from miejsca import idzieszDo
from taskMeny import allTasks


powitanie('Ala')            # wizytówka z pierwszego zadania
HP = 100                    # jakieś życie
caleZloto = 0               # jakieś punkty

# najpierw sam las, bez możliwości wybrania miejsca gdzie idziesz

twojaOdpowiedz = -1         # najlepiej ujemna bo "kto wstawia ujemne", a 0 wychodzi z programu
while twojaOdpowiedz != 0 and HP > 0 and caleZloto < 10: # wszystkie 3 muszą być 'prawdą'
    twojaOdpowiedz = allTasks()
    if twojaOdpowiedz > 0:
        (rany, zloto) = idzieszDo(twojaOdpowiedz)
        HP = HP - rany
        caleZloto = caleZloto + zloto
        print                # wstawia pustą linie
        print 'Masz:', caleZloto, 'złota'
        print 'Zostało Ci HP:', HP
        print                # wstawia pustą linie

print 'By by!!'
