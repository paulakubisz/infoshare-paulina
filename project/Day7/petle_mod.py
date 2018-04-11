for x in range(20):
    if x**2 > 280:
        print("Znalazlem:", x)
        break

print('Koniec - break')


for x in range(100):
    if x % 7 == 0:
        continue
        print('znalazlem continue')
    else:
        print(x)

print("Koniec - continue")


#for - else

for x in range(10):
    if x**2 > 100:
        print(f'KWadrat {x} jest wiekszy od 100')
        break
else:
    print("Zaden kwadrat nie jest wiekszy od 100")