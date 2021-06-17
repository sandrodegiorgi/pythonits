from abc import ABC, abstractmethod

class Konto(ABC):
    ''' abstract Class Konto
        Cute class representing an account, with a bank maybe...'''

    __naechsteNummer = 1001  # statische Variable

    def __init__(self, name="", ersteinzahlung=0):
        self.__kontoNummer = Konto.__naechsteNummer  # Attribute werden im Konstruktor initialisiert!
        Konto.__naechsteNummer += 1
        self.__inhaber = name
        self.__kontoStand = ersteinzahlung

    @abstractmethod
    def berechneZinsen(self):
        pass

    # nicht alle Methoden müssen hier abstract sein!
    def __str__(self):
        return "Kontonummer: " + str(self.__kontoNummer) + "\n" + \
            "Inhaber: " + self.__inhaber + "\n" + \
            "Kontostand: " + str(self.__kontoStand) + "\n" + \
            "Object-Type: " + str(self.__class__) + "\n" + \
            "\n-------------------\n"
