class Pies(object):

    def __init__(self):
        self.rasa = "Brak danych"
        self.plec = 'Brak danych'
        self.masc = "szarybury"

    def daj_glos(self):
        self.szczekac = True
        return

    def siad(self):
        self.siadac = True
        return

class Kot(Pies):

    def __init__(self):
        super().__init__()