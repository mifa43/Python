a = '1,2,3'.split(',')  # split je funkcija pomocu koje mozemo da 
                    # automacki dodajemo nesto tako sto izrazimo
                    # .split(',') dopdaje izmedju svakog broja zarez 
print (a)

b = '1,2,3,4'.split(',', maxsplit = 2)  # maxsplit oznacavga reindz 
                                # dokle zelimo da dodaje izrazen simbol
print (b)

rec_1 = "Ova rec je spojena"
rec_2 = rec_1.split(' ')    # razdvaja sve reci
rec_2 = ''.join(rec_2)  # onda ih spaja sve 
                          
print(rec_2)
