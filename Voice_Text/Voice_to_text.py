import sounddevice as sd
from scipy.io.wavfile import write
import winsound
import speech_recognition as sr
import soundfile as sf
import webbrowser
import subprocess

lista = []
unos = int(input("Unesi broj '1' za unos glasovne poruke:"))

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

    lista_cmds = ['open', 'do']     # lista komandi koje mogu da se izvrsavaju npr open ima svoju listu sta moze da otvara dok do nema nista za sad
    lista_za_open = ['YouTube', 'Google', 'docs.python.org']

    provera = any(item in rec_2 for item in lista_cmds)     # any funkcija pravi proveru da li rec_2 i lista_cmds ima zajednicko nesto ako ima vraca nam bool true ili false ako nema
    if provera == True:     # ako je tacno ulazimo u sledeci blok
        for i in rec_2:     # proveravamo reci iz liste i liste cmds ako postoje pomocu filtera mozemo da je ispisemo 
            filt_object = filter(lambda a : i in a, lista_cmds)
            provera_2 = any(item in rec_2 for item in lista_za_open)
            if provera_2 == True:
                    filt_object_2 = filter(lambda b : i in b, lista_za_open)
                    if ('open' and 'Google' in list(filt_object), list(filt_object_2)): #filte_object pretvaramo u listu kako bi mogli da utvrdimo da li su izgovorene reci odgovarajuce ovom bloku
                        subprocess.call("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
                        break
            else:
                print("ova komanda to ne moze")
    else:
        print("Rec nije komanda")

        #webbrowser.open("https://www.youtube.com")
            
if unos == 1:
    rekorduj()