

try:    # pyton kalkulator
    odg_1 =  int (input("""Ovo je kalkulator, izaberi sledece mogucnosti:
1. Sabiranje
2. Oduzimanje
3. Mnozenje
4. Deljenje
"""))
except:
    print ("mogu da se samo unesu brojevi !")
    exit ()
try:
    if odg_1 == 1:
        prvi_broj  = int (input("tvoj prvi broj je: "))
        drugi_broj = int (input("tvoj drugi broj je: "))
        rezultat = prvi_broj + drugi_broj
        print ("Rezultat je {}" .format(rezultat))
    elif odg_1 == 2:
        prvi_broj  = int (input("tvoj prvi broj je: "))
        drugi_broj = int (input("tvoj drugi broj je: "))
        rezultat = prvi_broj - drugi_broj
        print ("Rezultat je {}" .format(rezultat))
    elif odg_1 == 3:
        prvi_broj  = int (input("tvoj prvi broj je: "))
        drugi_broj = int (input("tvoj drugi broj je: "))
        rezultat = prvi_broj * drugi_broj
        print ("Rezultat je {}" .format(rezultat))
    elif odg_1 == 4:
        prvi_broj  = int (input("tvoj prvi broj je: "))
        drugi_broj = int (input("tvoj drugi broj je: "))
        rezultat = prvi_broj / drugi_broj
        print ("Rezultat je {}" .format(rezultat))
    else:
        print ("nisi upisao dobro broj.")
except:
    print ("mogu da se koriste samo brojevi !")

