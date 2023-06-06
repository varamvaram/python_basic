""" count number 4 in a given list""" 
INPUT_LIST = [1, 4, 2, 4, 3, 4, 5]
COUNT = 0
for num in INPUT_LIST:
    if num == 4:
        COUNT += 1

print("Number of 4's in the list:", COUNT)
