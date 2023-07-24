"""
her lager jeg en kalsse personer med metodene leggTilHobby, skrivHobbyer og skrivUt.

deretter bruker jeg prosedyren hvoedprogram til å spørre om navn og alder og setter denne inn i klassen
der har jeg også en while loop, som lar deg skrive hobbyer og stopper når man skriver s.
tilslutt printer den ut navnet og alder sammen med hobbyene
"""

class person:  #lager klassen
    def __init__(self,navn,alder): #lager konstruktøren med navn, alder og hobbyer som en tom liste
        self._navn=navn
        self._alder=alder
        self.hobbyer=[]

        def leggTilHobby(self, hobby): #lager metoden som legger til hobbyer
            self._hobbyer.append(hobby)

        def skrivHobbyer(self): #lager metoden som skriver ut listen
            for i in self._hobbyer:
                print("- " + i)

        def skrivUt(self): #skriver ut navn og kaller på at listen med hobbyer skrives ut
            print(f"{self._navn}, {str(self._alder)} år")
            self.skrivHobbyer()

def hovedprogram(): #lager prosedyren hovedprogram
    navn=input("Hva heter du? ") #spør om navn og alder
    alder=input("Hvor gammel er du? ")
    p_1=person(navn,alder) #setter dette inn i klassen
    inputGodkjent = True #setter denne variabele til true
    print("Hobby (skriv 's' for å avslutte): ")
    while inputGodkjent != False: #loopen skal gå helt til variabelen blir false
        hobbyer = input("> ")
    if hobbyer == 's': #hvis imputen er s så blir den false og hopper ut av loopen
        inputGodkjent = False
    else:
        p1.leggTilHobby(hobbyer) #hvis inputen ikke er s så blir det lagt i listen
    print() #lager mellomrom
    p_1.skrivUt() #skriver ut navn,alder og listen med hobbyer

hovedprogram() #kjører hovedprogrammet
