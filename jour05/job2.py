nb = input("Entrez un nombre :\n")
exp = input("Entrez la puissance :\n")

def puissance(nb, exp):
    if exp == 1:
        return nb
    else:
        return nb * puissance(nb, exp - 1)
    
print(puissance(int(nb), int(exp)))