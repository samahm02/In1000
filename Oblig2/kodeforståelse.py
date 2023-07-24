"""her har de glemt å gjøre om heltallet tilbake til tekst
når de skal printe helt til slutt.

Dette programmet vil også ha problemer med desimaltall
siden det ikke kan gjøres om til et heltall"""

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print (str(b) + "Hei!")
