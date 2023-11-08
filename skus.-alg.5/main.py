"""
a = int(input("zadaj cislo a: "))
b = int(input("zadaj cislo b: "))
c = int(input("zadaj cislo c: "))
print("najvacsie cislo je", c)
# daco je zle ked som vymeni elif a if
if a == b == c:
        print("vsety cisla sa rovnaju")
elif a > b:
    if a > c:
        print("najvacsie cislo je", a)
    else:
        print("najvacsie cislo je", c)
else:
    if b > c:
        print("najvacsie cislo je", b)
    else:
        print("najvacsie cislo je", c)
"""

a = int(input("zadaj cislo a: "))
b = int(input("zadaj cislo b: "))
c = int(input("zadaj cislo c: "))
d = int(input("zadaj cislo d: "))
e = int(input("zadaj cislo e: "))
max = a
if max < b:
    max = b
if max < c:
    max = c
if max < d:
    max = d
if max < e:
    max = e
print("najvacsie cislo je: ", max)