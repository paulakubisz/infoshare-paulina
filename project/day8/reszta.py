monety = {5:0, 2:0, 1:0, 0.5:0, 0.2:0, 0.1:0}

zakupy = 13.30
banknot = 20.00

reszta = banknot - zakupy

print(f'Do wydania: {reszta:.2f}')

for moneta in monety:
    if reszta >= moneta:
        il_monet = int(reszta // moneta)
        monety[moneta] = il_monet
        reszta -= moneta * il_monet
        #print(f'reszta po monecie {moneta}: {reszta}')

wydano = 0

for moneta, ilosc in monety.items():
    wart_monety = moneta * ilosc
    print(f'moneta: {moneta:<4} - ilosc: {ilosc:>2} - wartość: {wart_monety:>5.2f}')
    wydano += wart_monety

print(f"RAZEM {wydano:>35.2f}")
