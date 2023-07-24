"""
lager klassen hund med matodene hentAlder,hentVekt,spring og spis.
videre bruker jeg denne klassen i testHund.py
"""

class hund: #lager klassen hund
    def __init__(self,alder,vekt): #lager konstruktøren med alder og vekt
        self._alder=alder
        self._vekt=vekt
        self._metthet=10


    def hentAlder(self): #lager metoden som returnerer alder
        return self._alder

    def hentVekt(self): #lager metoden som returnerer vekt
        return self._vekt

    def spring(self): #lager metoden som minker mettheten med 1 og minker vekten om mettheten er under 5
        print("spring")
        self._metthet-=1
        if self._metthet <5:
            self._vekt-=1

    def spis(self,tall): #lager metoden som øker mettheten med og øker vekten om mettheten er over 7
        print("spis")
        self._metthet+=tall
        if self._metthet >7:
            self._vekt+=1
