# list comprehension

liczby = []

for i in range(21):
    liczby.append(i)

print(liczby)


numerki = [x for x in range(21)]
print(numerki)

#######################



liczby_3 = []

for i in range(20):
    liczby_3.append(i**3)
print(liczby_3)


numerki_3 = [x**3 for x in range(20)]
print(numerki_3)


########################


liczby_4 = []

for x in range(101):
    if x**2 % 3 == 0:
        liczby_4.append(x**2)

print(liczby_4)


numerki_4 = (x**2 for x in range(101) if x ** 2 % 3 == 0)
print(numerki_4)





