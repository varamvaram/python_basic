"""Removes the first item from a specified list.
   lst: The input list.
   The modified list with the first item removed.
"""
# simple program
# LIST = [5,8,7,4]
# LIST.pop(0)
# print(LIST)
def remove_first_item(lst):
    lst.pop(0)
    return lst

# Example usage
MY_LIST = [1, 2, 3, 4, 5]  # Replace with your list
MODIFIED_LIST = remove_first_item(MY_LIST)
print("Modified list:", MODIFIED_LIST)
