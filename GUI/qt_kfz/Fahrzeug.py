import math

# Fachklasse
class Fahrzeug:
    def __init__(self):
        self.typ = ""
        self.hubraum = 0.0
        self.co2 = 0.0
        self.is_diesel = True

    def berechne_steuer(self):
        """Berechne die Kfz-Steuer"""
        hubraumsteuer = 0.0
        co2_steuer = 0.0
        steuer = 0.0
        if self.is_diesel:
            hubraumsteuer = 9.5 * math.ceil(self.hubraum / 100)
        else:
            hubraumsteuer = 2.0 * math.ceil(self.hubraum / 100)
        co2_steuer = max(self.co2 - 95,0) * 2
        steuer = hubraumsteuer + co2_steuer
        return steuer