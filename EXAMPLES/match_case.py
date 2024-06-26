from datetime import date

sample_data = [
    "wombat",
    ["wombat", 2, 3],
    {'foo': 5, 'bar': 10},
    {'weasel': 5, 'wallaby': 10},
    "spam",
    date(2023, 12, 15),
    "ham",
    ["add", 5, 10],
    ["subtract", 25, 10],
    ("this", "is", "a", "tuple"),
    275,
    19.8,
]

for data in sample_data:
    match data:
        case "wombat":  # data is a specific string
            print("word", data)
        case str():     # data is any string
            print("any string", data)
        case {'weasel': value}:   # data is a dict with key 'weasel'
            print("weasel", data)
        case {'wallaby': value1, 'weasel': value2}:  # data is dict with keys 'weasel' & 'wallaby'
            print("weasel", data, value1, value2)
        case dict():  # data is a dict
            print("dict", data)
        case date() as date_value:  # data is datetime.date and copied to date_value
            print("year is", date_value.year)
        case ["add", value1, value2]:  # data is list whose first element is "add"
            print("add", value1 + value2)
        case ["subtract", value1, value2]:  # same as "add"
            print("subtract", value1 - value2)
        case [word, n1, n2]:  # data is 3-element list
            print("[word, n1, n2]", "word is", word,  data)
        case _:   # default
            print("NOT MATCHED", data)
print()

value = 37

# maybe not much of an improvement...
match value:
    case _ as x if x > 100:  # if x > 100:
        print("Wahoo")
    case _ as x if x > 50:   # elif x > 50:
        print("Blarf")
    case _ as x if x > 25:   # elif x > 25:
        print("Glurz")
