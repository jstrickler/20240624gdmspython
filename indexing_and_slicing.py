fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{fruits[0] = }")
print(f"{fruits[17] = }")
print(f"{fruits[21] = }")
print(f"{fruits[-1] = }")  #  fruits[len(fruits)-1]
print(f"{fruits[-5] = }")

#  LIST[start-at:stop-before]
print(f"{fruits[0:4] = }")
print(f"{fruits[12:15] = }")
print(f"{fruits[-5:len(fruits)] = }")
print(f"{fruits[:4] = }")
print(f"{fruits[-5:] = }")

s = "Sasquatch"
print(f"{s[2:7] = }")
print(f"{s[:3] = }")
print('-' * 60)

for fruit in fruits:
    print(fruit)
print()

# for VAR in ITERABLE:
#    VAR = ITERABLE[0]
#    VAR = ITERABLE[1]
#   ...

# for VAR, ... in ITERABLE:
#   ...

for fruit in fruits:
    print(fruit[:3].title())
print('-' * 60)

for i, fruit in enumerate(fruits, 1):
    print(i, fruit)






