personer = []
personer.append(Person("Elise", "Bergen"))
personer.append(Person("Frida", "Stavanger"))
personer.append(Person("Gustav", "Oslo"))

person = Person("Tristan", "Bergen")
person.hils()

for p in personer:
    p.hils()
    
personer[0].flytte("Kristiansand")
personer[0].hils()