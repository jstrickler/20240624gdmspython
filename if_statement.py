
value = 39
m = 47

if value > 75:   # if elif else try except finally while for def class with
    print("kangaroo")
    print("koala")
    if value > 85:
        print("kowabunga!")
elif value > 50:  # else if
    print("wallaby")
    print("wombat")
elif 47:
    print('weird')
else:
    print('nothing else matched')

print("ALL DONE")

debug = False

# CONDITION?VALUE1:VALUE2 C/C++/Java/C# etc etc
# VALUE1 if CONDITION else VALUE2
# print_message("red" if debug else "blue")


#  == != > < >= <=  is 

m = None  # NoneType
n = None
p = None
if m is None:  # not m == None
    print("whoopsie")

print(m is None)
print(m is n)
print(n is p)
print(m is p)

# = assignment
# == equality
# := assignment ...  (aka walrus)

name = "Bob"
count = 0
print('-' * 60)

# if x := some_function():
#     print('ok')

a = [1, 2, 3]
b = a # b is not a new list
c = [1, 2, 3]  # c IS a new list
d = list(a) # new list
e = a[::]  # entire slice
print(a == b)
print(a is b)
print(a == c)
print(a is c)

x = "hello"
y = "hello"
print(x is y)
a.append("wombat")
print(f"{a = }")
print(f"{b = }")
print(f"{a == b = }")
print(f"{a is b = }")

print(f"{id(a) = }")
print(f"{id(b) = }")
print(f"{id(c) = }")

# a is b
# id(a) == id(b)

#  and or not

#  x and y
#  x or y

# x = arg or 100







