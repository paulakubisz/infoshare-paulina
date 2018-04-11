"""
Moduł zawiera funkcjonalność odwracania stringów

"""


def odwroc(zdanie: str) -> str:
    """
    Zwraca odwrócone podane zdanie.

    :param zdanie: jakieś zdanie
    :return: Odwrócone zdanie
    """

    zdanie = zdanie [::-1]
    return zdanie


def main():
    zdanie = 'Kajaczek'
    zdanie_odwrocone = 'kezcajaK'

    odwrocone = odwroc(zdanie)

    if zdanie_odwrocone == odwrocone:
        print("Działa")

    else:
        print("Nie działa")

if __name__ == '__main__':
    main()
