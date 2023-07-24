"""
er lager jeg en kassen Sang, som har metodene spill, sjekkArtist, sjekkTittel og sjekkArtistOgTittel.

"""
class Sang:
    def __init__(self, artist, tittel): #lager konstruktøren med artist og tittel
        self._artist=artist
        self._tittel=tittel

    def spill(self): #lager metoden spill
        print("spiller av:") #printer ut sang tittel og artist(ene)
        print(self._tittel,"av",self._artist)

    def sjekkArtist(self,navn): #lager metoden sjekkArtist medn parameteren navn
        navn=navn.lower() #gjør det om til små bokstaver og spilter
        navn=navn.split()
        self._artist= self._artist.lower() #gjør om artisten til små bokstaver
        for x in navn: #går gjennom listen navn
            if x in self._artist: #ser om artisten er i listen
                return True #hvis artisten er i listen så blir True returnert
        else:
            return False #hvis ikke så blir False returnert

    def sjekkTittel(self,tittel): #lager metoden sjekkTittel medn parameteren tittel
        tittel=tittel.lower() #gjør det om til små bokstaver
        self._tittel=self._tittel.lower() #gjør det også om til små bokstaver
        if tittel ==self._tittel: #ser om de er like
            return True #hvis likes så blir True returnert
        else:
            return False #hvis ikke så blir false returnert

    def sjekkArtistOgTittel(self,artist,tittel): #lager metoden sjekkArtistOgTittel medn parameterene artist og tittel
        artist_test=self.sjekkArtist(artist) #ser om artist_test og artisten er samme
        tittel_test=self.sjekkTittel(tittel) #ser om tittel_test og tittelen er samme
        if artist_test and tittel_test is not True: #hvis den ikke er det samme så returneres false
            return False
        else:
            return True #hvis den er det samme så returneres false
