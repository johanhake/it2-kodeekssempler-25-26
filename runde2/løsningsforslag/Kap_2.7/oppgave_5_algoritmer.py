def alg(h):
    t = h
    s = 0
    r = 0
    while h != 0:
        r = h % 10
        s = s*10+r
        h = h // 10
    return t == s

# Bruker listcomprehension til å lage en liste med True og False
palindrom = [alg(tall) for tall in range(100, 1000)]
print(palindrom)
print(sum(palindrom))