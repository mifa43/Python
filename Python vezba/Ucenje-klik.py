# ovo je moja vezba ono sto pokusavam da napravim jeste program pomocu koga mogu da otvorim Notpade za beleske,Google za istrazivanje i youtube jel slusam muziku dok ucim
import os   # pomocu import naredbe pozvali smo vec postujece module
import subprocess
import webbrowser
print ("Zdravo, srecno ucenje")

solucija = int(input('''Odaberi sledece opcije  
1.Otvori Notpad
2.Otovri Google
3.Otvori Youtube
4.Opis Programa
'''))   # sa int input oznacili smo da je dozvoljeno samo unositi brojeve

if solucija == 1:
    print ('Otvaram notpad')
    os.system('Notepad.exe')    # otvara notpad.exe ili aplikacije u sistemu 

elif solucija == 2:
    print ('Otvaram Google')
    webbrowser.open ('http://Google.com')

elif solucija == 3:
    print ('Otvaram Youtube')
    webbrowser.open ('https://www.youtube.com/watch?v=sV2t3tW_JTQ') # otvara stranice browsera 

elif solucija == 4:
    print ('Zdravo ja sam Python treba ti opis programa ?')
    print("Da / Ne")    # koristi veliko slovo kako bi radilo
    pomoc = input("")
    if pomoc == "Da":
        print ('Ja sam program koji sluzi za lakse ucenje')
        print ('Ono sto ja radim jeste otvaranje stvari koje ti trebaju za ucenje')
        print ('******************************************************************')
        print ('Mogu da otvorim Notpad ako odaberes opciju 1')
        print ('Mogu da otvorim Google ako odaberes opciju 2')
        print ('Mogu da otvorim Youtube ako odaberes opciju 3')
        print ('******************************************************************')
        print ('Verzija-0.1')
    else:
        print ('Zasto si odabrao opis ako ne zlis da saznas opis programa ?!')
else:
    print ('Dozvoljeno je unositi samo brojeve koji su izrazeni')
