class Konto(object):
    ''' Class Konto
        Cute class representing an account, with a bank maybe...'''

    __naechsteNummer = 1001  # statische Variable

    def __init__(self, name="", ersteinzahlung=0):
        self.__kontoNummer = Konto.__naechsteNummer  # Attribute werden im "Konstruktor" initialisiert!
        Konto.__naechsteNummer += 1
        self.__inhaber = name
        self.__kontoStand = ersteinzahlung

    @classmethod
    def fromname(cls, name):
        return cls(name=name)

    @classmethod
    def fromnamemitersteinzahlung(cls, name, ersteinzahlung):
        return cls(name=name, ersteinzahlung=ersteinzahlung)

    @property
    def inhaber(self):
        return self.__inhaber

    @inhaber.setter
    def inhaber(self, name):
        self.__inhaber = name

    @inhaber.deleter
    def inhaber(self):
        self.__inhaber = None

    def einzahlen(self, betrag):
        if betrag > 0:
            self.__kontoStand = self.__kontoStand + betrag

    def abheben(self, betrag):
        if betrag > 0 and self.__kontoStand - betrag >= 0:
            self.__kontoStand = self.__kontoStand - betrag

    def getNaechsteNummer():
        return Konto.__naechsteNummer

    def __str__(self):
        return "Kontonummer: " + str(self.__kontoNummer) + "\n" + \
            "Inhaber: " + self.__inhaber + "\n" + \
            "Kontostand: " + str(self.__kontoStand) + "\n" + \
            "Object-Type: " + str(self.__class__) + "\n" + \
            "\n-------------------\n"

    # well... :)
    def getKontoNummer(self):
        return self.__kontoNummer

    def setInhaber(self, inhaber):
        if inhaber != "":
            self.inhaber = inhaber

    def getInhaber(self):
        return self.inhaber

    def getKontoStand(self):
        return self.__kontoStand

