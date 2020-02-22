# liste u pytonu 
# spisak .append
spisak = ["Mleveno meso", "Brasno", "x10 Jaja", "Sir"]

print (spisak)
spisak.append("Jogurt") # funkcija .append dodaje u listu stavku koju izrazimo u zagradama
print (spisak)

# spisak 2 .insert
spisak1 = ["Sir", "Jaja"]
print(spisak1)
spisak1.insert(0, "melko") # .insert naredba pomocu nje mozemo da dodamo novu stavku na spisak (0, "x") oznacava poziciju i dodajemo melko
print(spisak1)
spisak1.insert(2, "papir") # a ovde se dodaje melko i papir na dve vec izdefinisane stavke 
print(spisak1)

# spisak 3 .remove 

spisak3 = ["Mleveno meso", "Brasno", "x10 Jaja", "Sir"]
print (spisak3)
spisak3.remove("sir") # remove brise vrednost sa spiska koja je navedena u zagradama
print (spisak3)

# spisak 4 .pop

spisak4 = ["Hleb", "Secer", "Vanila"]
print (spisak4)
spisak4.pop() # .pop izbacuje stavku sa spiska u zagradi se navodi njena pozicija ako ostavimo praznu zagradu po defoultu ce obrisati poslednju vrednost
print (spisak4)

spisak4 = ["Hleb", "Secer", "Vanila", "Sok", "banane"]
print (spisak4)
spisak4.pop(4) # kada smo dodali vrednost 4 oznacili smo da zelimo da izbrisemo "banane" jel u pythonu brojanje krece 0,1,2,3,4 banane su na lokaciji 5
print (spisak4)

# spisak 5 .clear

spisak5 = ["Cips", "Bombone", "Slag", "Riba", "Paradaiz"]
print (spisak5)
spisak5.clear () # .clear brise sve stavke sa naseg spiska i ostavlja samo []
print (spisak5)

# spisak 6 

spisak6 = ["Hleb", "Secer", "Vanila", "Sok", "banane"]
print (spisak6.index("Secer")) # broji pozicije i vraca broj pozicije od vrednosti izdefinisane u zagradi = 1 jel u pythonu se broji od 0 ne  od 1 
print (spisak6.index("banane", 1)) # raspitaj se za ovo

# spisak 7 .count

spisak7  = ["Hleb", "Secer", "Vanila", "Sok", "banane", "Hleb", "hleb"]
print ('ovo je count')
print (spisak7.count("Hleb")) # broji koliko se puta ponavlja navedena stavka hleb znaci 0,1,2
print (spisak7.count("Secer"))
print (spisak7.count(""))

# spisak 8 .sort

print ('sort opcija')
spisak8 = [3,6,5,2,4,1] # obrojevi su izmesani kada smo dodali .sort sortira nam brojeve od manjeg ka vecem 1,2,3,4..
spisak8.sort()
print(spisak8)

spisak8 = [3,6,5,2,4,1]
spisak8.sort(reverse=True) # Sortira od veceg ka manjem 6,5,4,3.. kada smo dodali (reverse=true) znaci sortiraj od veceg ka manjem a 'false' daje od manjeg ka vecem
print(spisak8)

spisak8 = ["Hleb", "Secer", "Vanila", "Sok", "banane",]
spisak8.sort() # raspitaj se sa vraca
print(spisak8)

spisak8 = ["Hleb", "Secer", "Vanila", "Sok", "banane"]
spisak8.sort(key=len)# raspitaj se sa vraca
print(spisak8)


spisak8 = ["Hleb", "Secer", "Vanila", "Sok", "banane"]
spisak8.sort(key=len, reverse=True) # raspitaj se sa vraca
print(spisak8)


# NASTAVI DALJE SA LISTAMA I OBNOVI 
help(list) # za pomoc oko lista 

