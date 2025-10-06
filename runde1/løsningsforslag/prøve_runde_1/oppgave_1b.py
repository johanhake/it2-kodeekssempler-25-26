høyde = int(input("Angi høyde i cm: "))
vekt = int(input("Angi vekt i kg: "))

print("BMI:", round(vekt/(høyde/100)**2, 1))