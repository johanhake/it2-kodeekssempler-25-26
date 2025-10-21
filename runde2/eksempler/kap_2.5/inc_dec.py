# inc_dec.py
def increment(x):
    return x + 1

def decrement(x):
    return x - 1

if __name__ == "__main__":
    if increment(4) != 5:
        print("NOOOOOO")
    assert increment(4) == 5, "Feil i increment"
    assert decrement(4) == 3, "Feil i decrement"
    
    print("Allt gikk fint")
