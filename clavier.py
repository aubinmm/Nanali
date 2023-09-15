import keyboard

def interrompre_programme(ret_value):
    keyboard.wait("esc")
    print("fin du programme")
    ret_value.value = False

