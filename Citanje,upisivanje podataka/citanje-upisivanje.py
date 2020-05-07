fajl = open("test.txt","w")
# \t = ima ulogu taba u programu
# \n = ima ulogu entera
# "r" = Rezim citanja upotrebljava se samo kada se cita
# "w" =  Režim pisanja koji se koristi za uređivanje i upisivanje novih 
# podataka u datoteku (sve postojeće datoteke sa istim imenom biće 
# izbrisane kada se aktivira ovaj režim)
# "a" = Režim dodavanja, koji se koristi za dodavanje novih podataka na kraj 
# datoteke to jest novih podataka se automatski dopunjuje do kraja
#  "r+" = Specijalni režim čitanja i pisanja, koji se koristi za obradu 
# obe radnje pri radu sa datoteko

fajl.write("\tZdravo pajton sam pise") 
fajl.write("\nOvo je program za back-up") 
fajl.write("\nUskoro ce biti i datm realizacije") 
fajl.write("\n\nVerzija-0.1") 

fajl.close() 

# >!< Program kreira sam fajl i cuva ga za izrazavanje tacne lokacije
#     mozemo upotrebiti modul shutill >!<