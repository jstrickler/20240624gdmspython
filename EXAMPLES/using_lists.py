cities = ['Portland', 'Pittsburgh', 'Peoria']
print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)
# cities.append(more_cities)
print(f"cities: {cities}\n")

#  LIST.append(obj)  LIST.insert(index, obj)  LIST.extend(iterable)



del cities[3]
print(f"cities: {cities}\n")

# push:  LIST.append()
# pop:   LIST.pop()
# shift  LIST.pop(0)
# unshift LIST.insert(0)

# collections.deque

cities.remove('Buffalo')
print(f"cities: {cities}\n")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)
print(f"city: {city}")
print(f"cities: {cities}\n")

