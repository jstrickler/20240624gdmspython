import sys
import os
import geometry   # find and load geometry.py

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

# module search:
# 1. current folder
# 2. folders in PYTHONPATH 
# 3. standard location (sys.prefix/lib/...)
print(f"{sys.prefix = }\n")
print(os.listdir(os.path.join(sys.prefix, 'lib', 'python3.11', 'site-packages')))
print('-' * 60)
for path in sys.path:
    print(path)
