"""
her henter jeg klassen motorsykkel og lager 3 objekter og skriver dem ut i prosedyren hovedprogram

"""

from motorsykkel import motorsykkel #importerer klassen motorsykkel

def hovedprogram(): #lager prosedyren hovedprogram
    mrs= motorsykkel("Honda","As21235","10500km") #lager 3 objekter av klassen motorsykkel
    mrs2= motorsykkel("Bmw","SU30010","30202km")
    mrs3= motorsykkel("Yamaha","CF21340","2430km")
    mrs.skrivUt() #skriver ut
    print() #lager mellomrom
    mrs2.skrivUt() #skriver ut
    print() #lager mellomrom
    mrs3.skrivUt() #skriver ut
    print() #lager mellomrom
    mrs3= motorsykkel("Yamaha","CF21340","2440km") #øker den siste med 10km
    mrs3.skrivUt() #skriver ut igjen

hovedprogram() #kjører prosedyren
