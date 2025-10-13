def fjern_over_10(liste):
    ret = []
    for x in liste:
        if x <= 10:
            ret.append(x)
    return ret

def fjern_over_10_pent(liste):
    return [x for x in liste if x <= 10]

liste = [4,7,8,2,45,2143,6453,687,3,3,6,234,45,6,234,]

print(fjern_over_10(liste))
print(fjern_over_10_pent(liste))