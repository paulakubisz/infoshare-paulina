class Piec(object):

    def __init__(self, marka, moc, typ):
        self.marka = marka
        self.moc = moc
        self.typ = typ

    def __str__(self):
        return f'Piec {self.marka}, {self.typ} ' \
               f'o mocy {self.moc} kwh'


def main():
    piecyk = Piec('Bosch', 120, 'gazowy')
    print(piecyk)

if __name__ == '__main__':
    main()