import sounddevice as sd
from scipy.io.wavfile import write
import winsound
import speech_recognition as sr
import soundfile as sf
import webbrowser
import subprocess

lista = []
unos = int(input("Unesi broj '1' za unos glasovne poruke: "))

def rekorduj():
    global lista
    fs = 44100  # frekvencija u hz
    seconds = 5  # trajanje zvuka
    mojrekording = sd.rec(int(seconds * fs), samplerate=fs, channels=2) # kanali za snimanje
    sd.wait()  # pauziranje kako bi se snimijo zvuk
    write('output.wav', fs, mojrekording)  # pisanje i cuvanje zvuka u wav format

    # winsound.Beep(1000, 100)    # beep winsound modul za slusanje snimljenog zvuka
    # filename = "output.wav" # ekstenzija fajla je wav 
    # winsound.PlaySound(filename, winsound.SND_FILENAME) #  plejer 

    data, samplerate = sf.read('output.wav')    # modul za konvertovanje wav fajla u \
    sf.write('output.flac', data, samplerate)  # flac fajl 
    # nisam bas strucan za audio produkciju ali koliko sam procitao razlika izmedju wav i flaca je u frekvenciji i kanala emitovanja
    # i iz tog razloga speech_recognition modul za pisanje zvucnih fajlova u txt fajlove ne moze da koristi wav, mp3.. itd audio formate ali mu odgovara flac

    r = sr.Recognizer() 
    hard = sr.AudioFile('output.flac') # audio fajl koji citamo 
    with hard as source:    # otvaranje i konvertovanje audio fajla u tekst 
        audio = r.record(source)
    rec_1 = r.recognize_google(audio)   # izgovorenu recenicu stavljamo u variablu

    rec_2 = rec_1.split(" ")    # zatim pomocu splita rastavljamo recenicu i stavljamo u listu
    lista_cmds = ['open', 'copy']     # lista komandi koje mogu da se izvrsavaju npr open ima svoju listu sta moze da otvara dok do nema nista za sad
    lista_za_open = ['YouTube', 'Google', 'Python']    # lista cmds ima komandu open komanda open ima listu sadrzaja sta moze da otvori
    lista_za_copy = ["file", "directory"]
    lista_simbola = ["/", "\\", "c"]
    #print(lista_simbola[1])
    provera = any(item in rec_2 for item in lista_cmds)     # any funkcija pravi proveru da li rec_2 i lista_cmds ima zajednicko nesto ako ima vraca nam bool true ili false ako nema
    if provera == True:     # ako je tacno ulazimo u sledeci blok
        for i in rec_2:     # proveravamo reci iz liste i liste cmds ako postoje pomocu filtera mozemo da je ispisemo
            
            filt_object = filter(lambda a : i in a, lista_cmds)
            provera_2 = any(item in rec_2 for item in lista_za_open)
                
            if provera_2 == True:
                    filt_object_2 = (filter(lambda b : i in b, lista_za_open))
                    konvert = ''.join(list(filt_object))#filte_object pretvaramo u listu kako bi mogli da utvrdimo da li su izgovorene reci odgovarajuce ovom bloku
                    konvert_2 = ''.join(list(filt_object_2))    # flit_ogject je konvertovan u listu ali sa join pretvaramo u string tj. rec koja je izgovorena a pritom je komanda iz list_cmds

                    if 'copy' in konvert or konvert_2 == True :    # zato sto 'copy' komanda se nalazi u listi i kada kazemo do youtube otvara se yt ili bilo sta drugo morao sam da regulisem ako neko
                        break   # kaze do da ne otvara stvari koje se otvaraju sa open za to sam koristio bool ako se 'copy' nadje u reci da brejkujemo do sledece linije onda odatle mozemo da dodamo komande za copy 
                    if (konvert == 'Google' or konvert_2 == 'Google'): 
                        subprocess.call("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe") # subprocess otvara chrome ako filter objekti sadrze navedenu recu if uslovu google
                        break   # nakon otvaranja taba brejkujemo program
                    if (konvert == 'YouTube' or konvert_2 == 'YouTube'):    #uslovi za otvaranje su promenjeni vise nema open iz razloga jel taj uslov vec postoji da nismo rekli open ne bi ni dosli do ovog bloka
                        url = 'http://youtube.com/'     # url stranice koju otvaramo
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'  # ovo je lokacija chroma
                        webbrowser.get(chrome_path).open(url, new=1)    # prosledjujemo path i otvaramo url u novom prozoru
                        break   # nakon izvrsavanja brejkujemo program
                    if (konvert == 'Python' or konvert_2 == 'Python'): 
                        url = 'http://docs.python.org/'     
                        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'  
                        webbrowser.get(chrome_path).open(url, new=1)   
                        break
            else:
                print("Ova komanda ne moze da izvrsi taj proces")
    else:
        print("Rec nije komanda")


    provera = any(item in rec_2 for item in lista_cmds) # kreiramo novu proveru za komandu copy 
    if provera == True:
        for i in rec_2:
            filt_object = filter(lambda q : i in q, lista_cmds)
            provera_3 = any(item in rec_2 for item in lista_za_copy)

            if provera_3 == True:   # ako komanda file postoji u listi_za_copy ulazimo u blok
                filt_object_3 = (filter(lambda w : i in w, lista_za_copy))
                konvert = ''.join(list(filt_object))
                konvert_3 = ''.join(list(filt_object_3))
                

                info = """Za pomeranje fajlova navodi sa backslash za nazad i slash za napred"""
                
              
                if konvert == 'file' or konvert_3 == 'file':    # provera da li je file u nekoj od varijabli
                    print("file")
                    print(info)
                    names = []
                    izlaz = ''
                    recenice = []
                    while izlaz != 'quit':  # WHILE petlja traje sve dok se u listu za izlaz ne upise quit dok se unosi n nastavlja se snimanje reci
                        izlaz = input("Unesi 'n' za sledeci simbol ili 'quit' za izlaz: ")
                        names.append(izlaz)

                        if izlaz == 'quit': # izlaz iz petlje
                            break

                        print("3")
                        print("2")
                        print("1")

                        fs = 44100
                        seconds = 3
                        mojrekording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
                        sd.wait()  
                        write('output.wav', fs, mojrekording)  

                        data, samplerate = sf.read('output.wav')    
                        sf.write('output.flac', data, samplerate)  
                        
                        r = sr.Recognizer() 
                        hard = sr.AudioFile('output.flac') 
                        with hard as source:
                            audio = r.record(source)
                        navodi = r.recognize_google(audio)
                        navodi_2 = navodi.split(" ")
                        recenice.append(navodi_2)   # dodajemo u listu reci i karaktere koji su uneseni

                    
                    for t in recenice:
                        list_src = []   # u ovoj listi treba da pokusamo da spojimo zasebne karaktere i simbole da stvorimo naziv nekog foldera/direktorijuma
                        print(t[0])
                        if 'slash' in t:    # kada kazemo recenicom slash i ako je u t onda dodeljujemo vrednost simbola 
                            t = '/'
                            list_src.append(t)
                            
                        if lista_simbola[1] in t:  
                            t = lista_simbola[1]    
                            list_src.append(t)
                        if 'see' in t:  # posto modul nije najpametniji i ne moze da razlikuje spelovanje od slova potrebno je da navedemo neke od slova za neke od reci kako ih on tumaci i da sami dodelimo vrednost 
                            t = 'c'     # posto c je procitao 10-20 puta kao see i kada kaze see dodamo da je to vrednost c
                            list_src.append(t)
                        if 'colon' in t:
                            t = ':'
                            list_src.append(t)
                        for m in list_src:
                            print(m[0])
                            
                        
                    # print(names)
                   

                #lista abecede koja ne moze u ovaj program
                # s-see, h-ash, o-oh, p-b, q-kwel, r-are, s-ass, oce/t-d, u-you, v-we, y-why       

                   

                if konvert == "directory" or konvert_3 == 'directory':
                    print("directory")


if unos == 1:
    rekorduj()
    
# u nekim trenucima pre izgovora komande postoji greska zbog malih i velihih slova to pokusaj da resis sa uper ili lower komandom da generises pocena velika slova jel je svaka rec u listi
# za svako slovo koje je teze protumaciti dodaj kako ga tumaci i jednako kako bi trebao nakon toga sastavi karaktere i simbole u jednu variablu i i pokusaj sa os da proveris da li postoju dir 
# ako postoji ispisi ga da korisnik prvo vidi da li je to to na sta je mislio 