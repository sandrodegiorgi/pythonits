class Inhaber:

    def __init__(self, name, einKonto):
        # Kapselung durch Unterstriche
        self.__name = name
        #Ein Kunde, viele Konten (aber mindestens eins)
        self.__seineKonten = [einKonto]

    def fuegeKontoHinzu(self, einKonto):
        self.__seineKonten += [einKonto]


    def berechneGesamtStand(self):
        summe = 0
        for x in self.__seineKonten:
           summe += x.getKontostand()
        return summe

    def berechneGesamtGebuehr(self):
        summe = 0
        for x in self.__seineKonten:
            summe += x.berechneKontofuehrungsgebuehr()
        return summe

    def getName(self):
        return self.__name




