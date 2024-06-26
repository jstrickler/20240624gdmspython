# a tuple is a fixed collection of related objects

person = "Bill", "Gates", "Microsoft", "1955-10-24"

print(f"{person[0] = }")
print(f"{person[1] = }")

first_name, last_name, product, dob = person  # iterable unpacking
# first_name = person[0]
# last_name = person[1]

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]
print(f"{people[0] = }")
print(f"{people[0][1] = }")
print(f"{people[0][1][2] = }")
print(f"{people[8][3] = }")
print()

for person in people:
    print(person)  # person[0]  person[1]
print('-' * 60)

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, product, dob)

print(f"{person = }")
print(f"{'git' in person = }")

person = "Weird Al Yankovich"
print(f"{'Yank' in person = }")

a = 'foo'
b = 'bar'
print(a + b)

print('-' * 60)

print(f"{[True] * 10 = }")

print([1,2,3] * 5)





