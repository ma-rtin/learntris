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

def rotateClockwise(tet):
    anzahlZeilen = len(tet)
    anzahlSpalten= len(tet[0])

    tetNeu=[['0' for x in range(len(tet))]for x in range(len(tet))]
    #erste Zeile muss in letzte Spalte
    for zeile in range(anzahlZeilen):
        for spalte in range(anzahlSpalten):
            tetNeu[spalte][-1-zeile]=tet[zeile][spalte]
    return tetNeu

def tetInMatrix(matrix, tet, zeileTetramino, spalteTetramino):
    anzahlZeilen = len(tet)
    anzahlSpalten= len(tet[0])
    for zeile in range(anzahlZeilen):
        for spalte in range(anzahlSpalten):
            hilfsstring=tet[zeile][spalte]
            hilfsstring=str(hilfsstring)
            hilfsstring=hilfsstring.upper()
            matrix[zeileTetramino+zeile][spalteTetramino+spalte]=hilfsstring
    return

def nachLinks(matrix, activeTetramino, zeileTetramino, spalteTetramino):
    if spalteTetramino > 0:
        spalteTetramino = spalteTetramino - 1
        rechteSpalte=spalteTetramino+len(activeTetramino)-1
        for zeile in range(len(activeTetramino)):
            matrix[zeileTetramino+zeile][rechteSpalte+1]='.'
    return [zeileTetramino,spalteTetramino]

def nachRechts(matrix, activeTetramino, zeileTetramino, spalteTetramino):
    if (spalteTetramino+len(activeTetramino)-1) < (len(matrix[0])-1):
        spalteTetramino = spalteTetramino + 1
        for zeile in range(len(activeTetramino)):
            matrix[zeileTetramino+zeile][spalteTetramino-1]='.'
    return [zeileTetramino,spalteTetramino]

def nachUnten(matrix, activeTetramino, zeileTetramino, spalteTetramino):
    zeileTetramino = zeileTetramino+1
    for spalte in range(len(activeTetramino[0])):
        matrix[zeileTetramino-1][spalteTetramino+spalte]='.'
    return [zeileTetramino,spalteTetramino]



def inputVerarbeiten(matrix, activeTetramino, zeileTetramino, spalteTetramino, score, clearedLines):
    #matrix = [['.' for x in range(10)]for x in range(22)]
    #score = 0
    #clearedLines = 0
    #activeTetramino = []
    #zeileTetramino = 0
    #spalteTetramino = 4
    #Inputs abrufen und dementsprechende Funktionen aufrufen
    #while True:
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
            activeTetramino = rotateClockwise(activeTetramino)
        elif cmdListe[eingabe] ==";":
            print("")
        elif cmdListe[eingabe] =="P":
            tetInMatrix(matrix, activeTetramino, zeileTetramino, spalteTetramino)
            ausgeben(matrix)
        elif cmdListe[eingabe]=="<":
            zeileSpalte = nachLinks(matrix, activeTetramino, zeileTetramino, spalteTetramino)
            zeileTetramino = zeileSpalte[0]
            spalteTetramino = zeileSpalte[1]
        elif cmdListe[eingabe]==">":
            zeileSpalte = nachRechts(matrix, activeTetramino, zeileTetramino, spalteTetramino)
            zeileTetramino = zeileSpalte[0]
            spalteTetramino = zeileSpalte[1]
        elif cmdListe[eingabe]=="v":
            zeileSpalte = nachUnten(matrix, activeTetramino, zeileTetramino, spalteTetramino)
            zeileTetramino = zeileSpalte[0]
            spalteTetramino = zeileSpalte[1]
        else:
            print("falsche eingabe")
            print("input: " + cmdListe[eingabe])
        eingabe=eingabe+1
    return [matrix, activeTetramino, zeileTetramino, spalteTetramino, score, clearedLines]

def main():
    matrix = [['.' for x in range(10)]for x in range(22)]
    score = 0
    clearedLines = 0
    activeTetramino = []
    zeileTetramino = 0
    spalteTetramino = 4
    while True:
        ergebnis=inputVerarbeiten(matrix, activeTetramino, zeileTetramino, spalteTetramino,score, clearedLines)
        matrix = ergebnis[0]
        activeTetramino = ergebnis[1]
        zeileTetramino = ergebnis[2]
        spalteTetramino = ergebnis[3]
        score = ergebnis[4]
        clearedLines = ergebnis[5]
    return
if __name__ == '__main__':
    main()


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
