# 1. metode
sum1 = 1+2+3+4+5+6+7+8+9+10
print(sum1)

# 2. metode
liste = [1,2,3,4,5,6,7,8,9,10]
sum2   = 0

for tall in liste:
    sum2 = sum2 + tall

print(sum2)

# 3. metode
sum3 = 0

for tall in range(1,11):
    sum3 = sum3 + tall

print(sum3)

# 4. metode
sum4 = sum(range(1,11))
print(sum4)

# Vi kan også gjøre range om til en liste:
print(list(range(1,11)))

# Smidig IT-2 © TIP AS 2024