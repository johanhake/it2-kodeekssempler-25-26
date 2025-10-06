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
    
    bmi = vekt/(høyde/100)**2
    if bmi <= 18.4:
        hva = "Undervektig"
    elif bmi >= 25:
        hva = "Overvektig"
    else:
        hva = "Normalvektig"
    print(f"BMI: {bmi:.1f} ({hva})" )
        
print("Takk for nå.")
