"""Oppgavetekst: lag en quiz med minst 3 størsmål og tell riktige svar"""

poeng=0 #lager variabel for å holde styr på poengene

navn=input("Hei! velkommen til denne quizen. Hva heter du? ")
print("Hvert riktig svar gir deg et poeng, la oss starte", navn)



spørsmål1=input("Hvor ligger verdens høyeste bygning? ") #input for å stille og få svar på spørsmål
spørsmål1=spørsmål1.lower()
"""linjen over er for å gjøre at svaret som brukeren sikriver inn ikke blir feil
på grunn av store eller små bokstaver"""
if spørsmål1=="dubai":      #bruker if og else for svarene
    print("Riktig svar")    #men har if etter hverandre som gjør at man bare går videre etter riktig svar
    poeng=poeng+1           #legger bare til +1 på poeng variablene for hvert riktig spørsmål
    spørsmål2=input("Hvor mange kontinenter er det? ")
    if spørsmål2=="7":
        print("Riktig svar")
        poeng=poeng+1
        spørsmål3=input("Hvor gammel er Messi? ")
        if spørsmål3=="34":
            print("Riktig svar")
            poeng=poeng+1
            print("Bra jobbet", navn,",du fikk alt riktig!")
        else:
            print("Feil svar, du fikk",poeng,"poeng. Det er et godt førsøk!")
    else:
        print("Feil svar, du fikk",poeng,"poeng. Prøv igjen!")

else:
    print("Feil svar, du fikk",poeng,"poeng. Øv mer til neste gang")
