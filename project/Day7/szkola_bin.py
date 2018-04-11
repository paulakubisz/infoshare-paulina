import pickle
from pprint import pprint
#
# szkola = {
#     1: {'imie': 'Adam', "nazwisko": 'Kowalski', 'uwagi': ['brak']},
#     2: {'imie': 'Jas', "nazwisko": 'Nowak', 'uwagi': ['podpalal sciane zapalkami',
#                                                       'pobil kolege na przerwie']},
# }
#
#
# with open('szkola.gda', 'wb') as plik:
#     pickle.dump(szkola, plik)

szkola_2 = None

with open('szkola.gda', 'rb') as plik:
    szkola_2 = pickle.load(plik, encoding='utf-8')

pprint(szkola_2, indent=4)