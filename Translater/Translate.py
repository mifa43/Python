from googletrans import Translator  # ovo je modul google translate koji nudi python 

prevodilac = Translator()

unos_tekst = input("Unesi tekst za prevod: ")   # ovo je unos za tekst koji se prevodi
prevod = prevodilac.translate(unos_tekst, src="sr", dest="en")  # src = sr sa srpskog na engleski 
# za vise jezika moramo da ukucamo print(LANGUAGES)


print(unos_tekst,"--->",prevod.text)    #prevod.text nam pokazuje tekts koji se preveo