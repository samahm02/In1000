"""
Importerer objektet sang, og lager metodene lesFraFil,leggTilSang, fjernSang, spillSang, spillAlle,finnSang og hentArtistUtvalg

"""

from sang import Sang #Importerer sang

class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = [] #setter sanger til en tom liste
        self._navn = listenavn

    def lesFraFil(self, filnavn):
        self._filnavn = filnavn
        min_fil=open(self._filnavn) #åpner filen
        for x in min_fil: #går gjennom hver linje i filen
            linjer=x.strip().split(';') #striper og spliter på semikolon
            print(linjer)
            song = Sang(linjer[0], linjer[1]) #setter tittelen først også argisten
            self._sanger.append(song) #legger det i den tomme listen

    def leggTilSang(self, nySang):
        self._sanger.append(nySang) #legger til sang i listen

    def fjernSang(self, sang):
        if sang in self._sanger: # ser om sangen er i listen
            self._sanger.remove(sang) #hvis den er det så blir den fjernet

    def spillSang(self, sang):
        sang.spill() #spiller av via objektet sang

    def spillAlle(self):
        for song in self._sanger: #går gjennom listen
            song.spill() #spiller av sangene i listen gjennom objektet sang

    def finnSang(self, tittel):
        for song in self._sanger: #går gjennom listen
            if song.sjekkTittel(tittel):   #ser om sangen er i listen
                return song #returnerer sangen
        else:
            return None

    def hentArtistUtvalg(self, artistnavn):
        s = [] #lager en tom liste
        for song in self._sanger: ##går gjennom listen
            if song.sjekkArtist(artistnavn): #ser om artisten er i listen
                s.append(song) #hvis den er det så blir den lagd i den tomme lsiten s
                return s #returener listen s
