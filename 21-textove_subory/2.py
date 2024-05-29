femena = open('mena.txt', 'r', encoding='utf-8')
fpriezviska = open('priezviska.txt', 'r', encoding='utf-8')
fmena_priezviska = open('mena_priezviska.txt', 'w', encoding='utf-8') # w otvori subor na zapis, ak neexistuje tak sa vytvori, a ak je tak sa vymaze obsah
for meno in femena:
    priezvisko = fpriezviska.readline()
    print(f'{meno.strip()} {priezvisko.strip()}', file=fmena_priezviska)
    # fmena_priezviska.write(f'{meno.strip()} {priezvisko.strip()}\n ')
femena.close()
fpriezviska.close()
fmena_priezviska.close()