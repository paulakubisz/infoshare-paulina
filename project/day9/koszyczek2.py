from pisanka import Pisanka

koszyk = []


jajo1 = Pisanka('czerwony')
jajo2 = Pisanka("kraszona czarno-fioletowa")

jajo1.zjedz(20)
# print(jajo1.zostalo)

koszyk.append(jajo1)
koszyk.append(jajo2)

print(koszyk)

# for jajo in koszyk:
#     print(jajo.zostalo)
#     print(jajo.color)
#     jajo.przefarbuj()
#     print(jajo.color)

print(jajo1)
print(jajo2)