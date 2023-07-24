"""
lager classen dato med metodene lesAar,hentDato og sjekkDag.
videre bruker jeg denne klassen i testDato.py

"""


class dato: #lager klassen dato
    def __init__(self,Dag,Maaned,Aar): #lager konstruktøren med dag,maaned og aar
        self._nyDag=Dag
        self._nyMaaned=Maaned
        self._nyttAar=Aar

    def lesAar(self): #lager metoden lesaar som returenerer år
        return self._nyttAar

    def hentDato(self): #lager metoden hent dato som gjjør den til en string og returerer den
        self._dato = str(self._nyDag) + "." + str(self._nyMaaned) + "." + str(self._nyttAar)
        return self._dato

    def sjekkDag(self): #lager metoden sjekkDag som ser om det er 1 eller 15
        if self._nyDag == 1:
            print("Ny måned, nye muligheter!")
        elif self._nyDag == 15:
            print("Lønningsdag!:D")
