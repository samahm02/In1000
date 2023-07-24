"""
oppgaven: Skriv et beregningsprogram for skreddere med en funksjon som leser inn en fil
der hver linje beskriver et navn på et mål og selve målet i tommer.
La programmet legge disse målene i en ordbok med navn på målet som nøkkelverdi og returner ordboken.
Lag deretter en prosedyre som tar imot en liste av mål og benytter seg av tommerTilCm,
som du skrev tidligere for å skrive ut målene i centimeter.

"""



def tommerTilCm(antall_tommer):  #bruker prosedyren fra oppgaven tidligere
    antall_tommer=float(antall_tommer) #legger til denne til å gjøre om til desimaltall
    assert antall_tommer>0 #ser om det er noe å gjøre om
    i_cm= antall_tommer*2.54 #ganger med 2.54
    return i_cm #returnerer svaret



def p(): #prosedyre for programet
    ordbok={} #lager ordboken
    fil=open("skredder_mål.csv") #åpner filen
    for linje in fil: #for-loop som spliter og setter inn i ordboken
        biter=linje.split()
        område=biter[0]
        mål=biter[1]
        ordbok[område]=mål
        for område,mål in ordbok.items(): #for-loop som printer keyen og putter valuen i den første prosedyren
            omgjoring=område,tommerTilCm(mål)
        print(omgjoring) #printer ut ordboken med beregningene i cm


p() #kjører prosedyren
