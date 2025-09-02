a = [1,2]
print(f'a: {a}')

# Ikke kopi!
b = a
print(f'a is b: {a is b}')
print(f'a == b: {a == b}')

# Kopi!
c = a.copy()
print(f'a is c: {a is c}')
print(f'a == c: {a == c}')
b[0]=3
c[1]=4
print(f'b: {b}')
print(f'c: {c}')
print(f'a: {a}')
print(f'id a = {id(a)}')
print(f'id b = {id(b)}')
print(f'id c = {id(c)}')