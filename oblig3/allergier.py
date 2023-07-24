"""i denne oppgaven skal bruke en ordbok til å lage en liste av hva de ulike
personene tåler eller ikke. print ut navene til gjestene og bruk en if sjekk """

#her lager jeg ordboken som inneholder hva gjestene ikke tåler
allergi={
"Tåler alt":{"jonas","petter","ole"},
"Gluten allergi":{"jenny","lukas","henrik"},
"Laktose inntoleranse": {"preben","andreas","vetle"}

 }

#lager en prosedyre
def mat():
     print(allergi.values())    #printer ut navnene til gjestene
     navn=input("Velkommen! Skriv inn navn: ")
     navn=navn.lower()  #tar de i liten skrift, fordi navnene er i liten skrift i ordboken
     if navn in allergi["Tåler alt"]:   #ser hvis navnet er i tåler alt
         print("Du tåler alt! Her er menyen")
     elif navn in allergi["Gluten allergi"]:
         print("Du har gluten allergi, her er menyen uten gluten")
     elif navn in allergi["Laktose inntoleranse"]:
         print("Du er laktose inntolerant, her er menyen uten laktose")
     else:  #hvis navnet ikke er i noen av keysene så printer den ut dette
         print("Du er ikke i listen, ble du invitert?")
#kjører prosedyren
mat()
