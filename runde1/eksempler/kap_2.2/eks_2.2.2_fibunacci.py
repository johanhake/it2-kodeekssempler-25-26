a = 0
b = 1
n = 10

print(a, b, end=" ")
for i in range(2,n):
    # Skriv de neste tre linjene på EN linje!
    c = a+b
    a = b
    b = c
    print(b, end=" ")
    