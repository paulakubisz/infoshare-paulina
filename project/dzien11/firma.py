from pprint import pprint

from dzien11.pracownik import Pracownik

p1 = Pracownik('John Travolta', 3000, 'gwiazda wyblakła')
p2 = Pracownik('John Turturo', 1500, 'stara gwiazda')
p3 = Pracownik('John Rambo', 5000, 'killer')

# pprint(p1.__dict__, indent=4)

print(p1.dzien_podatkowy)
print(p2.dzien_podatkowy)
print(p3.dzien_podatkowy)

p1.dzien_podatkowy = '20.05.2018'
Pracownik.dzien_podatkowy = '25.04.2018'
# pprint(p1.__dict__, indent=4)
print('---------------')
print(p1.dzien_podatkowy)
print(p2.dzien_podatkowy)
print(p3.dzien_podatkowy)

del p1.dzien_podatkowy
print('--------------')
print(p1.dzien_podatkowy)
print(p2.dzien_podatkowy)
print(p3.dzien_podatkowy)
