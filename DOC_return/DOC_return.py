def minimum (x, y):
    if x < y :
        return x # upotrebljavamo kad nesto zlimo da vratimo iz funkcije
    elif x == y:
        return 'brojevi su jednaki' # ako su x i y jednaki vraca iz funkcije da su jednaki 
    else:
        return y # ako napisemo samo return po defaultu se intrepetira kao return none vraca nista nema vrednost
print (minimum(12, 12))
print(minimum.__doc__)
# docstring 
def prikazMaksimuma(x, y):
    '''kako ovo radi ?
    moze u vise redova 
    ovo je super'''
    x = int(x) 
    y = int(y)

    if x > y:
        print(x, 'je maksimum')   
    else:        
        print(y, 'je maksimum')

prikazMaksimuma(30, 10)
print(prikazMaksimuma.__doc__)  # funkcijonise tako sto smo pozvali funkciju parametra + doc i u programu ako se nadje '''komentar''' ispisuje se na prozoru pomocu printa ovo koristi svaki put kada si u mogucnosti

    # import naredba
from math import sqrt 
print("Kvadratni koren iz 16 je" , sqrt( 16 ))

# obnovi pyc import 47a