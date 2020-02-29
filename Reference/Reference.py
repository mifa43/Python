print('Jednostavno dodavanje vrednosti') 
listakupovine = ['jabuka', 'mango', 'sargarepa', 'banana'] 
mojalista = listakupovine  # mojalista je samo drugo ime koje se odnosi 
print (mojalista)
# na isti objekat (listakupovine)!
del listakupovine[0]  # Kupili smo prvu stvar, pa je brisemo iz liste 
print('listakupovine je', listakupovine) 
print('mojalista je', mojalista) # obratite paznju da obe (i listakupovine i mojalista) prikazuju isti 
# rezultat # bez objekta 'jabuka', cime potvrdjujemo da one referisu na isti 
# # objekat
print('Kopiranje pomocu punog isecanja') 
mojalista = listakupovine[:]  # pravimo kopiju tako sto isecamo sve # objekte iz jedne liste
del mojalista[0]  # uklanjamo prvi objekat 
print('listakupovine je', listakupovine) 
print('mojalista je', mojalista)
# sada primetite da su liste razlicite! 

# moj primer 

listakup = ['Sir','melko','sladoled','jaja']    # ovo je lista sa nekim stavkama 
listic = listakup # listicu dodajemo vrednosti listekup i odnosi se na isti objekat
print ('\novako izgleda moja lista kupovine', listic)
del listakup[0] # ovde smo oznacili poziciju 0 sto znaci obrisi prvu stavku
print ('ovo je listakup nakon del', listakup)
print ('listic je sada', listic)    # kada smo pomocu dela obrisali prvu stavku sa listakup tj. sir automacki se brise iz listic liste to znaci  da se referisu na isti objekat
#kopiranje
print ('\nSada cemo da kopiramo pomocu punog isecanja')
listic = listakup [:]
print (listic)
del listic[0]   # ovim uklanjamo stavku na poziciji 0 tj. melko 
print ('\nlistakup je sada',listakup) # ovde je melko jel ga nismo izbrisali 
print ('listic je sada', listic)    # ovde smo izdefinisali da zelimo da se stavka melko izbrise

#   Zapamtite da ako želite da napravite kopiju liste ili neke slične vrste sekvenci ili kompleksnih objekata,
#   onda morate da koristite operaciju isecanja kako bi napravi kopiju originalnog objekta. Ako samo dodelite drugo ime varijable, oba imena će se "odnositi" na isti objekat i
#   to bi moglo da bude problem ako niste dovoljno pažljivi. 
