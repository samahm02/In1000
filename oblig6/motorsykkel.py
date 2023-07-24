"""
her lager jeg en kasse motorsykkel, som har metodene kjor,hentKilometerstand og skrivut.
denne filen bruker jeg videre i testMotorsykkel.py
"""

class motorsykkel: #lager klassen mottorsykkel
    def __init__(self,merke,regNr,kmStand): #lager konstruktøren med merke,regnr og kmstand
        self._merke=merke
        self._regNr=regNr
        self._kmStand=kmStand


    def kjor(self,kmstand): #lager metoden som setter kmstanden
        self._kmStand+=km

    def hentKilometerstand(self): ##lager metoden som setter returnerer kmstanden
        return self._kmStand


    def skrivUt(self): #laget metoden som skriver ut merke, regnummeret og kmstaden
        print("Merke:", self._merke)
        print("Registreringsnummer:", self._regNr)
        print("Kilometerstand:", self._kmStand)
