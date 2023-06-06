"""
program to create a histogram from a given list of integers
"""
LENGTH = int(input("Enter the length value: "))
LST = []

for i in range(LENGTH):
    a = int(input("Enter the item: "))
    LST.append(a)

print("Histogram:")
HISTOGRAM = "* "
for i in LST:
    print(HISTOGRAM * i)
