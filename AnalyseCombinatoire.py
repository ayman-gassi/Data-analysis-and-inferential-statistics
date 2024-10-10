def factoriel(nbr):
    if nbr == 0 or nbr == 1:
        return 1
    else:
        return nbr * factoriel(nbr - 1)

def combinaison(n, r):
    return factoriel(n) // (factoriel(r) * factoriel(n - r))

def puissance(nbr,r):
        for i in range(1,r) :
            return nbr * puissance(nbr,i)



