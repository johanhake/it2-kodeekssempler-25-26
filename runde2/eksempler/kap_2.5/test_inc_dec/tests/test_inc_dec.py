# test_inc_dec.py
from ..src import inc_dec    # Koden som skal testes

def test_increment():
    assert inc_dec.increment(3) == 4

# Testen er designet til å feile for å demonstrere feiling.
def test_decrement():
    assert inc_dec.decrement(3) == 2