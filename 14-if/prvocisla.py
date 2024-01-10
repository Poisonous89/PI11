

while True:
    n = int(input('zadaj rozsah :'))
    print('Prvocisla:', end=' ')
    for cislo in range(n):
        pocet = 0
        # print('Delitele:', end=' ')
        for delitel in range(1,cislo+1):
            if cislo % delitel == 0:
                # print(delitel, end=' ')
                pocet = pocet + 1
        # print('| pocet delitelov je:',pocet)
        if pocet == 2:
            print(cislo, end=' ')
    print()
    if n == 0:
        break