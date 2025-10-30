import json

ordbok = {
    'fornavn':'Per',
    'yrke':'Snekker',
    'fødselsår':1992,
    'poststed':'Askim'
}

with open('snekker_data.json', 'w', encoding='utf-8') as fil:
    json.dump(ordbok, fil, indent=2, ensure_ascii=False)

with open('snekker_data.json', encoding='utf-8') as fil:
    data = json.load(fil)

for nøkkel, verdi in data.items():
    print(f'{nøkkel.capitalize():9}: {verdi}')
