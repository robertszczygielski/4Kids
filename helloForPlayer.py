# -*- coding:utf8 -*-
def powitanie(name):
    helloName = 'Witaj w grze ' + name      # dodaje tekst do imienia
    nameLenght = len(helloName)             # wstawia długość powitani do obrysowania
    endLine = '|'
    for znak in range(0, 6 + nameLenght):   # 6 bo 3 spacje z prawej i lewej
        endLine = endLine + '-'             # dowolny inny zak jak '*', '>'
    endLine = endLine + '|'

    print endLine
    print '|   ' + helloName + '   |'       # są 3 spacje i znak '|'
    print endLine
    print                                   # wstawia pustą linie

