liste=[2,9,19]  #lager liste
liste.append(40) #legger til i listen

print(liste[1], liste[3])   #printer ut element nr 1 og 3

navn=[]     #lager ny liste

navn.append(input("skriv inn et navn: "))   #spør om navn og setter det inn i navn listen
navn.append(input("skriv inn et navn: "))
navn.append(input("skriv inn et navn: "))
navn.append(input("skriv inn et navn: "))

if "sameer" in navn:    #bruker if sjekk til å se om mitt navn er der
    print("Du husket meg!")
elif "Sameer" in navn:
    print("Du husket meg!")
else:
    print("glemte du meg?")

liste2=[]   #lager ny liste
sum=liste[0]+liste[1]+liste[2]+liste[3] #legger sammen tallene i liste 1
produkt=liste[0]*liste[1]*liste[2]*liste[3] #ganger tallene i liste 1

liste2.append(sum)
liste2.append(produkt) #legger de nye tallene i liste2

siste_liste=liste+liste2 #setter sammen listene
print(siste_liste)
siste_liste.remove(70) #fjerner de 2 siste tallene
siste_liste.remove(13680)

print(siste_liste) 
