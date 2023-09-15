from speech_recognition import Recognizer, Microphone

from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('ueoTvA-yfIOwIuTcqqHWLVPLAz3nMAWJpIxJwdlatdCP')
speech_to_text = SpeechToTextV1(authenticator=authenticator)
speech_to_text.set_service_url('https://api.eu-de.speech-to-text.watson.cloud.ibm.com')





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
    print("j'écoute")
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


def ecouter_ibm():
    with Microphone() as source:
        recorded_audio = recognizer.listen(source, timeout=None)
    try:
        rec = speech_to_text.recognize(audio=recorded_audio, content_type="audio/basic", model="fr-FR_Multimedia")
        res = rec.get_result()
        text = res["results"][0]["alternatives"][0]["transcript"]

    except Exception as ex:
        print(ex)
        print(ESCAPE + RED + "None")