person = "Taylor Swift"
print(type(person))

p1 = person.upper()
print("p1", p1)

print("ay" in person)

print("foo" + "bar")

file_name = "wombat.py"
print(file_name.removesuffix('.py'))

print(file_name.endswith('.py'))
#             1
#   012345678901
#  "Taylor Swift"
print(person)
print(person.find('ay'))
print(person.find('wombat'))
print(person.find('Swift'))
print(person.count('t'))
print(person.count('T'))
print(person.lower().count('t'))
print(person.replace('Swift', 'Slow'))
names = person.split()  # split on any space or tab
print(names)
record = "a:b:c"
#print(record.split(':'))

fields = record.split(':')
print(fields[0], fields[1])




m = "wombat\n"
m2 = m.rstrip('\n')
m3 = m.rstrip()
value = "$123.45"
print(value.lstrip('$'))





