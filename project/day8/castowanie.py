# type casting
# czyli zamiana typu na inny typ
liczba = input("Podaj liczbę: ")

try:
    liczba = int(liczba)

except ValueError:
    print("Podałęś nieprawidłowe znaki. Wprowadź tylko cyfry.!")


finally:
    if type(liczba) == str:
        print("Nie podales prawidłowej wartośc")

    else:
        kwadrat = liczba * liczba
        print(f'Kwadrat liczby {liczba} wynosi: {kwadrat}')


def dodaj (a, b):
    if type(a) != input():
            raise ValueError('Nieprawidlowy tyn mienniej a!')
    return  a + b