steder=[]

for i in range(0,5):
    sted= (input("Skriv inn et sted: "))
    steder.append(sted)




klesplagg=[]

for i in range(0,5):
    plagg= (input("Skriv inn et klesplagg: "))
    klesplagg.append(plagg)




avreisedatoer=[]

for i in range(0,5):
    datoer= (input("Skriv inn en avreisedato: "))
    avreisedatoer.append(datoer)

reiseplan=[]
reiseplan=[steder]+[klesplagg]+[avreisedatoer]

liste_nr=0
for tall in reiseplan:
    print(reiseplan[liste_nr])
    liste_nr+=1

liste_indeks1=int(input("skriv inn et tall: (0,1,2) "))
if liste_indeks1 <0:
    print("Ugyldig input!")
elif liste_indeks1 >2:
    print("Ugyldig input!")
else:
    liste_indeks2=int(input("skriv inn et tall: (0,1,2,3,4) "))
    if liste_indeks2 >4:
        print("Ugyldig input!")
    elif liste_indeks2 <0:
        print("Ugyldig input!")
    else:
        print(reiseplan[liste_indeks1][liste_indeks2])
