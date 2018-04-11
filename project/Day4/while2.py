#

wejscie = input("Podaj mi liczbę: ")

while not wejscie.isdigit():
    print('Tylko cyfry!')
    wejscie = input("Podaj liczbę: ")

print(int(wejscie)** 2) # zamiana liczby do kwadratu

#DRUGI SPOSOB

# for cos in wejscie:
#     if not cos.isdigit():
#         break
#
# print(int(wejscie) ** 2)  # zamiana liczby do kwadratu

