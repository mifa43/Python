# Ulaz od korisnika

# U buducem poslu postojace prilika kada cemo zahvtevati da korisnik unosi nesto pomocu inputa
# bitno je da znamo dobro  da upravljamo sa njima jel se cesto koriste 

def obrnut(tekst):    
    return tekst[::-1]  # funkcija isecanja sekvenci 
    #Podrazumevan korak je 1 , zbog čega nam se uvek i vraća kontinuirani 
    # deo teksta (onako kako je i unesen). Davanje negativnog koraka, 
    # odnosno, -1 će nam vratiti tekst u "rikverc" 
def palindrom(tekst):  
    #   Palindrom je recenica koja moze da se cita od pozadi i od napred.
    return tekst == obrnut(tekst)
#nesto = input('Ukucaj tekst: ') # input() ima string kao argument i prikazuje ga korisniku. 
                            # Posle toga čeka korisnika da unesete nešto i 
                            # pritisnite taster Enter. Kada korisnik unese
                            #  nešto i pritisne taster Enter, input() će
                            #  vratiti u program taj tekst koji je korisnik uneo. 
                            # Mi koristimo taj tekst tako što ga preokrenemo. Ako su originalni 
                            # tekst i obrnuti tekst jednaki, onda 
                            # je taj tekst palindrom (rečenica koja se isto čita i piše i od 
                            # napred i od pozadi). 

rec_1 = input("Unesi palindrom: ")  # rec promenljiva je input 
# ovo je moje poboljsanje programa
def radi():
    rec_2 = rec_1.split(' ')    # razdvaja sve reci
    rec_2 = ''.join(rec_2)  # onda ih spaja sve                 
    rec_2 = rec_2.split(',')    # stavlja zarez
    rec_2 = ''.join(rec_2)  # brise zarez i spaja rec
    return rec_2.lower()    # generise sve u mala slova

if (palindrom(radi())): # provera da li je recenica palindroma 
    print('Da, to je palindrom') 
else:    
    print('Ne, to nije palindrom')

# Domaći zadatak:
# Provera da li je tekst palindrom treba da ignoriše znakove interpunkcije, 
# razmake i veličinu slova. Na primer, "A mene, ni dogodine nema." je palindrom,
# ali naš trenutni program nam ne bi prikazao da jeste. Možete li poboljšati gornji program da prepozna ovaj palindrom? 

