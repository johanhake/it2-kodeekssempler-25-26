# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
for i in range(10): 
    print(i, end=", ")
print()

# range(1,10) -> 1, 2, 3, 4, 5, 6, 7, 8, 9,
for i in range(1, 10):
    print(i, end=", ")
print()

# range(10,1) -> tomt!!
for i in range(10,1):
    print(i, end=", ")
print()

# range(1,10,2) -> 1, 3, 5, 7, 9
for i in range(1,10,2):
    print(i, end=", ")
print()

# range(10,1,-2) -> 10, 8, 6, 4, 2
for i in range(10,1,-2):
    print(i, end=", ")