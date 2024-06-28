FILE_PATH = "DATA/words.txt"
MIN_LENGTH = 10

with open(FILE_PATH) as words_in:
    count = 0
    for raw_line in words_in:
        word = raw_line.rstrip()
        if len(word) > MIN_LENGTH:
            print(word)
            count += 1
print(f"There were {count} words at least {MIN_LENGTH} letters long")