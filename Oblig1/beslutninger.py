"""dette programet spør først om du har lyst på brust,
 og etter som hva du svarer så vil du fa en et svar"""



brus= input("Har du lyst på brus? (Ja/Nei) ")  #bruker variabel med input for å stille spørsmålet
if brus== "ja":
            print("Her har du en brus!") #hvis du svarer ja, så printer ut programet dette
elif brus== "nei":
            print("Den er grei.")  #her bruker jeg elif fordi den gir meg muligheten til å se etter flere svar enn bare en
else:print("Det forstod jeg ikke helt.") #else blir brukt her for alle andre svar enn ja eller nei
