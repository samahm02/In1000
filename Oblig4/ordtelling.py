

def bokstaver():
    telle_bokstaver=input("Skriv inn et ord: ")
    print(len(telle_bokstaver))

bokstaver()


def ord_teller(setning):
    teller = dict()
    ordene = setning.split()

    for ord in ordene:
        if ord in teller:
            teller[ord] += 1
        else:
            teller[ord] = 1
    return teller

print(ord_teller(input("Skriv inn en setning: ")))
