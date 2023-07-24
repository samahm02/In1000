"""dette programmet spør først om davnet ditt og gir deg en hilsen.
deretter regner ut programmet differansen (variabel c) av variablene a og b.
tilslutt spør den om enda et navn, før den printer ut navnene sammen"""

navn=input("Hva heter du? ")
print("Hei " + navn)
"""først lagde jeg variabelen navn med input, som gjør at brukeren får oppgi et navn
også printer jeg dette ut"""

a=7
b=2
c= a-b
print("Differanse:")
print(c)
"""her har jeg langd 3 variabler som er a,b og c.
a og b har heltallsverdier, mens c finner differansen på dem"""

navn2=input("Kan jeg få enda et navn? ")
sammen= print(navn+" og "+navn2)
"""her igjen har jeg lagd en variabel med input som spør om enda et navn.
sammen variabelen printer bare navnene sammen """
