import requests 
from bs4 import BeautifulSoup 
import time
import selenium.webdriver

def citaj():
    ex = ['p','h1']
    
 
    url = 'https://help.twitter.com/en/using-twitter/vine-faqs'   # stranica koju otvaramo
      
    
    resp = requests.get(url)  # pomocu requesta otvaramo stranicu
      
   
    if resp.status_code == 200:   
        print("Uspesno pronadjena web stranica") 

        soup = BeautifulSoup(resp.text,'html.parser')     #  parser oznacava tip ekstenzije npr xml,html
 
        l = soup.find("body") # trazimo telo 
      
        for s in ex:    # for za listu koja nas satrzi tagove koji ce da se citaju
            ex
            pass

        for i in l.findAll(ex): # stavljamo u variablu a i h tagove
            time.sleep(1)       # time za sporije ispisivanje texta
            print(i.text)   # i vracamo kao text
    else: 
        print("Error") 
          
citaj()