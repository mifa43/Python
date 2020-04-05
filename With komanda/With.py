
# ovo je slicno kao prethodni primer sa try i finally samo sto ovde koristimo with komandu
# with komanda nam otvara fajl i po kraju programa on automacki zatvara dokument
with open('pesma.txt') as f:
    for linija in f:
        print(linija, end = ' ')
