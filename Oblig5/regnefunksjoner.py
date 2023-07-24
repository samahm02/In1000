"""
dette programmet ber brukeren om to tall som blir addert,subtrahert og dividert
videre spør den om enda et tall som den gjør fra tommer til cm
"""



def addisjon(tall1,tall2): #prosedyre for addisjon med 2 parametre
    sum=tall1 + tall2 #plusser tallene
    return sum #retuernerer sumen av tallene


def minus(tall3,tall4): #prosedyre for minus med 2 parametre
    minus1= tall3- tall4 #trekker fra tallene
    return minus1 #returnerer dette

def dele(tall5,tall6): #prosedyre for deling med 2 parametre
    dele1= tall5/tall6 #deler på hverandre
    return dele1 #returnerer det



assert minus(3,2)==1  #kjøere assertene 3 ganger for minus og dele prosedyren
assert dele(5,2)==2.5
assert minus(-3,1)==-4
assert dele(10,-2)==-5
assert minus(-17,-12)==-5
assert dele(-9,-3)==3


def tommerTilCm(antall_tommer): #prosedyre for å gjøre fra tommer til cm, men en paramenter
    assert antall_tommer>0 #bruker assert
    i_cm= antall_tommer*2.54 #ganger med 2.54 og får tallet i cm
    return i_cm #returnere tallet i cm



def skrivBeregninger(): #prosedyre som inneholder de andre prosedyrene
    tall_1=int(input("Skriv inn et tall: ")) #spør brukeren om tall
    tall_2=int(input("Skriv inn et tall: ")) #spør brukeren om tall
    print("resultatet av summering:",addisjon(tall_1,tall_2)) #setter inputen inn i addisjon prosedyren
    print("resultatet av substraksjon:",minus(tall_1,tall_2)) #setter inputen inn i minus prosedyren
    print("resultatet av divisjon:",dele(tall_1,tall_2)) #setter inputen inn i dele prosedyren
    print("kontertering fra tommer til cm:")
    tommer_tall=int(input("Skriv inn et tall: ")) #spør brukeren om tall
    print("resultatet i cm:",tommerTilCm(tommer_tall)) #setter inputen inn i tommerTilCm prosedyren

skrivBeregninger() #kjøerer hovedprogrammet
