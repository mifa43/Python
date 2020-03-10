import zipfile  # ovo je modul pomocu kojega moze da se pravi zip arhiva 
#nemam dovoljno znanja ali ukombnovacu shutill i zipfile module kako bi 
#odredio gde da kreira zip arhivu 
pravizip = zipfile.ZipFile("test.zip", "w") 
pravizip.write(physicalPathOfFile, logicalPathOfFileInZip)
