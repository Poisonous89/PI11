

# while True:
#     cislo = int(input('zadaj cislo (pre ukoncenie zadaj nulu):'))
#     if cislo == 0:
#         print('cislo je nula')
#         break
#     elif cislo % 2==0:
#         print('cislo je parne')
#     else:
#         print('cislo je naparne')

while True:
    cislo = int(input('zadaj cislo :'))
    pocet = 0
    print('Delitele:', end=' ')
    for delitel in range(1,cislo+1):
        if cislo % delitel == 0:
            print(delitel, end=' ')
            pocet = pocet + 1
    print('| pocet delitelov je:',pocet)
    if pocet == 2:
        print('je to prvocislo')
    if cislo == 0:
        break