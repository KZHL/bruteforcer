import keyboard
import time

# Ouvrir le fichier de la wordlist
with open("listdemots.txt", "r", encoding="utf-8") as fichier:
    # Lire le contenu du fichier et stocker dans la variable v
    v = fichier.read()

# Diviser la wordlist en une liste de mots
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

# Attendre quelques secondes pour donner le temps de se concentrer sur la fenêtre où la frappe sera effectuée
time.sleep(1)

# Boucler à travers chaque mot et simuler la frappe

for mot in mots:
    keyboard.write(mot)    
    # Simuler la pression de la touche "Enter"
    keyboard.press('enter')
    keyboard.release('enter')
    # Ajouter une pause entre chaque mot (ajustez si nécessaire)
    time.sleep(15)
