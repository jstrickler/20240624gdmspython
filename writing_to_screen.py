value = 2.34893093
person = "Taylor Swift"
city = "Nashville"

print(value, person, city)
print("next line")
print(value, end=" ")
print(person)
print(value, person, city, sep="/")
print(value, person, city, sep="//")

# Nashville: Taylor Swift

# f-strings first appeared in 3.6

print(f"{city}: {person}")  
print(f"2 + 2 is {2 + 2}")
print(f"length of person is {len(person)}")
print("length of person is {}".format(len(person)))

x = f"{city}: {person}"

print(f"{value}")
print(f"{value:.3f}")
print("{:.3f}".format(value))

print(f"{value = }")
print("value = {}".format(value))
print(f"{value = }")
print(f"value = {value}")

animal = "wombat\t'pangolin'\n"
print(animal)
print(repr(animal))
print(f"{animal =}")






