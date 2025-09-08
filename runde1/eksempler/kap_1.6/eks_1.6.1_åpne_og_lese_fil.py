with open('jada.txt') as fil:
    # jada\nJohan
    data = fil.read()
    print('read():')
    print(data)

    # ada
    fil.seek(1)
    data = fil.read(3)
    print('\nseek(); read():')
    print(data)

    # ["jada\n", "Johan\n"]
    fil.seek(0)
    linjer = fil.readlines()
    print('\nreadlines():')
    print(linjer)

    # jada
    # johan
    fil.seek(0)
    print('\nreadline():')    
    print(fil.readline(), end="")
    print(fil.readline())

    # JADA,JOHAN,
    fil.seek(0)
    print('\nfor linje in fil:')
    for linje in fil:
        # .strip(), Fjerner alle tomrom på start og slutt av string. 
        print(linje.strip(), end=",")
