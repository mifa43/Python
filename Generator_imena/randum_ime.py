import random  # modul za randum izbor

lista_imena = ("Minjole")     # lista zeljenih reci
lista_imena_sporedna = ("topologicar", "sekac pica", "Nigga old franja papa")  # druga lista

class Imena:   # klasa 
   def __init__(self, ime_jedan, ime_dva, konacno):   # privatna klase sa promenljivama
      self.ime_jedan = ime_jedan
      self.ime_dva = ime_dva
      self.konacno = konacno  # definisanje promenljivih pomocu kljucne reci self

   def generator(self):
      global lista_imena
      global lista_imena_sporedna

      self.ime_jedan = lista_imena #random.choice(lista_imena)     # bira nasumicno ime iz liste ime
      self.ime_dva = random.choice(lista_imena_sporedna)
      self.konacno = (self.ime_jedan + " " + self.ime_dva)  # spaja dva imena i odvaja spejsom
      print("Ime je: {0}".format(self.konacno)) # prikazujemo rezultat na ekranu

l = Imena("prvi","drugi","treci")
l.generator()  # pozivanje 