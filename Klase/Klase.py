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

# Ovo je prakticniji primer 