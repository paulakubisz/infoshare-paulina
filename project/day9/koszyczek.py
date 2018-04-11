from pisanka import Pisanka

jajeczko = Pisanka('czerwony')
print(jajeczko.color)


jajeczko2 = Pisanka("niebieska")
print(jajeczko2.color)

print(jajeczko.typ)

jajeczko.typ = 'kurze'
print(jajeczko.typ)

jajeczko2.typ = 'przepiórcze'
jajeczko2.color = "szare"

print(jajeczko2.color)

#przefarbowanie jaja
jajeczko2.przefarbuj()
print(jajeczko2.color)