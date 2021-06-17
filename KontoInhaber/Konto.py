from abc import ABC, abstractmethod


class Konto (ABC):

    #hier wäre Platz für Klassenvariablen

    def __init__(self, kontoNr, kontoStand = None):

        self._Nr = kontoNr
        #Überladung von Methoden simuliert durch Abfrage von default-Parametern
        if(kontoStand != None):
            self._kontoStand = kontoStand
        else:
            self._kontoStand =0


    def einzahlen(self, betrag):
        self._kontoStand += betrag

    @abstractmethod
    def abheben(self,betrag):
        pass

    @abstractmethod
    def berechneKontofuehrungsgebuehr(self):
        pass

    def getKontostand(self):
        return self._kontoStand

    def getKontoNr(self):
        return self._Nr

    def setInhaber(self, derInhaber):
        self._seinInhaber = derInhaber

    def getInhaber(self):
        return self._seinInhaber