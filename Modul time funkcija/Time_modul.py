import time # uvezli smo modul 

from datetime import datetime

sad = datetime.now()    #varijable smo upoptrebili kako bi lakse pozvali program

balkan = sad.strftime("%H:%M:%S:%Y")   # sati minuti sekunde ako dadte Y= years godina
print("Vreme na Balkanu je: ", balkan)
