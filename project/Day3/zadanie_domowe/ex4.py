# 4. oblicz ocenę na podstawie progu procentowego

zdobyte_punkty = int(input("Ile zdobyłeś procet: "))
if zdobyte_punkty > 95 and zdobyte_punkty <= 100:
    print("Gratulacje! Twoja ocena to celujący!")

elif zdobyte_punkty > 86 and zdobyte_punkty < 96:
    print("Gratulacje! Twoja ocena to bardzo dobry!")

elif zdobyte_punkty > 69 and zdobyte_punkty < 86:
    print("Gratulacje! Twoja ocena to  dobry!")

elif zdobyte_punkty > 51 and zdobyte_punkty < 70:
    print("Twoja ocena to dostateczny!")

elif zdobyte_punkty > 50 and zdobyte_punkty < 36:
    print("Twoja ocena to dopuszczajacy!")

elif zdobyte_punkty < 37:
    print("Słabo! Twoja ocena to niedostateczny")

else:
    print("Wprowadziles niepoprawną wartość!")