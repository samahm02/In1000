#lager prosedyren
def bilett():
    alder=int(input("Hei, hvor gammel er du? "))    #inneholder variabelen alder
    bilettpris= 0   #tar prisen lik 0
    if alder <= 17:     #bruker en if sjekk
        bilettpris=bilettpris+30
        print("Du skal kjøpe barnebilett for",bilettpris ,"kr")
    elif alder>17:
        bilettpris=bilettpris+50
        print("Du skal kjøpe voksenbilett for ",bilettpris," kr")
    elif alder>=63:
        bilettpris=bilettpris+35
        print("Du skal kjøpe pensjonistbilett for",bilettpris," kr")
    else:
        print("Den forsto jeg ikke! Prøv igjen")
#kjører prosedyren
bilett()


#det blir feil fordi man bør legge til "and alder<63" på linje 8 for at det skal bli riktig
