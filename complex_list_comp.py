fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

# most concise
f1 = [f.upper() if f.startswith('a') else (f.title() if f.startswith('p') else f) for f in fruits]

print(f"{f1 = }\n")

#-----------
# most flexible
f2 = []
for f in fruits:
    if f.startswith('a'):
        f2.append(f.upper())
    elif f.startswith('p'):
        f2.append(f.title())
    else:
        f2.append(f)

print(f"{f2 = }\n")

#----------
# easiest to read (?)
f3 = []
for f in fruits:
    match f[0]:
        case 'a':
            f3.append(f.upper())
        case 'p':
            f3.append(f.title())
        case _:  # default
            f3.append(f)
print(f"{f3 = }\n")

