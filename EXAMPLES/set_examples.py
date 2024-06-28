


colors1 = ['red', 'blue', 'green', 'purple', 'green']  # create literal set
colors2 = ['green', 'blue', 'yellow', 'orange']
set1 = set(colors1)
set2 = set(colors2)

set1.add('taupe')  # add element to set (ignored if already in set)
set1.add('taupe')  # add element to set (ignored if already in set)
set1.add('taupe')  # add element to set (ignored if already in set)
set1.add('taupe')  # add element to set (ignored if already in set)
set1.add('taupe')  # add element to set (ignored if already in set)
set1.add('taupe')  # add element to set (ignored if already in set)

print(f"{set1 = }")
print(f"{set2 = }")
print(f"{set1 & set2 = }")  # intersection -- common items
print(f"{set1 ^ set2 = }")  # XOR -- non-common items (in one set but not both)
print(f"{set1 | set2 = }")  # union -- unique combination of both sets
print(f"{set1 - set2 = }")  # difference -- Remove items in right set from left set
print(f"{set2 - set1 = }")
print()

with open('../DATA/breakfast.txt') as breakfast_in:
    food = breakfast_in.read().splitlines()

unique_food = set(food)  # Create set from iterable (e.g., list)
print(f"{food = }\n")
print(f"{sorted(unique_food, key=str.lower) = }\n")

print()

my_set = {'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'ham', 'spam', 'spam'}
print(f"{my_set = }\n")
