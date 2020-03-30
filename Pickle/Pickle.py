import pickle
# ime fajla u kom zelimo da cuvamo objekat 
fajllistekupovine = 'listakupovine.data' 
# lista stvari za kupovinu 
listakupovine = ['jabuka', 'mango', 'sargarepa']
# Sacuvaj u fajl 
f = open(fajllistekupovine, 'wb') 
pickle.dump(listakupovine, f)  # stavlja objekat u fajl 
f.close()
del listakupovine  # unistava listakupovine promenljivu
# Ucitava nazad iz fajla 
f = open(fajllistekupovine, 'rb')
sacuvanalista = pickle.load(f)  # ucitava objekat iz fajla 
print(sacuvanalista) 

# Kako bi smo memorisali neki objekat u fajl prvo moramo da otvorimo
# taj fajl u 'b' - binarnom rezimu i 'w'- upisivanje ona smo pozvali dump 
# funkciju iz modula pickle ovaj proces nazivamo - "Pickling"
# preuzimamo objekat pomocu load funkcije pickle modula koja vraca objekat
# ovaj proces se naziva - "Unpickling"