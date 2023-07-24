dag= input("skriv inn dag (1-31) ")
måned= input("skriv inn måned (1-12) ")
dato=dag+ " og " + måned

dag2= input("skriv inn dag (1-31) ")
måned2= input("skriv inn måned (1-12) ")
dato2= dag2+" og "+måned2
print(dato,dato2)

if måned<måned2:
    print("Riktig rekkefølge!")
elif måned>måned2:
        print("feil rekkefølge!")
    elif måned=måned2 and dag<dag2:
            print("Riktig rekkefølge!")
        elif måned=måned2 and dag>dag2:
                print("feil rekkefølge!")
            elif måned=måned2 and dag=dag2:
                    print("samme dato!")
