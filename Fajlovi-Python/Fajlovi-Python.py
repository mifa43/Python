# Manipulacija fajlovima pomocu Pythona

pesma = '''\
    Programiranje je zabavno,
    ali kada otkucas nekoliko linija 
    u Pyhonu shvatas da je to ljubav. 
        #STAYATHOME WITH PYTHON !
'''
f = open('pesma.txt', 'w')  # W je mod za pisanje
f.write (pesma)
f.close()   # obavezno je zatvaranje

f = open('pesma.txt', 'r')  # ako se 'r'-read ne upise bice po defaultu r -citanje
while True:
    linija = f.readline()#readline metoda sluzi za citanje svake linije pomocu while petlje

    if len(linija) == 0:
        break
    print (linija, end = ' ')   # pomocu enda smo sprecili prelazak u novi red
f.close

# Otvori svoj novo kreirani txt dokument i prover da li je program uradio sve sto 
#smo zahtevali od njega 


#   Režim može biti: čitanje ('r'), pisanje ('w')
#  ili dodavanje ('a'). Takođe možete odrediti da li će se čitanje, 
# pisanje, ili dodavanje odvijati u tekstualnom modu ('t') ili
# u binarnom modu ('b')
# mozemo i da odemo help(open)