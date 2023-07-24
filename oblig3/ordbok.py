#lager en ordbok

produkter={"melk":14.90, "brød":24.90, "yoghurt":12.90, "pizza":39.90}

print(produkter)    #printer produktene

p1=input("Skriv inn et nytt produkt? ")     #ber brukeren om en ny key
pris1=input("Skriv inn pris for "+p1+" ? ") #ber brukeren om value til keyen

p2=input("Skriv inn et nytt produkt? ")
pris2=input("Skriv inn pris for "+p2+" ? ")

produkter[p1]=pris1
produkter[p2]=pris2
#setter inn de nye produktene inn i ordboken

#printer produktene
print(produkter)
