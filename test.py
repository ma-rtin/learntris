#!/usr/bin/env python

pass

import numpy as np
import sys
import fileinput



def ausgeben(matrix):
    zeilenAnzahl = len(matrix)
    spaltenAnzahl = len(matrix[0])
    for zeile in range(zeilenAnzahl):
        for spalte in range(spaltenAnzahl):
            sys.stdout.write(matrix[zeile][spalte]+" ")
        sys.stdout.write("\n")
    return

def matrixEinlesen(matrix):

# . = empty (black)     0
# g = green             1
# r = red               2
# b = blue              3
# m = magenta           4
# y = yellow            5
# c = cyan              6
# o = orange            7

    for zeile in range(22):
        eingabe=raw_input()
        eingabe=eingabe.split(' ')
        for spalte in range(10):
            matrix[zeile][spalte]=eingabe[spalte]

    return

def matrixLeeren(matrix):
    for zeile in range(22):
        for spalte in range(10):
            matrix[zeile][spalte]='.'
    return

def zeigeZahl(zahl):
    print(str(zahl))
    return

def matrixSimulation(matrix, score, clearedLines):
    for zeile in range(22):
        zeileVoll=True
        for spalte in range(10):
            if matrix[zeile][spalte]=='.':
                zeileVoll = False
        if zeileVoll:
            for spalte in range(10):
                matrix[zeile][spalte]='.'
            score=score+100
            clearedLines = clearedLines+1
    return [score,clearedLines]


def setTetramino(tet):
    if tet=="I":
        tetramino=[['.','.','.','.'],['c','c','c','c'],['.','.','.','.'],['.','.','.','.']]
    elif tet=="O":
        tetramino=[['y','y'],['y','y']]
    elif tet=="Z":
        tetramino=[['r','r','.'],['.','r','r'],['.','.','.']]
    elif tet=="S":
        tetramino=[['.','g','g'],['g','g','.'],['.','.','.']]
    elif tet=="J":
        tetramino=[['b','.','.'],['b','b','b'],['.','.','.']]
    elif tet=="L":
        tetramino=[['.','.','o'],['o','o','o'],['.','.','.']]
    elif tet=="T":
        tetramino=[['.','m','.'],['m','m','m'],['.','.','.']]
    return tetramino

def rotateClockwise(matrix, tet, zeileTetramino, spalteTetramino, randRahmen):
    anzahlZeilen = len(tet)
    anzahlSpalten= len(tet[0])

    #links in Spielfeld schieben
    for i in range(randRahmen[0]):
        rg=nachRechts(matrix, tet, zeileTetramino, spalteTetramino, randRahmen)
        zeileTetramino=rg[0]
        spalteTetramino=rg[1]
        randRahmen=rg[2]
    #rechts in Spielfeld schieben
    for i in range(randRahmen[1]):
        rg=nachLinks(matrix, tet, zeileTetramino, spalteTetramino, randRahmen)
        zeileTetramino=rg[0]
        spalteTetramino=rg[1]
        randRahmen=rg[2]

    tetNeu=[['0' for x in range(len(tet))]for x in range(len(tet))]
    #erste Zeile muss in letzte Spalte
    for zeile in range(anzahlZeilen):
        for spalte in range(anzahlSpalten):
            tetNeu[spalte][-1-zeile]=tet[zeile][spalte]
    return [tetNeu, zeileTetramino, spalteTetramino, randRahmen]

def rotateCounterClockwise(matrix, tet, zeileTetramino, spalteTetramino, randRahmen):
    anzahlZeilen = len(tet)
    anzahlSpalten= len(tet[0])

    #links in Spielfeld schieben
    for i in range(randRahmen[0]):
        rg=nachRechts(matrix, tet, zeileTetramino, spalteTetramino, randRahmen)
        zeileTetramino=rg[0]
        spalteTetramino=rg[1]
        randRahmen=rg[2]
    #rechts in Spielfeld schieben
    for i in range(randRahmen[1]):
        rg=nachLinks(matrix, tet, zeileTetramino, spalteTetramino, randRahmen)
        zeileTetramino=rg[0]
        spalteTetramino=rg[1]
        randRahmen=rg[2]

    tetNeu=[['0' for x in range(len(tet))]for x in range(len(tet))]
    #erste spalte muss in letzte zeile
    for zeile in range(anzahlZeilen):
        for spalte in range(anzahlSpalten):
            tetNeu[-1-spalte][zeile]=tet[zeile][spalte]
    return [tetNeu, zeileTetramino, spalteTetramino, randRahmen]



def tetInMatrix(matrix, tet, zeileTetramino, spalteTetramino, caps):
    anzahlZeilen = len(tet)
    anzahlSpalten= len(tet[0])
    for zeile in range(anzahlZeilen):
        for spalte in range(anzahlSpalten):
            # Seitenrand testen
            if (spalteTetramino+spalte)>=0 and (spalteTetramino+spalte)<=(len(matrix[0])-1):
                # Unteren Rand testen
                if (zeileTetramino+zeile) <= (len(matrix)-1):
                    hilfsstring=tet[zeile][spalte]
                    hilfsstring=str(hilfsstring)
                    if caps:
                        hilfsstring=hilfsstring.upper()
                    matrix[zeileTetramino+zeile][spalteTetramino+spalte]=hilfsstring
    return matrix

def nachLinks(matrix, activeTetramino, zeileTetramino, spalteTetramino, randRahmen):
    moeglich=False
    if spalteTetramino > 0:
        moeglich = True
    else:
        linkeSpalteLeer = True
        for zeile in range(len(activeTetramino)):
            if activeTetramino[zeile][randRahmen[0]]!='.':
                linkeSpalteLeer = False
        if linkeSpalteLeer:
            moeglich=True
            randRahmen[0]=randRahmen[0]+1
    if moeglich:
        # Tetramino verschieben
        spalteTetramino = spalteTetramino - 1
        rechteSpalte=spalteTetramino+len(activeTetramino)-1
        if randRahmen[1] != 0:
            randRahmen[1]=  randRahmen[1]-1
        # frei gewordenen Bereich leeren
        for zeile in range(len(activeTetramino)):
            if (rechteSpalte+1)<len(matrix[0]):
                matrix[zeileTetramino+zeile][rechteSpalte+1]='.'
    return [zeileTetramino,spalteTetramino, randRahmen]

def nachRechts(matrix, activeTetramino, zeileTetramino, spalteTetramino,randRahmen):
    moeglich=False
    if (spalteTetramino+len(activeTetramino)-1) < (len(matrix[0])-1):
        moeglich=True
    else:
        rechteSpalteLeer = True
        for zeile in range(len(activeTetramino)):
            if activeTetramino[zeile][len(activeTetramino)-1-randRahmen[1]]!='.':
                rechteSpalteLeer = False
        if rechteSpalteLeer:
            moeglich=True
            randRahmen[1] = randRahmen[1]+1
    if moeglich:
        # Tetramino verschieben
        spalteTetramino = spalteTetramino + 1
        if randRahmen[0] != 0:
            randRahmen[0] = randRahmen[0]-1
        # frei gewordenen Bereich leeren
        for zeile in range(len(activeTetramino)):
            if (spalteTetramino-1)>=0:
                matrix[zeileTetramino+zeile][spalteTetramino-1]='.'
    return [zeileTetramino,spalteTetramino,randRahmen]

def nachUnten(matrix, activeTetramino, zeileTetramino, spalteTetramino, randRahmen):
    moeglich = False
    moeglichBlock = True
    moeglichSpielfeld = False
    # Werden die Spielfeld abmessungen eingehalten?
    if (zeileTetramino+len(activeTetramino))<len(matrix):
        moeglichSpielfeld = True
    else:
        untereZeileLeer = True
        for spalte in range(len(activeTetramino[0])):
            if(activeTetramino[-1-randRahmen[2]][spalte])!='.':
                untereZeileLeer = False
        if untereZeileLeer:
            moeglichSpielfeld=True
            randRahmen[2]= randRahmen[2]+1
    if moeglichSpielfeld:
        # Anderer Block im Weg?
        if (zeileTetramino+len(activeTetramino))<len(matrix): #falls noch nicht ganz unten 
            for spalte in range(len(activeTetramino[0])):
                if matrix[zeileTetramino+len(activeTetramino)][spalteTetramino+spalte]!='.':
                    moeglichBlock=False
    if moeglichSpielfeld and moeglichBlock:
        moeglich= True
    if moeglich:
        zeileTetramino = zeileTetramino+1
        for spalte in range(len(activeTetramino[0])):
            matrix[zeileTetramino-1][spalteTetramino+spalte]='.'
    return [zeileTetramino,spalteTetramino, randRahmen, moeglich]

def hardDrop(matrix, activeTet, zeileTet, spalteTet, randRahmen):
    moeglich=True
    while moeglich:
        rg=nachUnten(matrix,activeTet, zeileTet, spalteTet, randRahmen)
        zeileTet=rg[0]
        spalteTet=rg[1]
        randRahmen=rg[2]
        moeglich=rg[3]
    matrix = tetInMatrix(matrix, activeTet, zeileTet, spalteTet, False)
    return matrix

def inputVerarbeiten(matrix, activeTetramino, zeileTetramino, spalteTetramino, score, clearedLines, randRahmen):
    cmd=raw_input()
    #cmdListe=cmd.split(' ')
    cmdListe=cmd.replace(" ","")
    anzahlInputs=len(cmdListe)
    eingabe=0
    while eingabe<anzahlInputs:
        if cmdListe[eingabe]=="q":
            sys.exit()
        elif cmdListe[eingabe]=="p":
            ausgeben(matrix)
        elif cmdListe[eingabe]=="g":
            matrixEinlesen(matrix)
        elif cmdListe[eingabe]=="?":
            eingabe=eingabe+1
            if cmdListe[eingabe]=="s":
                zeigeZahl(score)
            if cmdListe[eingabe]=="n":
                zeigeZahl(clearedLines)
        elif cmdListe[eingabe]=="c":
            matrixLeeren(matrix)
        elif cmdListe[eingabe]=="s":
            ergebnis=matrixSimulation(matrix,score, clearedLines)
            score=ergebnis[0]
            clearedLines=ergebnis[1]
        #aktives Tetramino setzen:
        elif cmdListe[eingabe]=="I":
            spalteTetramino = 3
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("I")
        elif cmdListe[eingabe]=="O":
            spalteTetramino = 4
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("O")
        elif cmdListe[eingabe]=="Z":
            spalteTetramino = 3
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("Z")
        elif cmdListe[eingabe]== "S":
            spalteTetramino = 3
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("S")
        elif cmdListe[eingabe]== "J":
            spalteTetramino = 3
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("J")
        elif cmdListe[eingabe]=="L":
            activeTetramino = setTetramino("L")
            randRahmen = [0,0,0]
            spalteTetramino = 3
        elif cmdListe[eingabe]=="T":
            spalteTetramino = 3
            randRahmen=[0,0,0]
            activeTetramino = setTetramino("T")
        elif cmdListe[eingabe]=="t":
            ausgeben(activeTetramino)
        # Rotieren
        elif cmdListe[eingabe]==")":
            rg = rotateClockwise(matrix,activeTetramino, zeileTetramino, spalteTetramino,randRahmen)
            activeTetramino = rg[0]
            zeileTetramino = rg[1]
            spalteTetramino = rg[2]
            randRahmen = rg[3]
        elif cmdListe[eingabe]=="(":
            rg = rotateCounterClockwise(matrix,activeTetramino, zeileTetramino, spalteTetramino,randRahmen)
            activeTetramino = rg[0]
            zeileTetramino = rg[1]
            spalteTetramino = rg[2]
            randRahmen = rg[3]
        # Verschiedene Ausgabemoeglichkeiten
        elif cmdListe[eingabe] ==";":
            print("")
        elif cmdListe[eingabe] =="P":
            matrix = tetInMatrix(matrix, activeTetramino, zeileTetramino, spalteTetramino, True)
            ausgeben(matrix)
        # Tetramino verschieben:
        elif cmdListe[eingabe]=="<":
            rg = nachLinks(matrix, activeTetramino, zeileTetramino, spalteTetramino, randRahmen)
            zeileTetramino = rg[0]
            spalteTetramino = rg[1]
            randRahmen = rg[2]
        elif cmdListe[eingabe]==">":
            rg = nachRechts(matrix, activeTetramino, zeileTetramino, spalteTetramino,randRahmen)
            zeileTetramino = rg[0]
            spalteTetramino = rg[1]
            randRahmen = rg[2]
        elif cmdListe[eingabe]=="v":
            rg = nachUnten(matrix, activeTetramino, zeileTetramino, spalteTetramino, randRahmen)
            zeileTetramino = rg[0]
            spalteTetramino = rg[1]
            randRahmen = rg[2]
        elif cmdListe[eingabe]=="V":
            matrix = hardDrop(matrix, activeTetramino, zeileTetramino, spalteTetramino, randRahmen)
        else:
            print("falsche eingabe")
            print("input: " + cmdListe[eingabe])
        eingabe=eingabe+1
    return [matrix, activeTetramino, zeileTetramino, spalteTetramino, score, clearedLines, randRahmen]

def main():
    #Startwerte setzen
    matrix = [['.' for x in range(10)]for x in range(22)]
    score = 0
    clearedLines = 0
    activeTetramino = []
    zeileTetramino = 0
    spalteTetramino = 4
    randRahmen = [0,0,0]    #definiert, wie weit andere Bloecke oder der Spielfeldrand 
                            #in das Tet hinein ragen
                            # [links,rechts, unten]
    while True:
        ergebnis=inputVerarbeiten(matrix, activeTetramino, zeileTetramino, spalteTetramino,score, clearedLines, randRahmen)
        matrix = ergebnis[0]
        activeTetramino = ergebnis[1]
        zeileTetramino = ergebnis[2]
        spalteTetramino = ergebnis[3]
        score = ergebnis[4]
        clearedLines = ergebnis[5]
        randRahmen = ergebnis[6]
    return

if __name__ == '__main__':
    main()


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
