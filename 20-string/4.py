# if 'a' in 'aeiouy':
#     print('samohlaska')
slovo = input('zadaj slovo: ')
sh = 0
sa = 0
for i in slovo:
    if i in 'aeiouy':
        sa += 1
    else:
        sh += 1

print(f'samohlasky: {sa}')
print(f'spoluhlasky: {sh}')