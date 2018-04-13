#funkcja z wymaganymi argumentami 
def pole_trojkata(podstawa, wysokosc):
    '''
    Oblicza i zwraca pole trojkata
    :param podstawa: int
    :param wysokosc: int
    :return: float
    '''
    pole = podstawa * wysokosc / 2
    return pole


a = pole_trojkata(23,34)
print(a)

print(pole_trojkata(33,45))