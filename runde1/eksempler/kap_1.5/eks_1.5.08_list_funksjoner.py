tall = [5, 3, 8, 11, 9, 3, 2]
print(f'tall: {tall}')

print('\nSum, minst og størst:')
print(f'Sum: {sum(tall)}')
print(f'Min: {min(tall)}')
print(f'Max: {max(tall)}')

from statistics import mean, median, mode
print('Gjennomsnitt, median og typetall:')
print(f'Mean: {mean(tall)}')
print(f'Median: {median(tall)}')
print(f'Mode: {mode(tall)}')