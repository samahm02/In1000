"""Dette prgrammet spør om grader i farenheit,
og gjør dette om til grader i celsius"""

farenheit=int(input("Grader i farenheit? ")) #Bruker int med input for å konvertere til heltall
print(farenheit, "Grader i farenheit")

celsius=((farenheit-32)*5/9)
print("Det er ",str(celsius),"grader i celsuis")     #gjør om tilbake til tekst med str
