"""
dette programmet ber brukeren om å skrive inn i.p eller s.
i- spør brukeren om navn og epost suffix og lagrer dette i ordbok
p- skal kombinere navnene og suffixene fra orboken med @ imellom
s- skal stoppe while loopen
"""

def lagbrukernavn(): #lager prosedyre
    navn=input("Hva heter du? ") #spør brukere om navn
    navn=navn.lower() #gjør det om til små bokstaver og spliter dem
    delt=navn.split()
    brukernavn=delt[0]+delt[1][0] #tar hele fornavnet og bare første bokstaven i etternavnet
    return brukernavn #returnerer brukernavnen

def lagEpost(): #lager prosedyre
    brukernavn_=lagbrukernavn() #kjører den første prosedyren
    suffix= input("Hva vil du at suffixen skal være? ") #spør om suffix
    suffix=suffix.lower() #gjør det om til små bokstaver
    email=brukernavn_+"@"+suffix #tar dem sammen
    print(email) #printer eposten


def skrivUtEposter(personer): #lager prosedyre
    for x, y in personer.items(): #for loop med ordboken
        print(x+"@"+y) #printer key og value sammen som en epost



ordbok={} #lager ordboken
input=input("Skriv inn i,p eller s: ") #ber brukeren om å skrive inn i.p eller s
while input != "s": #loopen kjøere så lenge inputen ikke er s
    if input =="i": # får 'str' object is not callable feil her
        lagEpost()
        orbok[brukernavn]=suffix
    elif input=="p": # får 'str' object is not callable feil her
        skrivUtEposter(ordbok)
    input=input("Skriv inn i,p eller s: ")

#får feil når inputen er i eller p, når den er s så stopper den som den skal
