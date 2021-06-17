from Konto import Konto

class Sparkonto (Konto):

    def __init__(self, kontoNr, kontoStand=None):
        self.__guthabenZins = 1.5
        Konto.__init__(self, kontoNr, kontoStand)

    def abheben(self,betrag):
        if(self._kontoStand - betrag >=0):
            self._kontoStand -= betrag
        else:
            pass

    def berechneKontofuehrungsgebuehr(self):
        if(self._kontoStand<10000):
            return 10
        else:
            return 5