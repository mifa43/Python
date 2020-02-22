zoo = ('piton', 'slon', 'pingvin') # zapamtite da su zagrade opcionalne print('Broj zivotinja u zooloskom vrtu je', len(zoo))
novi_zoo = 'majmin', 'kamila', zoo 
print('Broj kaveza u novom zooloskom vrtu je', len(novi_zoo)) 
print('Sve zivotinje u novom zooloskom vrtu su', novi_zoo) 
print('Zivotinje koje su donete iz starog zooloskog vrta su', novi_zoo[2]) 
print('Poslednja zivotinja doneta iz starog zooloskog vrta je', novi_zoo[2][2]) 
print('Broj zivotinja u novom zooloskom vrtu je', len(novi_zoo),1+len(novi_zoo[2])) 

# tuple
print ('ovo je moj primer tupla')
#nab promenljiva
nab = 'ekseri','srafovi','matice','farba' # zagrade nisu obavezne ali je bolje sa zagradama kako bi izbegli dvosmislenost jel da smo napisali ('a','b','c') ovo prikazuje da su u zagradama tri karaktera a b c 
                                            # ( ('a','b','c') ) - ovo govori da je rec o tupleu koji sadrzi tri karaktera a b c 
nab_jos = ('daske','cekic','sravciger', nab)
print ('Broj stvari koje mi trebaju da napravim kucicu za pse je', len(nab_jos)) #kada smo dodali tuple nab len funkcija nam je prebrojala 4 u nab_jos jel i zajsta jesu 4 stavvke bez obzira sto se u nab nalaze jos 3 stavke
print ('Ovo su stvari koje mi trebaju', nab_jos) # kada smo u nab_jos dodali nab prikazuje i njegove stavke 
print ('Prvo mi trebaju',nab_jos[0])    # kada smo definisali broj u [] mi smo oznacili brojem poziciju stavke koju zelimo da prikazemo
print ('Poslednja stvar koja mi treba za kucicu je', nab_jos [3][3])  #kada smo kod nab_jos u [3] dodali broj oznacili smo poziciju tj. 3 to je tuple nab a u drugoj [3] oznacili smo cetvrtu poziciju u nabu tj. farbu koja se prikazuje
                                                                    # u tuple mogu da se odrede pozicije i negativnim brojevima 0 je isto kao i -9 dok ":" oznacava da prikaze sve sto se nalazi u tupleu
print ('Broj stavki koji imamo je', len(nab_jos),'i', 2 + len(nab_jos[3])) # len funkcija racuna broj stavki u nab_jos a kada smo napisali 2 + len(nab_jos[3]) izracunao je 4 i dodao jos 2. u pythonu brojevi krecu od 0 

my_tuple = ("zdravo")    #ovako napisano ukazuje na str-string
print(type(my_tuple))

my_tuple = ("zdravo",)  # a ovako napisano sa zarezom na tuple
print(type(my_tuple))   # ovo se koristi ako zelimo tuple sa jednom stavkom