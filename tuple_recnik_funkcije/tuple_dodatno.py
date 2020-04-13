# Slanje tuple i recnika funkcijama


#  Ovo je korisno kada treba poslati promenljivi broj argumenata za funkciju
def suma_stepena(stepen, *argument):    # zvezdica ispred parametra 'argument'
    # * je prefiks svi dodatni argumenti koje dajemo funkciji se cuva u 
    # *argument kao tuple ako se u mesto jedne zvezdice koristi prefiks
    # ** dodatni parametar se smatra kao kljuc/vrednost parova unutar recnika 
    '''Vraca sumu svih argumenata stepenovanih
    na specijalni broj'''
    totalno = 0
    for i in argument:
        totalno += pow(i, stepen)
    return totalno
print(suma_stepena(2, 3, 4))
print(suma_stepena(2, 10))