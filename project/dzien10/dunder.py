from dzien10.dom import Dom, DomLetniskowy
from piec import Piec

domek = Dom(80, 'Żukowo', 250000)
pol_blizniaka = Dom(120, 'Suchanino', 380000)
# print(domek)
# print(pol_blizniaka)
# print(domek.oddany)
# print(pol_blizniaka.oddany)
# domek.oddaj_do_uzytku()
# print(domek)
# print(domek.oddany)
# print('---------')
# print(f'sprawdzam domek > blizniak')
# print(domek > pol_blizniaka)
# print(domek.cena + pol_blizniaka.cena)
# print(domek + pol_blizniaka)
# wartosc, pow_calkowita = domek + pol_blizniaka
# print(f'Wartość zasobu mieszkalnego {wartosc}')
# print(f'Powierzchnia zasobu: {pow_calkowita}')

print(domek.piecyk)
domek.piecyk = Piec('AEG', 200, 'miał')
print(domek.piecyk)

domek.piecyk.moc = 210

print(domek.piecyk)

let1 = DomLetniskowy(45, 'Wdzydze', False)
print(let1)


