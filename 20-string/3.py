ret = input('Zadaj retazec: ')
posun = int(input('Zadaj posun pre kodovanie: '))
# print(ord(ret))

for i in ret:
    print(i,"",ord(i))

ret_kod = ""
for i in range(len(ret)):
    print(f'{ret[i]}:{chr(ord(ret[i])+posun)}')
    ret_kod += chr(ord(ret[i])+posun)

print(f'Zakodovany retazec: {ret_kod}')