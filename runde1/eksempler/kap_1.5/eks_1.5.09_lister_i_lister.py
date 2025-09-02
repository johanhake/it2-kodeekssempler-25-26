import copy

# Dag 1: Oslo, Bergen og Trondheim
# Dag 2
# Dag 3
temperaturer = [
    [22, 20, 18],
    [21, 20, 20],
    [17, 17, 17],
]

for dag in temperaturer:
    print(dag, type(dag))
    # for by in dag:
    #     print(f"{by:>4}", end="")
    # print()

# Kopierer den YTTRE listen, grunn kopi
grunn_kopi = temperaturer.copy()

# Kopierer ALLE listene, dyp kopi
dyp_kopi = copy.deepcopy(temperaturer)
temperaturer[1][2] = 19  # Endrer temp i Torndheim dag 2

print("Original:\n", temperaturer)
print("Grunn kopi:\n", grunn_kopi)
print("Dyp kopi:\n", dyp_kopi)