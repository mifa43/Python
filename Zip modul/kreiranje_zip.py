import zipfile  # ovo je modul pomocu kojega moze da se pravi zip arhiva 

pravizip = zipfile.ZipFile("test.zip", "w") #moze da se koristi i samo ova komanda za kreiranje zip arhive

pravizip.write(physicalPathOfFile, logicalPathOfFileInZip)

moj_zip = zipfile.ZipFile("D:/Back-up/py/zip.zip", mode = 'w', compression=zipfile.ZIP_DEFLATED) #za putanje
moj_zip.writestr("poz.txt", "cao ti tamo") # ovako moze da se doda neki novi fajl u kreirani zip fajl 
# ^---> Ovako se navodi direktorijum u kome zelim da napravim zip fajl 
moj_zip.close() # koristi se za zatvaranje pre nego što izađete iz programa ili 
#osnovni zapisi neće biti napisan