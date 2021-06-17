# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from Girokonto import Girokonto
from Inhaber import Inhaber
from Sparkonto import Sparkonto



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    erstesKonto = Girokonto(499, 500, 1000)
    ersterInhaber = Inhaber("Helga",erstesKonto)
    erstesKonto.setInhaber(ersterInhaber)
    print(erstesKonto.getInhaber().getName())

    naechstesKonto = Girokonto(500, 100, 319)
    print(naechstesKonto.getKontoNr())
    print(naechstesKonto.getKontostand())
    naechstesKonto.einzahlen(100)
    print(naechstesKonto.getKontostand())
    naechstesKonto.abheben(150)
    print(naechstesKonto.getKontostand())

    anderesKonto = Sparkonto(501)
    print(anderesKonto.getKontostand())
    anderesKonto.einzahlen(100)

    einKunde = Inhaber("Bruno", anderesKonto)
    einKunde.fuegeKontoHinzu(naechstesKonto)
    print(einKunde.berechneGesamtStand())
    print(einKunde.berechneGesamtGebuehr())
