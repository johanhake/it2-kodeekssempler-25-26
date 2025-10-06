# Telle variabel som økes med 1 for hver gjentagelse
i = 0

# Variabbel som holder på summen av alle tallene. Det er denne som skal skrives ut. 
sum = 0
while sum + i < 500:
    i = i + 1
    sum = sum + i
    print(f"{sum:3}", end= " ")
    
    # Hvis jeg har skrevet ut 10 tall lager jeg en ny linje. 
    if i % 10 == 0:
        print()
