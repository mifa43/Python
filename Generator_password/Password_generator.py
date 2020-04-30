import random   # modul za nasumican izbor
import string   # ascii znakovi

randum_str = string.ascii_letters   # daje listu stringova malih i velikih karktera

class Password: # klasa
    def __init__(self, bira_karakter, sifra):   # privatna klase

        self.bira_karakter = bira_karakter
        self.sifra = sifra  # promenljive

    def daje_pass(self):    
        
        global randum_str

        # bira nasumicno karakter iz liste assci znakova. for petlju smo iskoristili 
        # da obelezimo duzinu/broj karaktera 
        self.bira_karakter = (random.choice(randum_str)for i in range(9))
        self.sifra = ''.join(self.bira_karakter) 
        # onda smo svaki karakter spojili sa join 

        print("Vasa nova lozinka je: ",self.sifra)  # prikazujemo rezultat lozinke

i = Password("Password", 'Nasumicno')
i.daje_pass()   # ovako se poziva klasa


