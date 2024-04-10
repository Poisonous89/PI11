retazec = input('Zadaj retazec:')
print(retazec)
# print(retazec[0])

# for i in range(len(retazec)):
#     print(i , retazec[i])

# i = 0
# for znak in retazec:
#     print(i, znak)
#     i += 1

# print(retazec[-2])

for i, znak in enumerate(retazec):
    print(i, znak)
print()
for i, znak in enumerate(retazec[::-1]):
    print(-i, znak)

# toto nieje dovolene
# retazec[0] = 'a'