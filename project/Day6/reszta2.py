monety = {5: 0, 2:0 , 1:0, 0.5: 0, 0.2: 0, 0.1: 0}

zakupy = 17.40
banknot = 20.00

reszta = banknot -  zakupy

for moneta in monety:
    if reszta >= moneta:
        il_monet = reszta // moneta
        monety[moneta] = il_monet
        reszta -= moneta * il_monet

for moneta, ilosc in monety.items():
    print(f'moneta: {moneta} - ilosc- {ilosc}')
