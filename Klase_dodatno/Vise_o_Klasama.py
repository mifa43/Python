# dodatni primer klasa OOP Povezivanja(Inheritance)

class ClanoviSkole: # u clnanoviskole mozemo da dodamo novo polje npr. ID u klasu 
    #promene unutar pod tipova ne uticu na druge pod tipove prednost je 
    # sto moze da se odnosi objekat profesora ili objekat studenta
    # ovo je korisno za npr prebrojavanje clanova skole ovo se zove "Polimorfizam"
    #
    '''Predstavlja bilo kog clana skole'''    
    def __init__(self, ime, godine):        
        self.ime = ime        
        self.godine = godine        
        print('(Inicijalizujem ClanoviSkole: {0})'.format(self.ime))        
    def kazi(self):        
        '''Kaze moje detalje'''        
        print('Ime:"{0}" Godina:"{1}"'.format(self.ime, self.godine), end = " ")
class Ucitelj(ClanoviSkole):  # ovako se kreira subklasa klase koju lako mozemo da pozivamo   
    '''Predstavlja ucitelja'''    
    def __init__(self, ime, godine, zarada):        
        ClanoviSkole.__init__(self, ime, godine)        
        self.zarada = zarada        
        print('(Inicijalizujem Ucitelj: {0})'.format(self.ime))        
    def kazi(self):        
        ClanoviSkole.kazi(self)        
        print('Zarada: "{0:d}"'.format(self.zarada))
class Student(ClanoviSkole):    
    '''Predstavlja ucenike'''    
    def __init__(self, ime, godine, oznaka):        
        ClanoviSkole.__init__(self, ime, godine)        
        self.oznaka = oznaka        
        print('(Inicijalizujem Student: {0})'.format(self.ime))        
    def kazi(self):
        ClanoviSkole.kazi(self)        
        print('Oznaka: "{0:d}"'.format(self.oznaka))

u = Ucitelj('Gdja. Blebetala', 40, 30000) 
s = Student('Swaroop', 25, 75)
print()  # prikazuje praznu liniju
clanovi = [u, s] # da bi smo ih povezali moramo da koristimo ime bazne klase u tupli
    # se eksplicitno navodi koriscenjem self __init__  je metoda bazne klkase exsplicitno se 
    #navodi koristeci self promenljivu 
for clan in clanovi:    
    clan.kazi()  # radi kako za Ucitelje, tako i za Studente 
# Napomena: ako se vise od jedne klase navedeno u tupli povezivanja onda se 
# to naziva multi povezivanje (multiple inheritance)
# end koji se nalazi u prikazi sluzi za promenu umesto na kraju linije bude
# zapocet novio red print() funkcija prikazuje razmak 
# Vazno: Python nece automacki da poveze konstruktorbazne klase moramo da 
# ga mi pozovemo na zeljenom mestu 
