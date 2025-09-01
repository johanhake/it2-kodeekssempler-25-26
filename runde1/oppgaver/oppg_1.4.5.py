forrige = 1
forrige_forrige = 1
vist_tall = 2
print(forrige, forrige_forrige, end=" ")
while vist_tall < 10:
    neste_tall = forrige + forrige_forrige
    print(neste_tall, end=" ")
    vist_tall += 1
    forrige_forrige = forrige
    forrige = neste_tall