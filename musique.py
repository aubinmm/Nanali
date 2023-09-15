from pygame import mixer
import random


def jouer_musique(nom):

    # Initialisation du mixer :
    mixer.init()
    # chargement des musiques
    aleatoire = random.randint(1, 6)
    if nom == "musique_aléatoire":
        mixer.music.load('musique'+str(aleatoire)+'.mp3')

    elif nom == "suivante":
        mixer.music.load('musique'+str(aleatoire+1)+'.mp3')
    else:
        mixer.music.load(str(nom)+'.mp3')

    # Lecture :
    mixer.music.play()


def arreter():
    # Stop :
    mixer.music.stop()
