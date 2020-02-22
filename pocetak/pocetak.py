print ('pozdravg svima') # ovo  je komentar
ja = 19
mesto = 'koteza'
print ('ja imam {0} godina i iz {1} sam !'. format(ja, mesto)) # ja = 0, mesto = 1.. u pytonu brojevi krecu od 0,1,2,3,4..

a = 5
b = 3
rezultat = a + b
print ('Rezultat je = {0}'. format(rezultat)) # rezultat pozvan {0} racuna zadate vrednosti a i b upotrebljavajuci izrazenu formulu rezultat daje, rezultat = a + b = 8
print ((' ana ' * 1 + ' banana' * 1) * 2) # ovde se jasno vidi da python vrlo lako i jednostavno upravlja tekstom i brojevima uz operatore :)
print (5 > 3) # ako je izraz tacan daje true ako nije onda daje false 

duzina = 5
sirina = 4 
povrsina = duzina * sirina 
print ('povrsina je', povrsina)
print ('obim je ', 2 * (sirina + duzina))
# if 

broj = 7
pogadjanje = int (input('pogodi broj: ')) 

if pogadjanje == broj:
    print ('cestitam pogodio si broj: ') # pocetak prvog bloka
    print ('ali nisi osvojio nista.') # kraj prvog bloka naredbi
elif pogadjanje < broj:
    print ('ne, on je veci nego taj.')
else: 
    print ('ne, on je malo manji nego taj') # da se izvrsi else moralo je da se pogodi manji broj, pogadjanje > broj 
    print ('igra je gotova')

# while petlja 
broj = 10 # zadat broj za pogadjanje
radim = 'true' # true funkcijonise dok je pod '' navodnicima 

while radim: # pocetak petlje
    pogodi = int (input('pogodi broj: ')) 

    if pogodi == broj:
        print ('cestitam pogodio si broj: ') 
        radim = False # ovo prekida petlju
    elif pogodi < broj:
        print ('ne, on je veci nego taj.') # ako nije pogodjen broj petlja se nastavlja
    else: 
        print ('ne, on je malo manji nego taj') 
else:
    print ('petlja je gotova ovde') # ovde se zavrsava

print ('gotovo')

# for petlja

for i in range (1, 10, 3): # range funkcija ispisuje redne brojeve moze i da se dodaju 3 cifre (1, 10, 3) 
    print (i)
else:
    print ('kraj for petlje')