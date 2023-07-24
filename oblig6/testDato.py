"""
her henter jeg klassen dato og tester ut lesAar,skjekk dag og hent dato med 2 datoer
dette gjør jeg i prosedyren hovedprogram.
"""


from dato import dato #importer klassen dato

def hovedprogram(): #lager prosedyren hovedprogram
    d1 = dato(15, 1, 2001) #setter inn 2 datoer
    d2 = dato(1, 1, 2001)
    print(d1.lesAar()) #skriver ut datoens år
    d1.sjekkDag() #skjekker om det er 1 eller 15
    datoDagEn = d1.hentDato() #lagrer datoen som en variabel
    print(datoDagEn) #printer ut datoen

hovedprogram() #kjører prosedyren
