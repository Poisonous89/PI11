def sucet(x, z):
    return x + z


def parne(cislo):
    if cislo % 2 == 0:
        return "parne"
    else:
        return "neparne"


def prvocislo(cislo):
    prvocis = True
    for i in range(2, cislo):
        if cislo % i == 0:
            prvocis = False


a = int(input("zadaj a:"))
b = int(input("zadaj b:"))
sucet = sucet(a, b)
print(f"sucet cisel {a} + {b} = {sucet}")
print(f"Cislo {a} je {parne(a)}")
print(f"Cislo {b} je {parne(b)}")
if prvocislo == True:
    print(f'Cislo {a} je prvocislo')
else:
    print(f'Cislo {a} nie je prvocislo')
if prvocislo == True:
    print(f'Cislo {b} je prvocislo')
else:
    print(f'Cislo {b} nie je prvocislo')