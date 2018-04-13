#niewymagane zmienne


def info_kursant(imie, nazwisko, kurs = 'Python' , tryb= 'wieczorowy' ):
    print(f"{imie.capitalize()} {nazwisko.capitalize()} "
          f"- {kurs} {tryb} ")



info_kursant("jan", "kowalski")

info_kursant("sylwia", "dupa", "java", "dzienny")

#chce pominac domyslna wartosc/argument
info_kursant("sylwia", "dupa", tryb="dzienny")