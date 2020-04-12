
x = lambda a : a + 10

print(x(5))

def moja_funkcija(n):   # def sadrzi parametar n 
    return lambda a : a * n 
duplo = moja_funkcija(2)    # n dobija vrednost 2
print(duplo(11))    # a = 11

tacke = [{'x' : 2, 'y' : 3}, {'x' : 4, 'y' : 1}]
tacke.sort(key = lambda i : i['y'])
print(tacke)

# Lambda se koristi za kreiranje novih objekta funkcija, uzima parametar
# pracen jednim izrazom i postaje telo funkcije vrednost izraza je
# vrednost koju vraca nova funkcija

# lambda funkcija nam zamenjuje def blok koji bi smo mogli da pozovemo 
# u tom jednom slucaju ali kada smo kreirali lambda funkciju mozemo
# je pozivati kad god nam to treba 