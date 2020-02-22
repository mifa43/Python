def broj (c, a): #sve sto je iza taga def- 'broj' se naziva parametrom.. a unutar parametra (c, a)- argument 

    #samo za svaki def promeni ime i bice bez greske
    
    if c < a:
        print (c, 'je manje')
    elif c == a:
        print (c, 'je jednako sa', a)
    else:
        print (c, 'je vece od', a)
broj(4, 5)  # izdefinisali smo vrednosti parametra c, b
x = 12 # x se dodeljuje argumentu c
y = 6 # y dodeljujemo argumentu a
broj(x, y)
# lokalne funkcije

 # definisao sam vrednost x ona vazi za ceolu funkciju bloka programa # x = 50 dodaj u kod da bi radio prgoram 
def funk (x):
    print ('x je: ', x)
    x = 3 # x se ispsiuje lokalno samo za taj deo koda 
    print ('promenili smo lokalnu x u', x)
funk (x)
print ('x je jos uvek', x) # a ovde vidimo da je x = 3 uticalo samo na deo koda iznad a ovde je x = 50 kao sto je napocetku napisano 
print ('x je jos uvek', x)

# global promenljiva
 

#x = 30 obrisi komentar # izvrsava se sve dok ne dodje do sledeceg argumenta 'x = 100'
def funk():
    global x        # pomocu globala moze da se izdefinise novi argument u promenljivoj x i nakon toga krece da vazi novi argument 
    print('x je', x)  # ovde se zavrsava 
    x = 100 # ovde se zbog naredbe global zanemaruje 'x = 30' i pocinje da se izvrsava ova naredba 
    print('Promenjena globalna vrednost promenljive x na', x)
    print('Promenjena globalna vrednost promenljive x na', x)
    print('Promenjena globalna vrednost promenljive x na', x)

funk() 
print('Vrednost promenljive x sada je', x) # i ispisuje se do ovde
    # moze da se doda jos global naredbi u blok programa npr (x, y, z) funkcijonisace na istom principu kao sto pise gore

def kazi(poruka, puta = 1): # parametru kazi smo dali argumente i 'puta je dodeljena promenljiva' dobro napisano je (poruka, puta = 1), moze (poruka = 2, kazi = 1), lose (a = 1, b)
    print(poruka * puta)
kazi('dobro') # unutar pozvane funkcije moze da se zadaje rec koja ce biti ispisana
kazi('jutro', 7) # ovde je jutro * 7 ispisace se 7 puta to znaci da je poruka po defaultu = 1 

    # argumenti definisani kljucnom reci
def funk(a, b = 10, c = 20):
    print('a je', a, ',a b je', b, 'i c je', c)
funk(4,13)
funk(55, c = 39)
funk(c=500, a = 300)
    