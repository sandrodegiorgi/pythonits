from Konto import Konto

class GiroKonto(Konto):
    """ Class GiroKonto
        even cuter class for giro! """
    # def __init__(self, **kwargs):
    # super().__init__(kwargs)
    def __init__(self, name="", ersteinzahlung=0, credit=0):
        super().__init__(name, ersteinzahlung)
        self.__credit = credit

    def gk_method(self):
        print ("i am a gk method!")
