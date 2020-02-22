while 'true':
    s = input ('ukucaj rec: ')
    if s == 'izlaz':
        break
    if len(s) <= 3: # len koristimo funkciju da dobijemo duzinu stringa 'space' se isto racuna
        print ('previse je kratka rec koju ste uneli')
        continue    # continue ako uneta rec pomocu inputa nije veca ili jednaka 3 karaktera nece se nastaviti dalje od naredbe iznad 'continu' funkcije 
    print ('uneta rec je zadovoljavajuce veliine') # ako je <= 3 odstampace se print i tako zavrsiti program
    