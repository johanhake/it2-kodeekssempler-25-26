print('append:')
venner = ['Ole','Dole','Doffen']
print(venner)

# ['Ole','Dole','Doffen', 'Hetti']
venner.append("Hetti")
print(venner)

# ['Ole','Dole','Doffen', 'Hetti', 'Netti','Donald']
print('extend:')
venner.extend(["Netti", "Donald"])
print(venner)

# ['Ole','Dole','Doffen', 'Hetti', 'Netti','Letti', 'Donald']
print('insert:')
venner.insert(5, "Letti")
print(venner)