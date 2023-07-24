"""
her henter jeg klassen hund og lager et objekter og kaller på spis og spring 2 ganger
dette skjer i prosedyren hovedprogram

"""

from hund import hund #importerer klassen hund

def hovedprogram(): #lager prosedyren hobedprogram
    hund1=hund("19","25") #lager objektet hund
    spis(1) #kjører spis
    hentVekt() #printer vekt
    print() #lager mellomrom
    spring() #kjører spring
    hentVekt()
    print()
    spis(1) #kjører spis
    hentVekt()
    print()
    spring() #kjører spring
    hentVekt()

hovedprogram() #kjører prosedyren
