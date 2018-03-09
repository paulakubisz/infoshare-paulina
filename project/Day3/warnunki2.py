wyraz = input("Podaj jakis wyraz: ")
#print(type(wyraz)) - wskazuje jaki typ, zwracamy zawsze string

if "a" in wyraz:
    print(f"W wyrazie '{wyraz}' jest literka 'a'")
elif "A" in wyraz:
    print(f"Natomiast w wyrazie {wyraz} jest literka 'A'")
else:
    print(f"W wyrazie {wyraz} nie ma literki 'a'")