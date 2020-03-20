# help(int)
#objektivno orjentisano programiranje, klase pocetak, metode objekta

# metod
class licnost:    # class naredbom stvaramo novu klasu uvucen deo se zove telo klase
    def zdravo(self):   # self je instanca kalse, koriscenjem kljucne reci self mozemo pristupiti 
                    #atributima i metodama tih klasi 
        print("Pozdrav, kako si?")
L = licnost()   
L.zdravo()  # mozemo i da napismeo licnost().zdravo() 

#init metode

class leba:
    def __init__(self, ime):    # klase imaju metode init sa donjim crtama pokazuje specijalnu
                        # vrstu metoda nazivaju se (konstruktor) automacki se poziva prilikom
                        # kreiranja nove klase. konstruktor upotrebljavamo da zadamo pocetne
                        # vrednosti  varijablama iz klase konstruktor u ovom slucaju sadrzi 
                        # 1 varijablu. konstruktor(__init__) prihvata jednu vrednost (ime)
                        # i dodeljuje varijabli klase self.ime
        self.ime = ime
    def vreme(self):
        print('Ja se zovem ', self.ime)
k = leba('Milos')
k.vreme()


    # objekat se sastoji od dve stvari: podataka i funkcija(nazivamo ih metodama) one rade
    # sa podacima kao sto su stringovi oni su u pythonu objekti. podaci u string-objektu su 
    # slova koje string cini to znaci da nisu samo stringovi objekti vec i celi brojevi,
    # dec brojevi, cak i same funkcije 

# Prakticniji primer 

class robot:
    '''Zdravo ja sam robot sa imenom. '''

    # >!< Promenljiva objekta sa istim imenom kao i promenljiva klase ima 
    # da sakrije promenljivu klase >!<

    populacija = 0  # pripada klasi(robot) naziva se promenljiva klase 

    def __init__(self, ime):    # promenljiva (ime) pripada objektu 
        '''Inicijalizacija podataka'''  # dodeljujemo ime objektu upotrebom self
        self.ime = ime          # ovo je promenljiva objekta
        print('(Inicijalizujem {0})'.format (self.ime))

        robot.populacija += 1   # promenljiva klase (populacija) pozivamo kao
            # (robot.populacija) a ne kao self.populacija

    def __del__(self):
        '''Greska! Greska! #EROR/101'''
        print ('{0} je unisten!'.format(self.ime)) # promenljivu objekta pozivamo kao
                # (self.ime) unutar metoda tog objekta
        robot.populacija -= 1

        if robot.populacija == 0:
            print ('{0} je bio poslednji'.format(self.ime))
        else:
            print ('Funkcionalno je jos {0:d} robota'.format (robot.populacija))
    def zdravo(self):
        '''Pozdrav homosapijensi. 
            
            
        Da, roboti to mogu!'''
        print ('Pozdravljam vas stvoritelju, mozete me zvati {0} . '.format (self.ime))
    #@staticmethod
    def koliko():#< je metoda koja pripada klasi a ne objekatu to znaci
        # da ga pozivamo kao classmethod  ili staticmethod. 
        # a mozemo i da koristimo dekoratere koje stavljamo pre def
        # @staticmethod
        
        '''Prikazujem trenutnu populaciju robota.'''

        print ('Ima jos {0:d} robota'.format (robot.populacija))
    koliko = staticmethod(koliko)


megabot1 = robot('RP-MP1')

megabot1.zdravo()
megabot1.koliko()

megabot2 = robot('ARP-P2.0')

megabot2.zdravo()
megabot2.koliko()

print ("\nRoboti mogu da rade ovde nesto.\n")

print ("Roboti su zavrsili svoj posao sada se unistavaju")

del megabot1
del megabot2

print ('Svi su unisteni')
robot.koliko()

# Dekorateri vise: Dekorater mozemo da zamislimo kao precicu za pozivanje eksplicitne komande 
# varijablama i metodama istog objekta se obracamo sa self ovo se zove 'referenca atributa'

# Clanovi klase su javni osim ako sadrze dve donje crte kao prefiks primer. __privreda
# Paython ce koristiti specijalno znacenje i efikasno ce je uciniti privatnom promenljivom
# svaka promenljiva koja se koristi u okviru klase ili objekta pocinje sa dvostrukom
# donjom crtom a svi ostali nazivi su javni i mogu se koristiti od strane drugih kalsa/objekta
