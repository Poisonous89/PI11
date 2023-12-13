mb = 30
pb = int(input('Zadaj pocet bodov:'))
percenta = pb/mb*100
# if percenta >= 90:
#     print('Vyborny')
# else:
#     if percenta >= 75:
#         print('Chvalitebny')
#     else:
#         if percenta >= 50:
#             print('Dobry')
#         else:
#             if percenta >= 30:
#                 print('Uspokojivy')
#             else:
#                 print('Neuspokojivy')
print(f'mas {round(percenta, 2)}%')
if percenta >= 90:
    print('Vyborny')
if 75<=percenta<90:
    print('Chvalitebny')
if 50<=percenta<75:
    print('Dobry')
if 30<=percenta<50:
    print('Dostatocny')
if percenta < 30:
    print('Nedostatocny')