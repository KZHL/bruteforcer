import keyboard
import time

with open("listdemots.txt", "r", encoding="utf-8") as fichier:
    v = fichier.read()

mots = []
mot = ""

for lettre in v:
    if lettre == "\n":
        mots.append(mot)
        mot = ""
    else:
        mot = mot + lettre
if mot != "":
    mots.append(mot)

time.sleep(1)

for mot in mots:
    keyboard.write(mot)
    keyboard.press('enter')
    keyboard.release('enter')
    time.sleep(15)
