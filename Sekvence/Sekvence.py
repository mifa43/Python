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