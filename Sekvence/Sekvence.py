# Sekvence liste,tuple i stringovi
listakupovine = ['jabuka', 'mango', 'sargarepa', 'banana'] 
ime = 'swaroop'
# Operacija indeksiranja ili Subscription 
print('Stvar 0 je', listakupovine[0]) 
print('Stvar 1 je', listakupovine[1]) 
print('Stvar 2 je', listakupovine[2]) 
print('Stvar 3 je', listakupovine[3])

print('Stvar -1 je', listakupovine[-1]) 
print('Stvar -2 je', listakupovine[-2]) 
print('Znak 0 je', ime[0])
# secenje liste 
print('Stvari od 1 do 3 su', listakupovine[1:3])
print('Stvari od 2 do kraja su', listakupovine[2:]) 
print('Stvari od 1 do -1 su', listakupovine[1:-1]) 
print('Stvari od pocetka do kraja su', listakupovine[:])
# secenje stringa 
print('Znakovi od 1 do 3 su', ime[1:3]) 
print('Znakovi od 2 do kraja su', ime[2:]) 
print('Znakovi od 1 do -1 su', ime[1:-1]) 
print('Znakovi od pocetka do kraja su', ime[:]) 

# Sekvence moj primer

mojp = ['sir', 'mleko', 'jaja', 'brasno']
ime = 'Milos'

# primer indeksiranja operacija Subskripcije
print ('\nPozicija 0 je', mojp[0])  # kada smo pozvali listu mojp u uglastoj zagradi [] definisali smo broj koji oznacava poziciju stavke u listi u ovom slucaju 0 je sir u Pythonu brojevi krecu od 0 
print ('Pozicija 1 je', mojp[1])
print ('Pozicija 2 je', mojp[2])
print ('Pozicija 3 je', mojp[3])
# negativni brojevi
print ('\nPozicija -1 je', mojp[-1]) # kada koristimo negativne brojeve nasa lista se prikazuje od pozadi -1 = barso, -4 = sir brojevi krecu -1,-2,-3,-4,-5...
print ('Pozicija -2 je', mojp[-2])
print ('Pozicija -4 je', mojp[-4])
# Znakovi
print ('\nznak 0 je', ime[0]) # posto ime nije navedeno u [] ili {} tretira se kao str-string a brojevima u uglastim zagradama nam prikazuje karakter koji se nalazi na toj poziciji 
print ('znak 1 je', ime[1])
print ('znak 2 je', ime[2])
print ('znak 3 je', ime[3])
print ('znak 4 je', ime[4])

# isecanje lista

#   0       1      2        
#  sir    mleko   jaja   
#  -3      -2     -1        

print ('\npozicije od 1 do 3 je', mojp[1 : 3])  # kada smo napisali 1 : 3 rekli smo da je 3 granica i nece napisati 3 stavku da smo napisali 1 : 4 granica je 4 i nece je preci ali napisace 3 stavke
print ('pozicije od 0 do 4 je', mojp[0 : 4]) # od 0 : 4 oznacili smo da zelimo da vidimo sve stvake
print ('pozicije od 1 do -1 je', mojp[1 : -1]) # 1 je pozicija mleka dok je -1 pozicija jaja 
print ('Pozicije svih stavki je ', mojp[:]) # kada smo stavili dvotacku ':' rekli smo da zelimo da vidimo sve iz liste 

# isecanje stringa

#   0  1   2   3   4
#   m  i   l   o   s
#  -5 -4  -3  -2  -1

print ('\npozicije stringova od 1 do 3 je', ime[1 : 3]) # pozicija 1 = i dok je 3 granica znaci pozicija 2 = l  broj 3 je granica to znaci da prikazuje karaktere do 3 pozicije nama je 3 = o u prevodu to znaci Paython prikazi mi karaktere na poziciji od 1 do 3 ali ne i treci karakter
print ('pozicije stringova od 3 : je', ime[2:])  # znaci prikazi sve od drugog karaktera do kraja da smo stavili 0 : = to bi dalo kao rezultat ceo string = milos
print ('pozicije od 1 do -1 je', ime[1 : -1])   # pozicija 1 oznacava poziciju i dok -1 je granica  i prikazuje nam tako da 1 : -1 oznacava ilo 
print ("oznaka ':' daje", ime[:]) # prikazuje nam ceo string
# Napomena : Prvi broj (pre dvotačke) u operaciji isecanja, se odnosi na poziciju odakle isečak počinje, a drugi broj (posle dvotačke) pokazuje gde će se zaustaviti sečenje tj. granica