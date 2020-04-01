#   Podizanje Exceptiona
# Python kada cita nas kod i izvrsavaga i naidje na gresku on dize ruke
# to se naziva 'raises'- i recice da postoji greska
import time # za treci program
# try:
#     tekst = input('Unesi tekst -->')
# except EOFEror: # except klauzula sluzi za hvatanje greske uvek ide uz try
#     print('Zasto si mi uradio EOF?')
# except KeybordInterrput:
#     print('Ti si ponistio operaciju.')
# else:   # i else mozemo da dodamo try  
#     print('Ti si uneo {0}'.format(tekst))
# >>>>Odkomentarisi gornji program<<<<<

# Raise
class Izuzetak_za_kratak_unos(Exception):# Ovde smo stvorili sopstveni izuzetak'exception'
    '''Klasa definisana od korisnika'''
    def __init__(self, duzina, najmanje):# duzina je duzina unesenog teksta
        Exception.__init__(self)        # najmanja je najmanja dozvoljena duzina unosa
        self.duzina = duzina
        self.najmanje = najmanje
try:
    unos = input('Unesi nesto ---> ')
    if len(unos) < 3:
        raise Izuzetak_za_kratak_unos(len(unos), 3)# greska u koliko je unos manji od 3 
        # Ovde moze da bude definisano i nesto drugo
except EOFError:
    print('Zasto si mi uradio EOF?')
except Izuzetak_za_kratak_unos as ex:
    print('Izuzetak_za_kratak_unos: Unos je {0} kraktera dug, ocekivano je najmanje {1}'.format(ex.duzina, ex.najmanje))
else:
    print('Nijedan Exception nije podignut.')
# >>>>>>>>>>odkomentarisi i ovo <<<<<<<<<<<<<<<
# Try i Finally

try:    # finally mozemo da koristimo sa try,exception klauzulom kao i sa elsom
    f = open('pesma.txt')
    while True:
        linija = f.readline()
        if len(linija) == 0:
            break
        print(linija, end = ' ')
        time.sleep(2)   # funkcija iz time modula nakon svake linije odspava 2 sekunde
except KeyboardInterrupt:   # upotrebi ctrl + c ima i #EOFError ctrl + d = Windows korisnik
                        # kada smo pokrenuli KeyboardInterrupt program se prekida 
                        # ali bez obzira na to fajl koji smo citali se zayvara jer
                        # se nalazi u finally klauzoli i izvrsava se i objekat datoteke
                        # se uvek zatvara
    print('\n!! Ti si mi prekinuo citanje fajla.')
finally:
    f.close()
    print('(Cistimo: Zatvaram fajl.)')
