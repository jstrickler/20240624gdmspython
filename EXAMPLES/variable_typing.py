a = " 123 " # str
b = 456   # int
# result = a + b  # raises error due to incompatible types

result = int(a) + b
print(result)

x = 5
y = 10.2
result = x + y
print(a + str(b))
print(type(a))
print(type(b))