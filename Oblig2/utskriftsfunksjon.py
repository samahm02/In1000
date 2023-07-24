"""dette programmet tar spør hva du heter og hvor du kommer fra.
og den bruker dette til å gi deg en hilsen. den gjør dette 3 ganger totalt"""

def hilsen():                              #lager en prsedyre
    navn=input("Hei, hva heter du? ")
    sted=input("Hvor kommer du fra? ")
    print("Hei", navn,"du er fra", sted)

hilsen()           #kjører prosedyren 3 ganger
hilsen()
hilsen()
