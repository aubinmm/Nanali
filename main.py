from datetime import *
import time
import pyttsx3
from micro import *
from calcul import *
from musique import *
import wikipedia
import sys


ESCAPE = "\x1b"
BLACK = "[30m"
WHITE = "[0m"
BLUE = "[34m"
GREEN = "[32m"
RED = "[31m"

# paramètre parler
engine = pyttsx3.init("sapi5")
engine.setProperty("vitesse", 178)
engine.setProperty("volume", 0.7)
# paramètre écouter
initialise_micro()

prenom = "Nanali"

liste_micro()


def parler(parole):
    print(ESCAPE + GREEN + parole)
    engine.say(parole)
    engine.runAndWait()


def chrono(temps_secs):
    while temps_secs:
        mins, secs = divmod(temps_secs, 60)
        temps_format = '{:02}:{:02}'.format(mins, secs)
        sys.stdout.write(temps_format)  # affiche temps
        sys.stdout.flush()  # raffraichi l'écran
        time.sleep(1)
        temps_secs -= 1
        sys.stdout.write(chr(13))
        sys.stdout.write('' * len(temps_format))
        sys.stdout.write(chr(13))
    parler("fin du chrono")


def temps(t):
    if t == "heure":
        d = datetime.today().strftime('%H:%M')
        parler("Il est " + d)
    if t == "date":
        d = datetime.today().strftime('%d/%m/%Y')
        parler("La date du jour est " + d)
    if t == "jour":
        d = datetime.today().strftime('%A')
        jour = {"Monday": "Lundi", "Tuesday": "Mardi", "Wednesday": "Mercredi", "Thursday": "Jeudi",
                "Friday": "Vendredi", "Saturday": "Samedi", "Sunday": "Dimanche"}
        d = jour[d]
        parler("On est " + d)


debut = 1
pause = 0
musique = 0
running = 1

parler("Bonjour je m'appelle " + prenom + " que puis je faire pour vous ?")

while running == 1:
    try:
        r = ecouter()

        if not r == "":
            print(ESCAPE + WHITE + r)
        else:
            print("")

        if not pause == 1:

            if debut == 1 and prenom in r:

                parler("Bonjour je m'appelle " + prenom + " que puis je faire pour vous ?  ")
                debut = 0

            elif "Bonjour" in r:
                parler("Bonjour")
                temps("heure")

            elif "Salut" in r or "salut" in r:
                parler("Salut")
                temps("heure")

            elif "bonne nuit" in r:
                parler("Bonne nuit voici un peu de musique ")
                jouer_musique("piano")

            elif "anniversaire" in r or "Anniversaire" in r:

                if "Aubin" in r or "" in r:
                    parler("Votre anniversaire est le 3 juillet")

                elif "Flora" in r or "sœur" in r:
                    parler("L'anniversaire de Flora est le 23 mai")
            elif "chrono" in r or "minuteur" in r:
                parler("De combien de secondes ?")
                r = ecouter()
                print(ESCAPE + WHITE + r)
                parler("je mets un chrono de "+r+" secondes")
                chrono(abs(int(r)))

            elif "étein" in r:
                parler("ok")
                pause = 1

            elif " + " in r or " - " in r or " / " in r or " x " in r:
                resultat_calcul = calculer(r)
                parler(resultat_calcul[0] + " = " + str(resultat_calcul[1]))

            elif "bête" in r or "connais rien" in r or "comprends rien" in r:
                parler("c'est vous qui m'avez programmé")

            elif "heure" in r:
                temps("heure")

            elif "date" in r:
                temps("date")

            elif "jour" in r or "jours" in r and not"journal" in r:
                temps("jour")

            elif "musique" in r and "mets" in r:
                musique = 1
                parler("je mets de la musique")
                jouer_musique("musique_aléatoire")

            elif "arrête" in r or "stop" in r or "tais-toi" in r:
                musique = 0
                arreter()
                parler("j'arrête la musique")

            elif "musique" in r and "suivante" in r and musique == 1:
                parler("musique suivante")
                jouer_musique("suivante")

            elif r == prenom:
                parler("oui c'est moi")

            elif "merci" in r:
                parler("de rien")

            else:
                wikipedia.set_lang("fr")
                try:
                    parler(wikipedia.summary(r))
                except:
                    print(ESCAPE + RED + "mot inconnu")
        else:
            if "allume" in r:
                parler("ok")
                pause = 0
    except:
        running = 1
