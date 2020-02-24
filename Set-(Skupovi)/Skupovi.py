# Skupovi u Pythonu
skup = set (['srbija','hrvacka','bosna'])   # set oznacava da je rec o skupu skup se pise u ([neka vrednost])
print (skup)    # ovde prikazujemo nas skup
if 'srbija' in skup:    # ovde smo upotrebili if petlju pa ona ovako radi ako je srbija u skupu prikazi srbija se nalazi u skupu.. 
    print ('srbija se nalazi u skupu')      
    'madjarska' in skup # da li je madjarska u skupu python proverava vidi da nije i prikazuje madjarska se ne nalazi u skupu
    print ('madjarska se ne nalazi u skupu')

skupina = skup.copy()   # pomocu funkcije .copy smo kopirali parametre skup 
skupina.add ('Crna gora')   # pomocu funkcije .add smo skupini dodali 'crnu goru'
print (skupina) # to znaci da je skupina jednaka skup i da kopira sve iz tog skupa i da doda 'crnu goru' i prikazuje 4 zemlje

skupina = skup.issuperset (skup)    # vraca true ako svi elemeti skupa A se nalaze u skupu B ako se ne nalaze false
print (skupina)

skup.remove ('bosna')   # sa funkcijom .remove smo obrisali bosnu i prikazuje samo 2 zemlje unutar skupa A
print (skup)
#skupina.intersection (skup) # ova funkcija proverava sta se nalazi u preseku AnB npr A = 2,4,6,8    B = 1,3,4,7,8   AnB = 2,8 radi sa brojevima,stringovima pa cak i listama kao sto vidimo skup je neki spisak zemalja
#print (skupina) komentarisanesu linije 18,19 kako ne bi prikazivo gresku jel nemamo nista sto se nalazi u skupu i skupini


# skup tretirajte kao A, skupinu kao B

