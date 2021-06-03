import shutil # shutil je modul za kopiranje i pomeranje fajlova

src = "C:/src"  # u src je naapisana putanja faja iz kog pravimo kopiju
dst = "C:/dst/sve"  # ovo je folder gde zelimo da pastujemo /sve pravi novi folder 
# ako ne stavimo /sve izbacice gresku 

shutil.copytree(src=src, dst=dst)   #ovim izvrsavamo proces