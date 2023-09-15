import sys
from parler import *
from datetime import *
import time


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
    process_parler("fin du chrono")



def temps(t):
    if t == "heure":
        d = datetime.today().strftime('%H:%M')
        process_parler("Il est " + d)
    if t == "date":
        d = datetime.today().strftime('%d/%m/%Y')
        process_parler("La date du jour est " + d)
    if t == "jour":
        d = datetime.today().strftime('%A')
        jour = {"Monday": "Lundi", "Tuesday": "Mardi", "Wednesday": "Mercredi", "Thursday": "Jeudi",
                "Friday": "Vendredi", "Saturday": "Samedi", "Sunday": "Dimanche"}
        d = jour[d]
        process_parler("On est " + d)