import os

starting_folder = "."

GIT = ".git"

#  folder, subfolders, filenames = os.walk(starting_folder)
for folder, subfolders, file_names in os.walk(starting_folder):
    if GIT in subfolders:
        subfolders.remove(GIT)  # skip recursing into .git
    # print(folder)
    for file_name in file_names:
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder, file_name)
            if 'egg-info' in file_path:
                continue
            file_size = os.path.getsize(file_path)
            print(f" {file_size:8} {file_path}")
