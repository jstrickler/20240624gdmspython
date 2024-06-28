import os
from datetime import datetime

FILE_FOLDER = "DATA"
FILE_NAME = "alice.txt"

# os.listdir('folder-name')

file_path = os.path.join(FILE_FOLDER, FILE_NAME)
print(f"{file_path = }")

print(f"{os.path.exists(file_path) = }")

print(f"{os.path.dirname(file_path) = }")
print(f"{os.path.basename(file_path) = }")
print(f"{os.path.abspath(file_path) = }")

file_size = os.path.getsize(file_path)
print(f"{file_size = }")
raw_ts = os.path.getmtime(file_path)
print(f"{raw_ts = }")
file_ts = datetime.fromtimestamp(raw_ts)
print(f"{file_ts = }")

print(f"{os.path.isdir(file_path) = }")
print(f"{os.path.isfile(file_path) = }")

