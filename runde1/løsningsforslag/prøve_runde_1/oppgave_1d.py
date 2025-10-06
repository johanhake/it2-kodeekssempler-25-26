print("BMI-kalkulator")
while True:
    try:
        høyde_input = input("Angi høyde i cm: ")
        if høyde_input == "":
            break
        høyde = int(høyde_input)
    except:
        print("Feil! Skriv inn et heltall for høyde!")
        continue
    try: 
        vekt = int(input("Angi vekt i kg: "))
    except:
        print("Feil! Skriv inn et heltall for høyde!")
    
    print("BMI:", round(vekt/(høyde/100)**2, 1))
        
print("Takk for nå.")
