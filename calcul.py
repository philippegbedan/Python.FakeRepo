def ajouter(a, b):
    return a + b


def multiplier(a, b):
    return a * b


# Fonction soustraire
def soustraire(a, b):
    return a - b


def ajouter_puis_multiplier(a, b, c):
    somme = ajouter(a, b)
    return multiplier(somme, c)
