produkter_med_priser = [["Eple", 10], ["Banan", 8], ("Appelsin", 13)]

for frukt, pris in produkter_med_priser:
    print(f"{frukt} koster {pris}")
    
produkter = ["Eple", "Banan", "Appelsin"]
priser = [10, 8, 13]

for i in range(len(produkter)):
    print(f"{produkter[i]} koster {priser[i]}")
    
print(list(zip(produkter, priser)))

for frukt, pris in zip(produkter, priser):
    print(f"{frukt} koster {pris}")


# Bruk av zip