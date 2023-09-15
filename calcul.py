import re


def calculer(r="je ne sais pas"):
    # extraire le calcul de la chaîne de caractère et mémorisation dans la variable : calcul_demande
    resultat = None
    r = r.replace("x", "*")
    regex = re.compile("([0-9]+\.?[0-9]*)( [\*\/\+\-] [0-9]+\.?[0-9]*)+")
    calcul_demande = regex.search(r).group(0)

    while " + " in r or " - " in r or " / " in r or " * " in r:
        if " * " in r and resultat is None:
            if r.find("/") == -1 or r.find("*") < r.find("/"):
                regex = re.compile("([0-9]+\.?[0-9]*) \* ([0-9]+\.?[0-9]*)")
                resultat = float(regex.search(r).group(1)) * float(regex.search(r).group(2))
        if " / " in r and resultat is None:
            if r.find("*") == -1 or r.find("/") < r.find("*"):
                regex = re.compile("([0-9]+\.?[0-9]*) \/ ([0-9]+\.?[0-9]*)")
                resultat = float(regex.search(r).group(1)) / float(regex.search(r).group(2))
        if " + " in r and resultat is None:
            if r.find("-") == -1 or r.find("+") < r.find("-"):
                regex = re.compile("([0-9]+\.?[0-9]*) \+ ([0-9]+\.?[0-9]*)")
                resultat = float(regex.search(r).group(1)) + float(regex.search(r).group(2))
        if " - " in r and resultat is None:
            if r.find("+") == -1 or r.find("-") < r.find("+"):
                regex = re.compile("([0-9]+\.?[0-9]*) \- ([0-9]+\.?[0-9]*)")
                resultat = float(regex.search(r).group(1)) - float(regex.search(r).group(2))
        r = r.replace(regex.search(r).group(0), str(resultat), 1)
        resultat_final = resultat
        resultat = None
        print(r)

    return calcul_demande, resultat_final
