liste=[]


tall=int(input("skriv inn et tall: "))
liste.append(tall)

while tall != 0:
    print(tall)
    tall=int(input("skriv inn et tall: "))
    liste.append(tall)

liste_nr=0
for tall in liste:
    print(liste[liste_nr])
    liste_nr+=1

def minSum(liste):
    sum = 0
    for x in liste:
        sum += x
    print("Dette er summen av alle tallene:",sum)

minSum(liste)

m = liste[0]
for i in liste:
    if i<m:
       m = i
print("det laveste tallet i listen er",m)

n = liste[0]
for x in liste:
    if x>n:
       n = x
print("det høyeste tallet i listen er",n)
