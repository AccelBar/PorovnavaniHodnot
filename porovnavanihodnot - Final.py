#!/usr/bin/env python3

from typing import NewType


numberlist = []
highestnumberlist = []
coordinates = []
highestnumber = None
rotations = 0
highrotations = 0
listoption = 0
y = int(input("Chceš přidat číslo do seznamu? \nNapiš 1. pokud ano, napiš 2. pokud ne.\n"))
if y == 1:
    while y == 1:
        rotations = rotations + 1
        newnumber = int(input("Zadej číslo které chceš přidat do seznamu: "))
        if highestnumber == None:
            highestnumber = newnumber
        else:
            highestnumber = highestnumber
        if newnumber == highestnumber:
            #print("if newnumber == highestnumber:")
            highrotations = rotations + 1
            coordinates.append(highrotations)
            numberlist.append(newnumber)
            highestnumberlist.append(newnumber)
        if newnumber < highestnumber:
            #print("if newnumber < highestnumber:")
            numberlist.append(newnumber)
        if newnumber > highestnumber:
            #print("if newnumber > highestnumber:")
            numberlist.append(newnumber)
            coordinates.clear()
            highrotations = 0
            coordinates.append(rotations)
            highestnumber = newnumber
            highestnumberlist.clear()
            highestnumberlist.append(highestnumber)
        #print(f"numberlist: {numberlist}")
        #print(f"highestnumberlist: {highestnumberlist}")
        #print(f"HIGHEST NUMBER: {highestnumber}")
        #print(f"Rotations: {rotations}")
        #print(f"highestnumber is {highestnumber}, on coordinates: {coordinates}")
        y = int(input("Chceš přidat číslo do seznamu? \nNapiš 1. pokud ano, napiš 2. pokud ne.\n"))

if y == 2:
    print(f"Zadal jsi celkem {rotations} čísel, nejvyšší číslo je {highestnumber}.\nNejvyšší číslo se nachází na souřadnicích {coordinates}.\nChceš vypsat seznam zadaných čísel? (Ano - 1, Ne - 2)")
    listoption = int(input(" "))
    if listoption == 1:
        print(f"Seznam veškerých čísel: {numberlist}")
    if listoption == 2:
        print("Ok.")
