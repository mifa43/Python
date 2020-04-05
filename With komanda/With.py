
# ovo je slicno kao prethodni primer sa try i finally samo sto ovde koristimo with komandu
# with komanda nam otvara fajl i po kraju programa on automacki zatvara dokument
# to je zato sto with komanda ima standarde i kada je pokrecemo ona u pozadini
# radi __enter__ i __exit__ otvara i zatvara bez close()
with open('pesma.txt') as f:
    for linija in f:
        print(linija, end = ' ')
