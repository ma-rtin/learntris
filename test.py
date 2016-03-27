#!/usr/bin/env python

pass

import sys

def ausgeben(matrix, offsetLinks, offsetRechts, offsetUnten,leer):
# verschiedene Matrizen ausgeben
# matrix        :Liste[][]  Inhalt zum ausgeben
# offsetLinks   :Integer    linke Spalten der Matrix, die nicht ausgegeben werden
# offsetRechts  :Integer    rechte Spalten der Matrix, die nicht ausgegeben werden
# offsetUnten   :Integer    untere Zeilen, die nicht ausgegeben werden
# leer          :Boolean    Falls True wird Inhalt der Matrix mit '.' ueberschrieben

    zeilenAnzahl = len(matrix)-offsetUnten
    spaltenAnzahl = len(matrix[0]) - offsetRechts-offsetLinks
    for zeile in range(zeilenAnzahl):
        for spalte in range(spaltenAnzahl):
            if leer:
                sys.stdout.write(". ")
            else:
                sys.stdout.write(matrix[zeile][spalte+offsetLinks]+" ")
        sys.stdout.write("\n")
    return

def matrixEinlesen(matrix):
# Testzwecke, eine Matrix mit Inhalt fuer das 22x10 Spielfeld kann eingelesen werden
# matrix        :Liste[][]  Matrix, in die der Inhalt geschrieben wird
#                           Rahmen 2 Spalten links und rechts und 2 Zeilen unten

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
            matrix[zeile][spalte+2]=eingabe[spalte]

    return

def matrixLeeren(matrix):
# Inhalt der Matrix wird mit '.' ueberschrieben, der Rahmen, 2 Spalten links und rechts und
# 2 Zeilen unten mit dem Rahmen werden nicht veraendert
    for zeile in range(22):
        for spalte in range(10):
            matrix[zeile][spalte+2]='.'
    return

def zeigeZahl(zahl):
# Zahl ausgeben, eigentlich unnoetig, evtl spaeter fuer Score ausgabe veraendern
    print(str(zahl))
    return

def matrixSimulation(matrix, score, clearedLines):
# Testen ob komplett volle Zeilen vorhanden sind. Falls ja, werden diese mit '.' ueberschrieben
# Die Anzahl der geclearten Zeilen, sowie der Punktestand werden erhoeht
# spaeter sollten die oberen Zeilen dann automatisch nachruecken

# matrix        :Liste[][]
# score         :Integer        +100  wenn eine volle Zeile gefunden wird
# clearedLines  :Integer        +1 wenn eine volle Zeile gefunden wird
    for zeile in range(22):
        zeileVoll=True
        for spalte in range(10):
            if matrix[zeile][spalte+2]=='.':
                zeileVoll = False
        if zeileVoll:
            for spalte in range(10):
                matrix[zeile][spalte+2]='.'
            score=score+100
            clearedLines = clearedLines+1
    return [score,clearedLines]


def setTetramino(tet):
# Aktiven Tetramino festlegen
# tet   :String     kann die Werte "I","O","Z","S","J","L","T" annehmen

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
# Rotiert das Tetramino im Uhrzeigersinn,
# nur moeglich wenn der komplette Rahmen in der Matrix frei ist
# spaeter verschieben, wenn ein Teil des Rahmens verdeckt ist

# matrix    :Liste[][]
# tet       :Liste[][]
# posTet    :Liste[zeile,spalte]

    moeglich = True
    for zeile in range(len(tet)):
        for spalte in range(len(tet[0])):
            strTet=tet[zeile][spalte]
            strTet=strTet.upper()
            strMat=matrix[posTet[0]+zeile][posTet[1]+spalte]
            strMat=strMat.upper()
            if strMat != '.': # nur testen falls matrix nicht leer
                if strTet != strMat:
                    moeglich = False

    if moeglich:
        #rahmen in matrix leeren:
        for zeile in range(len(tet)):
            for spalte in range(len(tet[0])):
                matrix[posTet[0]+zeile][posTet[1]+spalte]='.'

        tetNeu=[['0' for x in range(len(tet))]for x in range(len(tet))]
        #erste Zeile muss in letzte Spalte
        for zeile in range(len(tet)):
            for spalte in range(len(tet[0])):
                tetNeu[spalte][-1-zeile]=tet[zeile][spalte]
        tet=tetNeu
    return [tet, posTet, randRahmen]

def rotateCounterClockwise(matrix, tet, posTet, randRahmen):

# Rotiert das Tetramino gegen Uhrzeigersinn,
# nur moeglich wenn der komplette Rahmen in der Matrix frei ist
# spaeter verschieben, wenn ein Teil des Rahmens verdeckt ist

# matrix    :Liste[][]
# tet       :Liste[][]
# posTet    :Liste[zeile,spalte]

    moeglich = True
    for zeile in range(len(tet)):
        for spalte in range(len(tet[0])):
            strTet=tet[zeile][spalte]
            strTet=strTet.upper()
            strMat=matrix[posTet[0]+zeile][posTet[1]+spalte]
            strMat=strMat.upper()
            if strMat != '.': #nur testen falls matrix nicht leer
                if strTet != strMat:
                    moeglich = False

    if moeglich:
        #rahmen in matrix leeren:
        for zeile in range(len(tet)):
            for spalte in range(len(tet[0])):
                matrix[posTet[0]+zeile][posTet[1]+spalte]='.'

        tetNeu=[['0' for x in range(len(tet))]for x in range(len(tet))]
        #erste spalte muss in letzte zeile
        for zeile in range(len(tet)):
            for spalte in range(len(tet[0])):
                tetNeu[-1-spalte][zeile]=tet[zeile][spalte]
        tet=tetNeu
    return [tet, posTet, randRahmen]

def tetInMatrix(matrix, tet, posTet, caps):
# Speichert einen Tetramino in die Matrix, dabei werden nur Werte von Stellen uebernommen,
# an denen der Rahmen des Tetraminos nicht leer ('.') ist

# matrix    :Liste[][]
# tet       :Liste[][]
# posTet    :[zeile,spalte]
# caps      :Boolean        Falls True, Werte werden in Grossbuchstaben uebernommen

    for zeile in range(len(tet)):
        for spalte in range(len(tet[0])):
            if tet[zeile][spalte]!='.':
                # Seitenrand testen
                if (posTet[1]+spalte)>=2 and (posTet[1]+spalte)<=(len(matrix[0])-3):
                    # Unteren Rand testen
                    if (posTet[0]+zeile) <= (len(matrix)-3):
                        hilfsstring=tet[zeile][spalte]
                        hilfsstring=str(hilfsstring)
                        if caps:
                            hilfsstring=hilfsstring.upper()
                        matrix[posTet[0]+zeile][posTet[1]+spalte]=hilfsstring
    return matrix

def nachLinks(matrix, actTet, posTet, randRahmen):
# Verschiebt da Tetramino nach Links, falls der Bereich nicht in der matrix blockiert wird

# matrix        :Liste[][]
# actTet        :Liste[][]
# posTet        :[zeile,spalte]

    moeglich=True
    for zeile in range(len(actTet)):
        for spalte in range(len(actTet[0])):
            if actTet[zeile][spalte]!='.': #stelle nicht leer im tetramino?
                if matrix[posTet[0]+zeile][posTet[1]-1+spalte]!='.': #stelle links davon leer in matrix?
                    moeglich=False
                break #in jeder zeile muss nur eine stelle getestet werden

    if moeglich:
        # Tet verschieben:
        posTet[1]=posTet[1]-1
        # rand rechts verkleinern
        if randRahmen[1]!=0:
            randRahmen[1]=randRahmen[1]-1
        # frei gewordenen Bereich leeren:
        for spalte in range(len(actTet[0])):
            for zeile in range(len(actTet)):
                    if posTet[1]+spalte+1<len(matrix)-3:
                        if actTet[zeile][spalte]!='.':
                            matrix[posTet[0]+zeile][posTet[1]+spalte+1]='.'
        # tet in matrix speichern
        tetInMatrix(matrix, actTet, posTet, True)
        #testen wie weit in den Rahmen verschoben wurde
    return [posTet, randRahmen]

def nachRechts(matrix, actTet, posTet, randRahmen):
# Verschiebt da Tetramino nach rechts, falls der Bereich nicht in der matrix blockiert wird             

# matrix        :Liste[][]
# actTet        :Liste[][]
# posTet        :[zeile,spalte]

    moeglich=True
    for zeile in range(len(actTet)):
        for spalte in range(len(actTet[0])):
            #print("["+str(zeile)+"]["+str(-1-spalte)+"]="+str(actTet[zeile][-1-spalte]))
            if actTet[zeile][-1-spalte]!='.': #stelle nicht leer im tetramino?
                if matrix[posTet[0]+zeile][posTet[1]+len(actTet[0])-spalte]!='.': #stelle rechts davon leer in matrix?
                    moeglich=False
                break #in jeder zeile muss nur eine stelle getestet werdenh=True
    if moeglich:
        # Tet verschieben:
        posTet[1]=posTet[1]+1
        # rand links verkleinern
        if randRahmen[0]!=0:
            randRahmen[0]=randRahmen[0]-1
        # frei gewordenen Bereich leeren:
        for spalte in range(len(actTet[0])):
            if posTet[1]+spalte-1>=2:
                for zeile in range(len(actTet)):
                    if actTet[zeile][spalte]!='.':
                        matrix[posTet[0]+zeile][posTet[1]+spalte-1]='.'
        # tet in matrix speichern
        tetInMatrix(matrix, actTet, posTet, True)
        #testen wie weit in den Rahmen verschoben wurde
    return [posTet, randRahmen]

def nachUnten(matrix, actTet, posTet, randRahmen, gameOver):
 # Verschiebt da Tetramino nach unten, falls der Bereich nicht in der matrix blockiert wird              
# matrix        :Liste[][]
# actTet        :Liste[][]
# posTet        :[zeile,spalte]
# gameOver      :Boolean            True, falls Tet ganz unten und obere Zeile belegt

    moeglich=True
    for spalte in range(len(actTet[0])):
        for zeile in range(len(actTet)):
            if actTet[-1-zeile][spalte]!='.': # wenn stelle nicht leer im actTet
                if matrix[posTet[0]+len(actTet)-zeile][posTet[1]+spalte]!='.':
                    moeglich=False
                break
    if moeglich:
        # Tet verschieben:
        posTet[0]=posTet[0]+1
        # frei gewordenen Bereich leeren:
        for spalte in range(len(actTet[0])):
            for zeile in range(len(actTet)):
                if actTet[zeile][spalte]!='.':
                    matrix[posTet[0]+zeile-1][posTet[1]+spalte]='.'
        # tet in matrix speichern
        tetInMatrix(matrix, actTet, posTet, True)
    #gameOver testen:
    else:
        for spalte in range(len(matrix[0])-4):
            if matrix[0][spalte+2]!='.':
                gameOver=True
    return [posTet, randRahmen, moeglich, gameOver]

def hardDrop(matrix, activeTet, posTet, randRahmen, gameOver):
# verschiebt das Tetramino so weit nach unten wie moeglich

    moeglich=True
    while moeglich:
        rg=nachUnten(matrix,activeTet, posTet, randRahmen, gameOver)
        posTet=rg[0]
        randRahmen=rg[1]
        moeglich=rg[2]
        gameOver=rg[3]
    matrix = tetInMatrix(matrix, activeTet, posTet, False)
    return [matrix,gameOver]

def randRahmenErmitteln(matrix, actTet, posTet, randRahmen):
    #tet mit matrixinhalt vergleichen
    #links:
    imRahmenLinks=False
    for zeile in range(len(actTet)-randRahmen[2]):
        hilfsstring=str(actTet[zeile][randRahmen[0]])
        hilfsstring=hilfsstring.upper()
        if matrix[posTet[0]+zeile][posTet[1]]!=hilfsstring:
            imRahmenLinks=True
    if imRahmenLinks:
        randRahmen[0]=randRahmen[0]+1
    # links neu:
#    spalteGefunden = False
#    randRahmen[0]=0
#    while not spalteGefunden:
#        imRahmenLinks=False
#        for zeile in range(len(actTet)-randRahmen[2]):
#            print("zeile: "+str(zeile)+" spalte: "+str(randRahmen[0]))
#            stringTet = str(actTet[zeile][randRahmen[0]])
#            stringTet = stringTet.upper()
#            print("sT: "+stringTet)
#            stringMat = str(matrix[posTet[0]+zeile][posTet[1]])
#            stringMat = stringMat.upper()
#            print("sM: "+stringMat)
#            if stringMat!=stringTet:
#                imRahmenLinks=True
#        if imRahmenLinks:
#            randRahmen[0]=randRahmen[0]+1
#        else:
#            spalteGefunden=True
    #rechts:
    imRahmenRechts=False
    for zeile in range(len(actTet)-randRahmen[2]):
        hilfsstring=str(actTet[zeile][-1-randRahmen[1]])
        hilfsstring=hilfsstring.upper()
        if matrix[posTet[0]+zeile][posTet[1]+len(actTet[0])-1-randRahmen[1]]!=hilfsstring:
            imRahmenRechts=True
    if imRahmenRechts:
        randRahmen[1]=randRahmen[1]+1
    #unten:
    #print("randErmitteln Unten:")
    imRahmenUnten=False
    for spalte in range(len(actTet[0])-randRahmen[0]-randRahmen[1]):
        hilfsstring=str(actTet[-1][spalte+randRahmen[0]])
        hilfsstring=hilfsstring.upper()
        if matrix[posTet[0]+len(actTet)-1-randRahmen[2]][posTet[1]+spalte+randRahmen[0]]!=hilfsstring:
            imRahmenUnten=True
    if imRahmenUnten:
        randRahmen[2]=randRahmen[2]+1

    print("rr0: "+str(randRahmen[0]))
    print("rr1: "+str(randRahmen[1]))
    print("rr2: "+str(randRahmen[2]))

    return randRahmen

def mainMenu():
    print("Learntris (c) 1992 Tetraminex, Inc.")
    print("Press start button to begin.")
    return

def pauseScreen(matrix):
    #ausgeben(matrix,1,1,1,True)
    print("Paused")
    print("Press start button to continue.")
    return

def inputVerarbeiten(matrix, activeTetramino, posTet, score, clearedLines, randRahmen, status, gameOver):
# Inputs fuer Tests verarbeiten

    cmd=raw_input()
    cmdListe=cmd.replace(" ","")
    anzahlInputs=len(cmdListe)
    eingabe=0
    while eingabe<anzahlInputs:
        if cmdListe[eingabe]=="q":
            sys.exit()
        elif cmdListe[eingabe]=="p":
            if status=="titleScreen":
                mainMenu()
            elif status=="pause":
                pauseScreen(matrix)
            else:
                ausgeben(matrix,2,2,2,False)
                if gameOver:
                    print("Game Over")
        elif cmdListe[eingabe]=="@":
            status="titleScreen"
        elif cmdListe[eingabe]=="!":
            if status=="imSpiel":
                status="pause"
            elif status =="pause":
                status="imSpiel"
            elif status =="titleScreen":
                status="imSpiel"
            else:
                status="imSpiel"
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
            posTet = [0,5]
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("I")
        elif cmdListe[eingabe]=="O":
            posTet = [0,6]
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("O")
        elif cmdListe[eingabe]=="Z":
            posTet = [0,5]
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("Z")
        elif cmdListe[eingabe]== "S":
            posTet = [0,5]
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("S")
        elif cmdListe[eingabe]== "J":
            posTet = [0,5]
            randRahmen = [0,0,0]
            activeTetramino = setTetramino("J")
        elif cmdListe[eingabe]=="L":
            activeTetramino = setTetramino("L")
            posTet = [0,5]
            randRahmen = [0,0,0]
        elif cmdListe[eingabe]=="T":
            posTet = [0,5]
            randRahmen=[0,0,0]
            activeTetramino = setTetramino("T")
        elif cmdListe[eingabe]=="t":
            ausgeben(activeTetramino,0,0,0,False)
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
            ausgeben(matrix,2,2,2,False)
            if gameOver:
                print("Game Over")
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
            rg = nachUnten(matrix, activeTetramino, posTet, randRahmen, gameOver)
            posTet = rg[0]
            randRahmen = rg[1]
            gameOver = rg[3]
        elif cmdListe[eingabe]=="V":
            rg = hardDrop(matrix, activeTetramino, posTet, randRahmen, gameOver)
            matrix= rg[0]
            gameOver=rg[1]
            activeTetramino = []
        else:
            print("falsche eingabe")
            print("input: " + cmdListe[eingabe])
        eingabe=eingabe+1
    return [matrix, activeTetramino, posTet, score, clearedLines, randRahmen,status, gameOver]

def main():
    #Startwerte setzen
    matrix = [['.' for x in range(14)]for x in range(24)]
    #Spielfeldgrenzen eintragen:
    for spalte in range(len(matrix[0])):
        matrix[-1][spalte]='X'
        matrix[-2][spalte]='X'
    for zeile in range(len(matrix)):
        matrix[zeile][0]='X'
        matrix[zeile][1]='X'
        matrix[zeile][-1]='X'
        matrix[zeile][-2]='X'
    status='imSpiel'
    gameOver = False
    score = 0
    clearedLines = 0
    activeTetramino = []
    posTet = [0,5]          # Position des Tetraminos [zeile,spalte]
    randRahmen = [0,0,0]    # definiert, wie weit andere Bloecke oder der Spielfeldrand 
                            # in das Tet hinein ragen
                            # [links,rechts, unten]
    while True:
        ergebnis=inputVerarbeiten(matrix, activeTetramino, posTet ,score, clearedLines, randRahmen, status, gameOver)
        matrix = ergebnis[0]
        activeTetramino = ergebnis[1]
        posTet = ergebnis[2]
        score = ergebnis[3]
        clearedLines = ergebnis[4]
        randRahmen = ergebnis[5]
        status=ergebnis[6]
        gameOver = ergebnis[7]
    return

if __name__ == '__main__':
    main()


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
