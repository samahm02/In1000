#lager ordboken
måltider={
"kari nordmann":"brød til frokost, egg til lunsj og pølser til middag",
"ali olsen":"omelett til frokost, pasta til lunsj og kylling til middag",
"preben castberg":"brød til frokost, kylling til lunsj og pizza til middag"

 }


#lager prosedyre
def Beboer():
    print(måltider.keys())  #keysene er navnene
    navn=input("Skriv inn navn: ")
    navn=navn.lower()   #tar de i små bokstaver, siden navnene er det også
    if navn =="kari nordmann":  #bruker if sjekk
        print(måltider["kari nordmann"])
    elif navn=="ali olsen":
        print(måltider["ali olsen"])
    elif navn=="preben castberg":
        print(måltider["preben castberg"])
    else:
        print("Det forsto jeg ikke")
#kjører prosedyren
Beboer()


"""
oppgave 3:
a- i en mengde for å unngå like navn 2 ganger
b- ordbok, siden da kan man ha navnene som keys og poengene som value
c- i en liste
d- ordbok, siden da kan man ha allergiene som keys og navnene som value
"""
