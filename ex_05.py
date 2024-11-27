def custom_sort(liste):
    if type(liste)!=list:
        raise ValueError("Cette fonction prend en paramètre une liste")
    return sorted(liste, key=lambda x: (len(x), x))