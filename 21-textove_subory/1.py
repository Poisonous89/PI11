fmena = open('mena.txt', 'r', encoding='utf-8') #otvori subor mena.txt na citanie r=citanie, w=zapis
# fmena = open('../mena.txt', 'r') absolutna cesta suboru

# riadok = fmena.readline()

while True:
    riadok = fmena.readline()
    if riadok == '':
        break
    print(riadok[:-1])  # [:-1] vzpise vsetky znaky od nulteho po predposledny


fmena.close() # zatvorenie suboru, vzdy treba!!!