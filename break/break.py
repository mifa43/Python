while True:
    s = input('Ukucaj neku rec: ')
    if s == 'izlaz': # promenljiva s jednaka 'izlaz'-(moze da se stavi bilo sta rec, broj..) 
        break   # break ako se ukuca izrazena rec 'izlaz' break funkcija zanemaruje print('Duzina stringa je', len(s)) i prelazi na sledeci red koda 'kraj'
    print('Duzina stringa je', len(s))
print('izlaz')