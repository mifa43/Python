
izbor = int(input("""Zdravo, ovo je spisak za kupovinu odaberi jednu od sledecih opcija: 
1. Dodaj stavku na spisak
2. izlaz
"""))
lista = [ ] 
n = int(input("Unesi broj stavki koje kupujemo : "))
if n == 0:
    print ('Uneo si 0 stavki u spisak')

if izbor == 1:
    
    for i in range(0, n):
        element = [input("Unesi stvaku: "), int(input("Unesi kolicinu: "))] 
        lista.append(element)
        
        print ('Vasa lista za kupovinu je',lista)
