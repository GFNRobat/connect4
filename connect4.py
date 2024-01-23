# spieldfeld x=7 y=6
feld = [[" . "," . "," . "," . "," . "," . "," . "],
        [" . "," . "," . "," . "," . "," . "," . "],
        [" . "," . "," . "," . "," . "," . "," . "],
        [" . "," . "," . "," . "," . "," . "," . "],
        [" . "," . "," . "," . "," . "," . "," . "],
        [" . "," . "," . "," . "," . "," . "," . "]]

player = " X "

def draw():
    for row in feld:
        print(*row, sep=" |")

def spielzug(ein):
    pass

def eingabe():
    ein = input(f"Spieler {player} ist an der Reihe\nBitte Spielzug wählen")
    if feld[ein][0] != " . ":
        print("Feld belegt. Bitte anderen Spielzug wählen.")
        eingabe()
    else:
        spielzug(ein)

draw()
eingabe()