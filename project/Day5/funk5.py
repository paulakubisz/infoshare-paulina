#

imie = "ola"

def drukuj_imie(imie1= "anna"):
    global imie
    imie = imie.capitalize()
    return imie


print(drukuj_imie())