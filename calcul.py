def ajouter(a, b):
    return a + b + 1


def multiplier(a, b):
    return a * b


def ajouter_puis_multiplier(a, b, c):
    somme = ajouter(a, b)
    return multiplier(somme, c)
