fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

enum_fruits = enumerate(fruits)  # iterator! (AKA generator)
print(f"{enum_fruits = }")
for index, fruit in enum_fruits:
    print(index, fruit)  
print('-' * 60)

enum_fruits = enumerate(fruits)  # iterator! (AKA generator)
print(list(enum_fruits))

print('-' * 60)

reversed_fruits = reversed(fruits)
for fruit in reversed_fruits:
    print(fruit)

print('-' * 60)

# for index, fruit in reversed(enumerate(fruits)):
#     print(index, fruit)

for i in range(5):
    print(i)
print()
for i in range(1, 11):
    print(i, end=", ")
print('\n')



