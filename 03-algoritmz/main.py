"""
r = int(input("zadaj polomer"))
O = 2 * 3.14 * r
S = 3.14 * r * r
print("obvod kruhu je: ", O)
print("obsah rkuhu je: ", S)
"""

a = int(input("zadaj a:"))
b = int(input("zadaj b:"))
if a > b:
    print("vacsie je cislo", a)
elif b > a:
    print("vacsie je cislo", b)
else:
    print("cisla sa rovnaju")