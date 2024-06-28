from pprint import pprint

knight_info = {}  # create empty dict

with open("../DATA/knights.txt") as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(":")
        knight_info[name] = title, color, quest, comment  # create new dict element with name as key and a tuple of the other fields as the value

pprint(knight_info, sort_dicts=False)
print()

#for  key, value in DICT.items()
for wombat, kazoo in knight_info.items():
    print(kazoo[0], wombat)

print()
print(knight_info['Robin'])
print()
print(knight_info['Robin'][2])
