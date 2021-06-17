from Konto import Konto

class Girokonto (Konto):

    def __init__(self, kontoNr, limit, kontoStand=None):
        self.__kreditZins = 10
        self.__limit = limit
        Konto.__init__(self, kontoNr, kontoStand)

    def abheben(self,betrag):
        if(self._kontoStand - betrag + self.__limit >=0):
            self._kontoStand -= betrag
        else:
            pass

    def berechneKontofuehrungsgebuehr(self):
        return self.__limit * 0.01


