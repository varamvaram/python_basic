""" Read a file into dictionary """
DICT = {}

with open("dict1.txt", "r", encoding="utf-8") as d:
    for i in d:
        (k, v) = i.split()
        DICT[str(k)] = v

print(DICT)
