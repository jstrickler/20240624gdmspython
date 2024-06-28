import os
from glob import glob

FOLDER = "DATA"

files_to_process = []
for file_name in os.listdir(FOLDER):
    file_path = os.path.join(FOLDER, file_name)
    if os.path.isfile(file_path):
        files_to_process.append(file_path)

print(f"{files_to_process = }\n")
print('-' * 60)

files = glob('DATA/*.txt')
print(f"{files = }\n")

