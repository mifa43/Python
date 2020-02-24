# kontakti u pythonu
# tuple unutar neke druge tuple ne gube svoj identitet (tj i dalje su - tuple, a ne pojedinačni objekti koji su sačinjavali staru tuplu). Možemo pristupiti stavkama unutar tuple navodeći položaj te stavke u paru 
# uglastih zagrada baš kao što smo uradili za liste. Ovo se zove operator indeksiranja
# 'ab' je skracenica za 'a'-address 'b'-book 
ab = {'Pandimenzionalni' : 'pd@ma.cme',      
      'mega'             : 'mno@hoo.moo',
      'giga'             : 'kokos@kokoda.lom',
      'troler'           : 'gong@pong.pet'}

print("Trolova adresa je", ab['troler'])
# brisanje para kljuc-vrednost 
del ab['troler']
print('\nImamo {0} kontakata u adresaru\n'.format(len(ab)))
for ime, adresa in ab.items():    
    print('Kontaktiraj {0} na {1}'.format(ime, adresa))
# Dodavanje para kljuc-vrednost 
ab['Genije'] = 'popara@lebac.voda'
if 'Genije' in ab:    
    print('\nAdresa genija je', ab['Genije']) 

# moj primer imenik 

ab = {'Ognjen' : 'OgnjenPY@gmail.com',  # ab je skracenica za adres book u ab se definise kljuc ime_id bitno je da je navedeno ime jedinstveno kako nam ne bi doslo do greske prilikom pozivanja iz knjige adresa npr'Ognjen'
      'Aleksandar' : 'AleksandarCS@yahoo.com',
      'Aleksa' : 'AleksaBUCK@gamil.com',
      'Nemanja' : 'NemanjaMACE@yahoo.com',
      'Minja' : 'MinjaTrap@hotmail.com'}

print ("\n\nOgnjenov mejl je", ab['Ognjen']) # kao i u C \n ima funkciju entera. prilikom printanja ab se poziva u uglastim zagradama [] i u njima navodimo kljuc koji je jedinstven ab['Ognjen']
del ab['Ognjen']    # pomocu del-a smo obrisali ognjena i vise se ne prikazuje u nasim kontaktima
print ('\nU mojoj knjizi adresa imam {0} kontakta ali bice ih vise!\n'.format(len(ab))) # U viticastoj {} zagradi smo pozvali vec definisanu ab i pomocu .format je ukljucili u print i len je izracuno koji je broj kontakta = 5 kontakta

for ime, adresa in ab.items():  # u for petlji smo definisali varijable ime i adresu koje se nalaze u ab-u for nam izvrsava od prvog do poslednjeg kontakta u ab.itemu
    print ('Moje prijatelji se zovu {0} a njihov mejl je {1} a adresa '.format(ime, adresa))  # sa formatom smo je ukljucili u funkciju {0} poziva imena a {1} mejl adresu 

ab ['Milos'] = 'Mifa43@gmail.com' # ab ima promenljivu vrednost 'milos' ona je jednaka mojoj mejl adresi 'mifa43@gmail.com'
if 'Milos' in ab:   # ovde smo rekli ako je milos u ab da se isprinta moja mejl adresa ovo je jos jedan primer kako mozemo da definisemo kontakt 
    print ('\nMoja adresa je', ab['Milos'])
# help(dict) ovde mozemo da procitamo vise o funkciji 