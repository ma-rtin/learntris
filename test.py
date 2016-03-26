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

def rotateClockwise(matrix, tet, zeileTetramino, spalteTetramino, linksAnRand, rechtsAnRand):
    anzahlZeilen = len(tet)
    anzahlSpalten= len(tet[0])

    #links in Spielfeld schieben
    for i in range(linksAnRand):
        rg=nachRechts(matrix, tet, zeileTetramino, spalteTetramino, linksAnRand, rechtsAnRand)
        zeileTetramino=rg[0]
        spalteTetramino=rg[1]
        linksAnRand=rg[2]
        rechtsAnRand=rg[3]
    #rechts in Spielfeld schieben
    for i in range(rechtsAnRand):
        rg=nachLinks(matrix, tet, zeileTetramino, spalteTetramino, linksAnRand, rechtsAnRand)
        zeileTetramino=rg[0]
        spalteTetramino=rg[1]
        linksAnRand=rg[2]
        rechtsAnRand=rg[3]

    tetNeu=[['0' for x in range(len(tet))]for x in range(len(tet))]
    #erste Zeile muss in letzte Spalte
    for zeile in range(anzahlZeilen):
        for spalte in range(anzahlSpalten):
            tetNeu[spalte][-1-zeile]=tet[zeile][spalte]
    return [tetNeu, zeileTetramino, spalteTetramino, linksAnRand, rechtsAnRand]

def rotateCounterClockwise(matrix, tet, zeileTetramino, spalteTetramino, linksAnRand, rechtsAnRand):
    anzahlZeilen = len(tet)
    anzahlSpalten= len(tet[0])

    #links in Spielfeld schieben
    for i in range(linksAnRand):
        rg=nachRechts(matrix, tet, zeileTetramino, spalteTetramino, linksAnRand, rechtsAnRand)
        zeileTetramino=rg[0]
        spalteTetramino=rg[1]
        linksAnRand=rg[2]
        rechtsAnRand=rg[3]
    #rechts in Spielfeld schieben
    for i in range(rechtsAnRand):
        rg=nachLinks(matrix, tet, zeileTetramino, spalteTetramino, linksAnRand, rechtsAnRand)
        zeileTetramino=rg[0]
        spalteTetramino=rg[1]
        linksAnRand=rg[2]
        rechtsAnRand=rg[3]

    tetNeu=[['0' for x in range(len(tet))]for x in range(len(tet))]
    #erste spalte muss in letzte zeile
    for zeile in range(anzahlZeilen):
        for spalte in range(anzahlSpalten):
            tetNeu[-1-spalte][zeile]=tet[zeile][spalte]
    return [tetNeu, zeileTetramino, spalteTetramino, linksAnRand, rechtsAnRand]



def tetInMatrix(matrix, tet, zeileTetramino, spalteTetramino):
    anzahlZeilen = len(tet)
    anzahlSpalten= len(tet[0])
    for zeile in range(anzahlZeilen):
        for spalte in range(anzahlSpalten):
            if (spalteTetramino+spalte)>=0 and (spalteTetramino+spalte)<=(len(matrix[0])-1):
                hilfsstring=tet[zeile][spalte]
                hilfsstring=str(hilfsstring)
                hilfsstring=hilfsstring.upper()
                matrix[zeileTetramino+zeile][spalteTetramino+spalte]=hilfsstring
    return

def nachLinks(matrix, activeTetramino, zeileTetramino, spalteTetramino, linksAnRand, rechtsAnRand):
    moeglich=False
    if spalteTetramino > 0:
        moeglich = True
    else:
        linkeSpalteLeer = True
        for zeile in range(len(activeTetramino)):
            if activeTetramino[zeile][linksAnRand]!='.':
                linkeSpalteLeer = False
        if linkeSpalteLeer:
            moeglich=True
            linksAnRand = linksAnRand +1
    if moeglich:
        # Tetramino verschieben
        spalteTetramino = spalteTetramino - 1
        rechteSpalte=spalteTetramino+len(activeTetramino)-1
        if rechtsAnRand != 0:
            rechtsAnRand = rechtsAnRand-1
        # frei gewordenen Bereich leeren
        for zeile in range(len(activeTetramino)):
            if (rechteSpalte+1)<len(matrix[0]):
                matrix[zeileTetramino+zeile][rechteSpalte+1]='.'
    return [zeileTetramino,spalteTetramino, linksAnRand, rechtsAnRand]

def nachRechts(matrix, activeTetramino, zeileTetramino, spalteTetramino,linksAnRand, rechtsAnRand):
    moeglich=False
    if (spalteTetramino+len(activeTetramino)-1) < (len(matrix[0])-1):
        moeglich=True
    else:
        rechteSpalteLeer = True
        for zeile in range(len(activeTetramino)):
            if activeTetramino[zeile][len(activeTetramino)-1-rechtsAnRand]!='.':
                rechteSpalteLeer = False
        if rechteSpalteLeer:
            moeglich=True
            rechtsAnRand = rechtsAnRand +1
    if moeglich:
        # Tetramino verschieben
        spalteTetramino = spalteTetramino + 1
        if linksAnRand != 0:
            linksAnRand = linksAnRand -1
        # frei gewordenen Bereich leeren
        for zeile in range(len(activeTetramino)):
            if (spalteTetramino-1)>=0:
                matrix[zeileTetramino+zeile][spalteTetramino-1]='.'
    return [zeileTetramino,spalteTetramino,linksAnRand, rechtsAnRand]

def nachUnten(matrix, activeTetramino, zeileTetramino, spalteTetramino):
    zeileTetramino = zeileTetramino+1
    for spalte in range(len(activeTetramino[0])):
        matrix[zeileTetramino-1][spalteTetramino+spalte]='.'
    return [zeileTetramino,spalteTetramino]



def inputVerarbeiten(matrix, activeTetramino, zeileTetramino, spalteTetramino, score, clearedLines, linksAnRand, rechtsAnRand):
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
            activeTetramino = setTetramino("I")
        elif cmdListe[eingabe]=="O":
            spalteTetramino = 4
            activeTetramino = setTetramino("O")
        elif cmdListe[eingabe]=="Z":
            spalteTetramino = 3
            activeTetramino = setTetramino("Z")
        elif cmdListe[eingabe]== "S":
            spalteTetramino = 3
            activeTetramino = setTetramino("S")
        elif cmdListe[eingabe]== "J":
            spalteTetramino = 3
            activeTetramino = setTetramino("J")
        elif cmdListe[eingabe]=="L":
            activeTetramino = setTetramino("L")
            spalteTetramino = 3
        elif cmdListe[eingabe]=="T":
            spalteTetramino = 3
            activeTetramino = setTetramino("T")
        elif cmdListe[eingabe]=="t":
            ausgeben(activeTetramino)
        elif cmdListe[eingabe]==")":
            rg = rotateClockwise(matrix,activeTetramino, zeileTetramino, spalteTetramino,linksAnRand, rechtsAnRand)
            activeTetramino = rg[0]
            zeileTetramino = rg[1]
            spalteTetramino = rg[2]
            linksAnRand = rg[3]
            rechtsAnRand = rg[4]
        elif cmdListe[eingabe]=="(":
            rg = rotateCounterClockwise(matrix,activeTetramino, zeileTetramino, spalteTetramino,linksAnRand, rechtsAnRand)
            activeTetramino = rg[0]
            zeileTetramino = rg[1]
            spalteTetramino = rg[2]
            linksAnRand = rg[3]
            rechtsAnRand = rg[4]
        elif cmdListe[eingabe] ==";":
            print("")
        elif cmdListe[eingabe] =="P":
            tetInMatrix(matrix, activeTetramino, zeileTetramino, spalteTetramino)
            ausgeben(matrix)
        elif cmdListe[eingabe]=="<":
            rg = nachLinks(matrix, activeTetramino, zeileTetramino, spalteTetramino, linksAnRand,rechtsAnRand)
            zeileTetramino = rg[0]
            spalteTetramino = rg[1]
            linksAnRand = rg[2]
            rechtsAnRand = rg[3]
        elif cmdListe[eingabe]==">":
            rg = nachRechts(matrix, activeTetramino, zeileTetramino, spalteTetramino,linksAnRand, rechtsAnRand)
            zeileTetramino = rg[0]
            spalteTetramino = rg[1]
            linksAnRand = rg[2]
            rechtsAnRand = rg[3]
        elif cmdListe[eingabe]=="v":
            zeileSpalte = nachUnten(matrix, activeTetramino, zeileTetramino, spalteTetramino)
            zeileTetramino = zeileSpalte[0]
            spalteTetramino = zeileSpalte[1]
        else:
            print("falsche eingabe")
            print("input: " + cmdListe[eingabe])
        eingabe=eingabe+1
    return [matrix, activeTetramino, zeileTetramino, spalteTetramino, score, clearedLines, linksAnRand, rechtsAnRand]

def main():
    #Startwerte setzen
    matrix = [['.' for x in range(10)]for x in range(22)]
    score = 0
    clearedLines = 0
    activeTetramino = []
    zeileTetramino = 0
    spalteTetramino = 4
    rechtsAnRand = 0    #definiert wie weit der leere Teil des Tetramino Rahmens
    linksAnRand = 0     #aus dem Spielfeld heraus ragt
    while True:
        ergebnis=inputVerarbeiten(matrix, activeTetramino, zeileTetramino, spalteTetramino,score, clearedLines, linksAnRand, rechtsAnRand)
        matrix = ergebnis[0]
        activeTetramino = ergebnis[1]
        zeileTetramino = ergebnis[2]
        spalteTetramino = ergebnis[3]
        score = ergebnis[4]
        clearedLines = ergebnis[5]
        linksAnRand = ergebnis[6]
        rechtsAnRand = ergebnis[7]
    return

if __name__ == '__main__':
    main()


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
