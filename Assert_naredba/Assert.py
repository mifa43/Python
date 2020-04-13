# Assert naredba

moja_lista = ['stvari']
assert len(moja_lista) >= 1
moja_lista.pop()
print(moja_lista)

# assert naredba se koristi kada zelimo da ptvrdimo da li je nesto tacno ili ne
# ako ste sigurni da ćete imati barem jedan element u listi koju koristite,
#  a želite da proverite, i da podignete grešku ako to nije istina, onda 
# je assert komanda idealna u toj situaciji. Ako assert komanda ne prođe, 
# AssertionError je podignut. 