# 1: EN
# 2: TO
# 3: TRE
# æ ø å Æ Ø Å
with open('norsk.txt', mode='w', encoding="ascii") as fil:
    fil.write('1: EN\n2: TO\n3: TRE\n')
    fil.write('æ ø å Æ Ø Å')

# jada
# Johan
# bada
#
with open("jada.txt", mode="a", encoding="utf-8") as fil:
    fil.write("bada")
    
fil = open("jada.txt", mode="r", encoding="utf-8")
print(fil.read())
fil.close()