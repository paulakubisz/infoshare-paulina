with open('osoby.txt', 'r+', encoding="utf-8" ) as plik:
    do_zapisania = "To jest nowa linijka\n"

    plik.readline()
    koniec = plik.tell()

    plik.seek(koniec -1)

    ostatni_znak = plik.readline(1)

    if ostatni_znak == "\n":
        plik.write(do_zapisania)

    else:
        plik.write('\n' + do_zapisania)