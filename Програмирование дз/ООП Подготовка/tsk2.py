def decorate(recepie):
    def ananass():
        recepie.append("Ананас")
    def salatlist():
        recepie.append("Салат")

@decorate
def recepie(n, lambda: ):
    recepie = "Хлеб\nКотлета\nБекон\nПомидор\nОгурец"
    return recepie

recepie(decorate(recepie))