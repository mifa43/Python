# Back-up skripta
import os 
from datetime import datetime   # ovo znaci iz modula datetime importuj datetime jel u jednom modulu ima vise submodula koje posebno 
# mozemo da izvlacimo i koristimo u nasem programu 
import zipfile # ovo je modul koji kreira zip arhivu

# vreme kada smo importovali vreme upotrebili smo varijablu da zapisemo trenutno vreme nakon toga
# koristimo varijablu vreme kako bi joj dodali sta da prikaze tj. sate minute i sekunde 
trenutno = datetime.now()
vreme = trenutno.strftime("%H_%M_%S")

# u def smo definisali sta zelimo da prebacimo tj. zelimo sve da prebacimo
def sve(direktorijum):

    lista = [] # ovo je lista u kojoj upisujemo fajlove u direktorijumu, subdirektorijumu i root 
   
    for root, dirs, files in os.walk(direktorijum): # root , dirs , fails je sistemski upotrebljeno kako
        # bi mogli da izvucemo fajlove i to tako mora da se pise kako bi os prepozno sta zelimo od njega
        for f_ime in files: # f_ime mozemo da nazovemo kako god zelimo 
            pch = os.path.join (root, f_ime) # ovde smo rekli os.path.join spoji/udruzi root-folder sa f_ime
            lista.append(pch) # a ovde smo u listu zapisali te stavri koje se nalaze u root folderu 

        return(lista)   # return vraca listu zabelezenih stringova
src = "C:/src"  # src je odakle se kopiraju fajlovi
lista = sve(src)    # ovde smo rekli to sto zelimo da prebaci da se nalazi src  
print('Konvertujem sa', src)  
for fajl in lista:  # ovde bukv kaze za fajl u listi prikazi liste i to radi 
    print(lista)
os.mkdir("D:/Back-up")  # ova komanda kreira folder na D lokiaciji 
with zipfile.ZipFile("D:/Back-up/zip.zip", 'w') as moj_zip: # ovde kreiramo zip fajl 
    moj_zip.writestr ("Proces_je_izvrsen.txt","Vreme izvrsavanja Back-up/a je: {0}".format(vreme))  # ovo je napisano izdvojeno kako ne bi doslo do greske ili vise puta ubacio jedan te isti txt dokument 
    # ^--- mojzip writestr pravi txt fajl i upisuje stringove i vreme koje smo definisali gore 
    for fajl in lista:  # ovde kopira se sa c i prebacuje u d za fajl u listi prepisi/kopiraj/zapisi u moj_zip a to je nasa zip arhiva koju smo kreirali 
        moj_zip.write (fajl)
print("Back-up je uspesno izvrsen, ukupno prebaceno fajlova: {0}".format(len(lista))) # ovo je potvrda 
# da je sve izvrseno i len nam racuna koliko fajlova imamo prebacenih