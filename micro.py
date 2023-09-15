from speech_recognition import Recognizer, Microphone



recognizer = Recognizer()

ESCAPE = "\x1b"
BLACK = "[30m"
WHITE = "[0m"
BLUE = "[34m"
GREEN = "[32m"
RED = "[31m"

# On enregistre le son

def liste_micro():
    for index, name in enumerate(Microphone.list_microphone_names()):
        print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

def initialise_micro():
    with Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)


def ecouter():
    with Microphone() as source:
        recorded_audio = recognizer.listen(source, timeout=None)
    try:
        text = recognizer.recognize_google(
            recorded_audio,
            language="fr-FR"
        )
        return(format(text))

    except Exception as ex:
        print(ex)
        print(ESCAPE + RED + "None")


