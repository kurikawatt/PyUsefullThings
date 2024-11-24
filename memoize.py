#coding: utf-8

def memoize(function):
    """
    Ce décorateur permet d'utiliser la mémoization dans
    une fonction récursive
    """
    # Le bout de code pour la rendre mémoizable
    def memoized_function(*args):
        if args in memory:
            return memory[args]
        res = function(*args)
        memory[args] = res
        return res
    # Création de la mémoire
    memory = {}
    # On renvoit la fonction mémoizée
    return memoized_function