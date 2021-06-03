def main(): 
    s = slanje()[0] # pozivamo slnje
    return s + 'svete!!!'   # dodajemo vrednst
def slanje():   
    a = prima() # pozivamo glavni def
    a[0]    # citamo prvu vrednost a[0]
    return a    #vracamo

def prima():    # glavna definicija


    def prima2():   


        def prima3(*args):  # definicija sa parametrom l
            args = []  # l pretvaramo u listu i dodajem vrednost (str, int, funkcije)
            args.append("zdravo!!!")

            return args    # vracamo l iz definicije

        return prima3()    # vracamo def u def 

    return prima2() 
    
y = main() + "1234" # i ovako mozemo da dodelimo vrednos
print(y)
