venner = ['Ole','Donald','Doffen']
tall = list(range(10,1,-2))

print(type(venner))
print(len(venner))
print(tall, '\n')

# Ole
print(venner[0])

# Donald
print(venner[1])

# Doffen
print(venner[-1], '\n')

# ['Ole','Dole','Doffen']
venner[1] = 'Dole'
print(venner)

# antall elementer er: 3
print("antall elementer er:", len(venner))
