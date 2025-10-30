import json

with open('navn_alder.json',encoding='utf-8') as fil:
    data = json.load(fil)

print('*** print data(list/dictionaries) ***')
print(data)
print(type(data))
for obj in data: print(type(obj))

print('\nNavnliste:\n**********')
for obj in data:
    for  nøkkel, verdi in obj.items():
        print(f'{nøkkel.capitalize():6}: {verdi}')
    print()

from pprint import pprint
print('\n*** pprint - Data pretty printer ***')
pprint(data)

print('\n*** print data (str) ***')
with open('navn_alder.json',encoding='utf-8') as fil:
    data = fil.read()
print(type(data))
print(data)




