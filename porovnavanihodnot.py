#!/usr/bin/env python3

numberlist = []
highestnumberlist = []
highestnumber = 0
rotations = 0
y = int(input("Chceš přidat číslo do seznamu? \nNapiš 1. pokud ano, napiš 2. pokud ne.\n"))
if y == 1:
    while y == 1:
        rotations = rotations + 1
        newnumber = int(input("Zadej číslo které chceš přidat do seznamu: "))
        if newnumber == highestnumber:
            print("if newnumber == highestnumber:")
            numberlist.append(newnumber)
        if newnumber < highestnumber:
            print("if newnumber < highestnumber:")
            numberlist.append(newnumber)
        if newnumber > highestnumber:
            print("if newnumber > highestnumber:")
            numberlist.append(newnumber)
            highestnumber = newnumber
            highestnumberlist.clear()
            highestnumberlist.append(highestnumber)
        print(f"numberlist: {numberlist}")
        print(f"highestnumberlist: {highestnumberlist}")
        print(f"HIGHEST NUMBER: {highestnumber}")
        print(f"Rotations: {rotations}")
        y = int(input("Chceš přidat číslo do seznamu? \nNapiš 1. pokud ano, napiš 2. pokud ne.\n"))

if y == 2:
    print("nn")
