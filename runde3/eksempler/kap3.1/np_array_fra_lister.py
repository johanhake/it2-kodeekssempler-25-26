import numpy as np

tall1 = np.array([-1, 1, 3, 5, 9])
tall2 = np.array([-2, 2, 6, 10, 14])

for i in range(len(tall1)):
    print(f"{i+1} | {tall1[i]:2} | {tall2[i]:2}")

