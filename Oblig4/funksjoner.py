def adder():
    print("summen er: ")
    return print(tall1+tall2)

tall1= int(input("Skriv inn et tall: "))
tall2= int(input("Skriv inn et tall: "))

adder()

tall1= int(input("Skriv inn et tall: "))
tall2= int(input("Skriv inn et tall: "))


adder()

teller=0
setning=input("Skriv inn en setning: ")
bokstav=input("Skriv en bokstav: ")
count=0
for char in setning:
    if char == bokstav:
        count+=1
print(count)

def tellForekomst():
    count2=0
    minTekst=input("Skriv inn en setning: ")
    minBokstav=input("Skriv en bokstav: ")
    for char in minTekst:
        if char == minBokstav:
            count+=1
    print("I setningen", minTekst,"var det",count2,minBokstav)

tellForekomst()
