# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

#różnoboczny a =! b =! c
#równoramienny a = a != c
#równoboczny  a = a = a

a = int(input("Długość nahdłuższego boku trójkąta: "))
b = int(input("Długość drugiego boku trójkąta: "))
c = int(input("Długość trzeciego boku trójkąta: "))

if a != b and  a != c and b != c:
    print("To jest trójkąt różnoboczny!")

elif b == c and a > b or a > c:
    print("To jest trójkąt równoramienny!")

elif a == b and b == c and a == c:
    print("To jest trójkąt równoboczny!")

if a < (b * c):
    print("Tak, jest możliwość narysowania tego trójkąta!")

else:
    print("Nie jest możliwe narysowanie tego trójkąta!")