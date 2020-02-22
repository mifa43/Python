def mojmodul (): # pyton je modularni jezik to znaci da mozemo da uvozimo neke njegove biblijoteke vec napisanih funkcija, a isto tako mozemo da definisemo nase funkcije
                 # i da ih pozovemo u drugom nasem programu 
    odg_1 =  int (input("""Ovo je kalkulator, izaberi sledece mogucnosti:
1. Sabiranje
2. Oduzimanje
3. Mnozenje
4. Deljenje
"""))
    if odg_1 == 1:
        prvi_broj  = int (input("tvoj prvi broj je: "))
        drugi_broj = int (input("tvoj drugi broj je: "))
        rezultat = prvi_broj + drugi_broj
        print ("Rezultat je {}" .format(rezultat))
mojmodul ()
    # obnovi module kompletno
import os; # pomocu ove naredbe mozemo da vidimo direktorijum u kom se nalazi nas program 
print(os.getcwd()) 
# import naredba se koristi kako ne bi doslo do sukoba imena pri pozivanju modula jel praksa je da se modulu doda verzija sa importom cemo izbeci sukob from mojmodul import kaziZdravo, __version__

