from datetime import *
import pyttsx3
from micro import *
from calcul import *
from musique import *

ESCAPE = "\x1b"
BLACK = "[30m"
WHITE = "[0m"
BLUE = "[34m"
RED = "[31m"

# paramètre parler
engine = pyttsx3.init("sapi5")
engine.setProperty("vitesse", 178)
engine.setProperty("volume", 0.7)
# paramètre écouter
initialise_micro()


prenom = "Nanali"


def parler(parole):
    print(ESCAPE + BLUE + parole)
    engine.say(parole)
    engine.runAndWait()


def temps(type):
    if type == "heure":
        date = datetime.today().strftime('%H:%M')
        parler("Il est " + date)
    if type == "date":
        date = datetime.today().strftime('%d/%m/%Y')
        parler("La date du jour est " + date)
    if type == "jour":
        date = datetime.today().strftime('%A')
        jour = {"Monday": "Lundi", "Tuesday": "Mardi", "Wednesday": "Mercredi", "Thursday": "Jeudi",
                "Friday": "Vendredi", "Saturday": "Samedi", "Sunday": "Dimanche"}
        date = jour[date]
        parler("On est " + date)


debut = 1
pause = 0
running = 1
while running == 1:
    try:
        r = ecouter()

        if not r == "":
            print(ESCAPE + WHITE + r)
        else:
            print(ESCAPE + BLUE + "None")

        if not pause == 1:

            if debut == 1:

                parler("Bonjour je m'appelle " + prenom + " que puis je faire pour vous ?  ")
                debut = 0

            elif "Salut" in r or "salut" in r:
                parler("salut")

            elif "anniversaire" in r or "Anniversaire" in r:

                if "Aubin" in r or "" in r:
                    parler("Votre anniversaire est le 3 juillet")

                elif "Flora" in r or "sœur" in r:
                    parler("L'anniversaire est le 23 mai")

            elif "étein" in r:
                parler("ok")
                pause = 1

            elif " + " in r or " - " in r or " / " in r or " x " in r:
                resultat_calcul = calculer(r)
                parler(resultat_calcul[0]+" = "+str(resultat_calcul[1]))

            elif "bête" in r or "connais rien" in r or "comprends rien" in r:
                parler("c'est vous qui m'avez programmé")

            elif "heure" in r:
                temps("heure")

            elif "date" in r:
                temps("date")

            elif " jour " in r or " jours " in r:
                temps("jour")

            elif "musique" in r and "mets" in r:
                parler("ok")
                jouer_musique("musique_aléatoire")

            elif "arrête" in r or "stop" in r or "tais-toi" in r:
                arreter()
                parler("j'arrête la musique")

            elif r == prenom:
                parler("oui c'est moi")

            elif "merci" in r:
                parler("de rien")

            else:
                print(ESCAPE + BLUE + "mot inconnu")
        else:
            if "allume" in r:
                parler("ok")
                pause = 0
    except:
        running = 1
