"""programmet spør deg om 2 datoer med heltall for dag og måned.
printer ut datoene og ser om datoene er i riktig rekkefølge"""




dag= input("skriv inn dag (1-31) ")         #bruker variabler med input
måned= input("skriv inn måned (1-12) ")
dato=dag+ " og " + måned

dag2= input("skriv inn dag (1-31) ")
måned2= input("skriv inn måned (1-12) ")
dato2= dag2+" og "+måned2
print("din første dato er ",dato)
print("din andre dato er ",dato2)       #printer ut datoene ved hjelp av variablene

if måned<måned2:                        #ser om måneden er i riktig rekkefølge først
    print("Riktig rekkefølge!")
elif måned>måned2:  #bruker elif siden den gir muligheten til å gå gjennom alle variablene
        print("Feil rekkefølge!")
elif dag<dag2: #hvis ikke måned 1 og måned 2 er større eller mindre enn hverandre så er de i samme måned
        print("Riktig rekkefølge!")
elif dag>dag2:
        print("Feil rekkefølge!")
else: print("samme dato!") #hvis ikke dag 1 og dag 2 er større eller mindre enn hvermande så er det lik dato
