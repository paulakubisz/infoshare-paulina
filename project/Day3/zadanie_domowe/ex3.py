# 3a. czy liczba jest podzielna przez 3 lub 5 lub 7
# 3b. czy liczba jes podzielne przez 3 i 5 i 7

liczba = int(input("Wprowadź swoją ulubioną liczbę: "))

if liczba % 3 == 0:
    print(f"Twoja liczba jest podzielna przez 3.")

elif liczba % 5 == 0:
    print(f"Twoja liczba jest podzielna przez 5.")

elif liczba % 7 == 0:
    print(f"Twoja liczba jest podzielna przez 7.")

else:
    print(f"Twoja {liczba} nie jest podzielna!")

liczba_new = int(input("Wprowadź swoją ulubioną liczbę: "))

if liczba_new % 3 == 0 and liczba % 5 == 0 and liczba % 7 == 0:
    print(f"Twoja {liczba_new} jest podzielna przez 3, 5 i 7.")
else:
    print(f"Twoja {liczba_new} nie jest podzielna!")
