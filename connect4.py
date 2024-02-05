# spieldfeld x=7 y=6
feld = [[" . "," . "," . "," . "," . "," . "," . "],
        [" . "," . "," . "," . "," . "," . "," . "],
        [" . "," . "," . "," . "," . "," . "," . "],
        [" . "," . "," . "," . "," . "," . "," . "],
        [" . "," . "," . "," . "," . "," . "," . "],
        [" . "," . "," . "," . "," . "," . "," . "]]

regeln = [[" | "," | "," | "," | "," | "," | "," | "],
        [" 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "]]

player = " X "
done = 0

def reihe():
    global player
    if player == " X ":
        player = " O "
    else:
        player = " X "

def draw(liste):
    for row in liste:
        print(*row, sep=" |")

def spielzug(ein):
    global player
    for i in range(1, 7):
        if feld[-i][ein] == " . ":
            feld[-i][ein] = player
            reihe()
            check()
            break

def eingabe():
    draw(feld)
    draw(regeln)
    try:
        ein = (int(input(f"Spieler {player} ist an der Reihe\nBitte Spielzug wählen\n"))-1)
        if ein >= 0 and ein <= 6:
            if feld[0][ein] != " . ":
                print("Feld belegt. Bitte anderen Spielzug wählen.")
                eingabe()
            else:
                spielzug(ein)
        else:
            print("Ungültige Eingabe. Bitte nur Zahlen zwischen 1 und 7 eingeben")
    except:
        print("Ungültige Eingabe. Bitte nur Zahlen zwischen 1 und 7 eingeben")
        eingabe()



def check():
    global done
    for i in range(6):      #check rows
        for j in range(4):
            if feld[i][j] == feld[i][j+1] == feld[i][j+2] == feld[i][j+3] !=" . ":
                done = 1
                return done
    for t in range(7):
        for r in range(3):
            if feld[r][t] == feld[r+1][t] == feld[r+2][t] == feld[r+3][t] != " . ":
                done = 1
                return done

    

def play():
    global done
    while done == 0:
        eingabe()
    reihe()
    print(f"Spieler {player} gewinnt.")

play()