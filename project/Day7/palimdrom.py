import odwracacz




def czy_palimdrom(slowo: str) -> bool:
    """
    Sprawdź czy słowo jest palindromem


    :param slowo: jakieś słowo
    :return:
    """

    odwrocone = odwracacz.odwroc(slowo)
    if slowo == odwrocone:
        return True

    else:
        return False

def main():
    print(czy_palimdrom("kajak"))
    print(czy_palimdrom("oal"))

if __name__ == '__main__':
    main()

# print(czy_palimdrom('kajak'))
# print(czy_palimdrom('oal'))

