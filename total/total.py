    # total 
def total(inicijal=10, *brojevi, **kljucnereci):"""pojavljuje se greska jel sam 
                                                        vise puta definisao istu stvar kopiraj odvojeno svaki prmier"""
    # brojanje = inicijal

    # # for broj in brojevi:  
    # #     brojanje += broj   

    # for rec in kljucnereci: 
    #     brojanje +=kljucnereci[rec]    
    #     return brojanje
                                        #postoji greska
print(total(10, 1, 2, 3, povrce = 50, voce = 100)) 

#ponovi 41 total nakon sto naucis sta je tuple i druge termine 
def total(papir = 12, *cena, **porez):
    ugovor = papir
    for broj in cena:
        ugovor += broj
    for rec in porez:
        ugovor += porez[rec]
    return ugovor
print (total(10, 1, 2, 3, kola = 100, provizija = 150 ))

# total samo sa kljucnim recima
def total(inicijal = 5, *broj, **ekstra_broj):
    brojanje = inicijal
    for broj in brojanje:
        brojanje += broj
        brojanje += ekstra_broj
    print(brojanje)

total(10, 1, 2, 3, ekstra_broj=50)
total(10, 1, 2, 3) 
#obnovi sve sa total