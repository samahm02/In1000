def minFunksjon():
    for x in range(2):
        c=2
        print(c)
        c += 1
        b = 10
        b += a
        print(b)
    return(b)

def hovedprogram():
    a = 42
    b=0
    print(b)
    b=a
    a = minFunksjon()
    print (b)
    print (a)


hovedprogram()

"""

Først defineres prosedyren minfunksjon, som ikke tar imot noen parametere.
Deretter defineres prosedyren hovedprogram, som heller ikke tar imot noen parametre.
Deretter kalles hovedprogram.

Inne i hovedprogram opprettes det to variabler a som er lik 42, og b som er lik 0.
b blir printet. og deretter blir b lik a, det vil si at b blir lik 42.
Men så blir a satt lik minfuksjon prosedyren, der er det en for løkke som printer c som er 2.
C blir plusset med 1 og blir lik 3. variablen b er lik 10, deretter blir b satt lik a.
men er kommer det en feil siden a ikke er definert i prosedyren. da stopper programet.

outputen blir:
0
2
"""
