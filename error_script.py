FILE_PATH = "walrus_gumball.txt"

try:
    with open(FILE_PATH) as walrus_in:
        data = walrus_in.read()
except (FileNotFoundError, PermissionError) as err:
    print(err)
except Exception:  # catch ANY error
    print(err) 

print("ALL DONE!")

