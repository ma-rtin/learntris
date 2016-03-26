#!/usr/bin/env python

pass

import numpy as np
import sys
import fileinput



def ausgeben(matrix, offsetLinks, offsetRechts, offsetUnten):
    zeilenAnzahl = len(matrix)-offsetUnten
    spaltenAnzahl = len(matrix[0]) - offsetRechts-offsetLinks
    for zeile in range(zeilenAnzahl):
        for spalte in range(spaltenAnzahl):
            sys.stdout.write(matrix[zeile][spalte+offsetLinks]+" ")
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
            matrix[zeile][spalte+1]=eingabe[spalte]

    return

def matrixLeeren(matrix):
    for zeile in range(22):
        for spalte in range(10):
            matrix[zeile][spalte+1]='.'
    return

def zeigeZahl(zahl):
    print(str(zahl))
    return

def matrixSimulation(matrix, score, clearedLines):
    for zeile in range(22):
        zeileVoll=True
        for spalte in range(10):
            if matrix[zeile][spalte+1]=='.':
                zeileVoll = False
        if zeileVoll:
            for spalte in range(10):
                matrix[zeile][spalte+1]='.'
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

def rotateClockwise(matrix, tet, posTet, randRahmen):
    anzahlZeilen = len(tet)
    anzahlSpalten= len(tet[0])

    #links in Spielfeld schieben
    for i in range(randRahmen[0]):
        rg=nachRechts(matrix, tet, posTet, randRahmen)
        posTet=rg[0]
        randRahmen=rg[1]
    #rechts in Spielfeld schieben
    for i in range(randRahmen[1]):
        rg=nachLinks(matrix, tet, posTet, randRahmen)
        posTet=rg[0]
        randRahmen=rg[1]

    tetNeu=[['0' for x in range(len(tet))]for x in range(len(tet))]
    #erste Zeile muss in letzte Spalte
    for zeile in range(anzahlZeilen):
        for spalte in range(anzahlSpalten):
            tetNeu[spalte][-1-zeile]=tet[zeile][spalte]
    return [tetNeu, posTet, randRahmen]

def rotateCounterClockwise(matrix, tet, posTet, randRahmen):
    anzahlZeilen = len(tet)
    anzahlSpalten= len(tet[0])

    #links in Spielfeld schieben
    for i in range(randRahmen[0]):
        rg=nachRechts(matrix, tet, posTet, randRahmen)
        posTet = rg[0]
        randRahmen=rg[1]
    #rechts in Spielfeld schieben
    for i in range(randRahmen[1]):
        rg=nachLinks(matrix, tet, posTet, randRahmen)
        posTet=rg[0]
        randRahmen=rg[1]

    tetNeu=[['0' for x in range(len(tet))]for x in range(len(tet))]
    #erste spalte muss in letzte zeile
    for zeile in range(anzahlZeilen):
        for spalte in range(anzahlSpalten):
            tetNeu[-1-spalte][zeile]=tet[zeile][spalte]
    return [tetNeu, posTet, randRahmen]



def tetInMatrix(matrix, tet, posTet, caps):
    anzahlZeilen = len(tet)
    anzahlSpalten= len(tet[0])
    for zeile in range(anzahlZeilen):
        for spalte in range(anzahlSpalten):
            # Seitenrand testen
            if (posTet[1]+spalte)>=1 and (posTet[1]+spalte)<=(len(matrix[0])-2):
                # Unteren Rand testen
                if (posTet[0]+zeile) <= (len(matrix)-2):
                    hilfsstring=tet[zeile][spalte]
                    hilfsstring=str(hilfsstring)
                    if caps:
                        hilfsstring=hilfsstring.upper()
                    matrix[posTet[0]+zeile][posTet[1]+spalte]=hilfsstring
    return matrix

def nachLinks(matrix, activeTetramino, posTet, randRahmen):
    moeglich=False
    if posTet[1] > 1:
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
        posTet[1]=posTet[1]-1
        rechteSpalte=posTet[1]+len(activeTetramino)-1
        if randRahmen[1] != 0:
            randRahmen[1]=  randRahmen[1]-1
        # frei gewordenen Bereich leeren
        for zeile in range(len(activeTetramino)):
            if (rechteSpalte+1)<len(matrix[0])-1:
                matrix[posTet[0]+zeile][rechteSpalte+1]='.'
    return [posTet, randRahmen]

def nachRechts(matrix, activeTetramino, posTet, randRahmen):
    moeglich=False
    if (posTet[1]+len(activeTetramino)-1) < (len(matrix[0])-2):
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
        posTet[1]=posTet[1]+1
        if randRahmen[0] != 0:
            randRahmen[0] = randRahmen[0]-1
        # frei gewordenen Bereich leeren
        for zeile in range(len(activeTetramino)):
            if (posTet[1]-1)>=1:
                matrix[posTet[0]+zeile][posTet[1]-1]='.'
    return [posTet, randRahmen]

def nachUnten(matrix, activeTetramino, posTet, randRahmen):
    moeglich = False
    moeglichBlock = True
    moeglichSpielfeld = False
    # Werden die Spielfeld abmessungen eingehalten?
    if (posTet[0]+len(activeTetramino))<len(matrix)-1:
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
        if (posTet[0]+len(activeTetramino))<len(matrix)-1: #falls noch nicht ganz unten 
            for spalte in range(len(activeTetramino[0])):
                if matrix[posTet[0]+len(activeTetramino)][posTet[1]+spalte]!='.':
                    moeglichBlock=False
    if moeglichSpielfeld and moeglichBlock:
        moeglich= True
    if moeglich:
        posTet[0]=posTet[0]+1
        for spalte in range(len(activeTetramino[0])):
            matrix[posTet[0]-1][posTet[1]+spalte]='.'
    return [posTet, randRahmen, moeglich]

def hardDrop(matrix, activeTet, posTet, randRahmen):
    moeglich=True
    while moeglich:
        rg=nachUnten(matrix,activeTet, posTet, randRahmen)
        posTet=rg[0]
        randRahmen=rg[1]
        moeglich=rg[2]
    matrix = tetInMatrix(matrix, activeTet, posTet, False)
    return matrix

#def randRahmenErmitteln(matrix, activeTetramino, posTet, randRahmen)
    #links:

    #rechts:

    #unten:


#    return randRahmen

def inputVerarbeiten(matrix, activeTetramino, posTet, score, clearedLines, randRahmen):
    cmd=raw_input()
    #cmdListe=cmd.split(' ')
    cmdListe=cmd.replace(" ","")
    anzahlInputs=len(cmdListe)
    eingabe=0
    while eingabe<anzahlInputs:
        if cmdListe[eingabe]=="q":
            sys.exit()
        elif cmdListe[eingabe]=="p":
            ausgeben(matrix,1,1,1)
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
            posTet = [0,4]
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("I")
        elif cmdListe[eingabe]=="O":
            posTet = [0,5]
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("O")
        elif cmdListe[eingabe]=="Z":
            posTet = [0,4]
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("Z")
        elif cmdListe[eingabe]== "S":
            posTet = [0,4]
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("S")
        elif cmdListe[eingabe]== "J":
            posTet = [0,4]
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("J")
        elif cmdListe[eingabe]=="L":
            activeTetramino = setTetramino("L")
            posTet = [0,4]
            randRahmen = [0,0,0]
        elif cmdListe[eingabe]=="T":
            posTet = [0,4]
            randRahmen=[0,0,0]
            activeTetramino = setTetramino("T")
        elif cmdListe[eingabe]=="t":
            ausgeben(activeTetramino,0,0,0)
        # Rotieren
        elif cmdListe[eingabe]==")":
            rg = rotateClockwise(matrix,activeTetramino, posTet ,randRahmen)
            activeTetramino = rg[0]
            posTet = rg[1]
            randRahmen = rg[2]
        elif cmdListe[eingabe]=="(":
            rg = rotateCounterClockwise(matrix,activeTetramino, posTet,randRahmen)
            activeTetramino = rg[0]
            posTet = rg[1]
            randRahmen = rg[2]
        # Verschiedene Ausgabemoeglichkeiten
        elif cmdListe[eingabe] ==";":
            print("")
        elif cmdListe[eingabe] =="P":
            matrix = tetInMatrix(matrix, activeTetramino, posTet, True)
            ausgeben(matrix,1,1,1)
        # Tetramino verschieben:
        elif cmdListe[eingabe]=="<":
            rg = nachLinks(matrix, activeTetramino, posTet, randRahmen)
            posTet = rg[0]
            randRahmen = rg[1]
        elif cmdListe[eingabe]==">":
            rg = nachRechts(matrix, activeTetramino, posTet, randRahmen)
            posTet = rg[0]
            randRahmen = rg[1]
        elif cmdListe[eingabe]=="v":
            rg = nachUnten(matrix, activeTetramino, posTet, randRahmen)
            posTet = rg[0]
            randRahmen = rg[1]
        elif cmdListe[eingabe]=="V":
            matrix = hardDrop(matrix, activeTetramino, posTet, randRahmen)
        else:
            print("falsche eingabe")
            print("input: " + cmdListe[eingabe])
        eingabe=eingabe+1
    return [matrix, activeTetramino, posTet, score, clearedLines, randRahmen]

def main():
    #Startwerte setzen
    matrix = [['.' for x in range(12)]for x in range(23)]
    #Spielfeldgrenzen eintragen:
    for spalte in range(len(matrix[0])):
        matrix[-1][spalte]='X'
    for zeile in range(len(matrix)):
        matrix[zeile][0]='X'
        matrix[zeile][-1]='X'
    score = 0
    clearedLines = 0
    activeTetramino = []
    posTet = [0,5]          # Position des Tetraminos [zeile,spalte]
    randRahmen = [0,0,0]    # definiert, wie weit andere Bloecke oder der Spielfeldrand 
                            # in das Tet hinein ragen
                            # [links,rechts, unten]
    while True:
        ergebnis=inputVerarbeiten(matrix, activeTetramino, posTet ,score, clearedLines, randRahmen)
        matrix = ergebnis[0]
        activeTetramino = ergebnis[1]
        posTet = ergebnis[2]
        score = ergebnis[3]
        clearedLines = ergebnis[4]
        randRahmen = ergebnis[5]
    return

if __name__ == '__main__':
    main()


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
