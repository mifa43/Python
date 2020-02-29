ime = 'Swaroop'  # ovo je prvi string objekt

if ime.startswith('Swa'):    
    print('Da, string pocinje sa "Swa"')
if 'a' in ime:    
    print('Da, string u sebi ima slovo "a"')
if ime.find('war') != -1:    
    print('Da, string sadrzi slova "war"')
razmak = '_*_' 
mojalista = ['brazil', 'Rusija', 'Indija', 'Kina'] 
print(razmak.join(mojalista)) 

# moj primer stringova

grad = 'Beograd'
if grad.startswith ('Beo'): # kao sto sam kod kaze ako grad pocinje sa 'Beo' da prikaze print
    #startswitch metoda koristi se da sazna da li string pocinje sa zadatim stringom 
    print ("\nU ovom stringu se nalazi 'Beo'")
if 'g' in grad: # ako se 'g' nalazi u gradu da nam prikaze print
    # in operator koristimo za proveru da li je dati string deo proveravanog stringa.
    print ('g se nalazi u stringu') 
if grad.find('rad') != -1:  # find metoda se koristi za trazenje polozaja stringa u stringu a ako nije uspeo da nadje substring u stringu vraca -1
    print ('rad se nalazi u stringu')
print (grad)
dodatak = ' Je divan grad :D '  # u promenljivu dodatak mozemo da dodamo brojeve,karaktere,stringove znakove i kasnije da ih pozivamo u listi
gradovi = ['Beograd', 'Novi sad','Nis']
print (gradovi)
print (dodatak.join(gradovi)) # ovde smo dodatku dali metodu join i on izmedju svake stavke u listi dodaje da divan grad osim na poslednju ali da je tu cetvrta stavka 
#dodao bi i nisu ali opet izostavio poslednju 
# join metoda spaja stringove koje mi zelimo mozemo da dodamo i _*_ za razdvajane
