def hils(person):
    print(f"Hei, jeg er {person['navn']} og jeg kommer fra {person['bosted']}.")

def flytte(person, nytt_bosted):
    if nytt_bosted in ["Bergen", "Stavanger", "Oslo", "Kristiansand"]:
        print(f"{person['navn']} flytter fra {person['bosted']} til {nytt_bosted}")
        person["bosted"] = nytt_bosted
    else:
        raise ValueError(f"{nytt_bosted} er ikke med i gyldige steder å flytte til")

if __name__ == "__main__":

    personer = []
    personer.append(dict(navn="Elise", bosted="Bergen"))
    personer.append(dict(navn="Frida", bosted="Stavanger"))
    personer.append(dict(navn="Gustav", bosted="Oslo"))

    for p in personer:
        hils(p)

    flytte(personer[0], "Kristiansand")
    hils(personer[0])