"""# Opening the file in read mode
Reading the content of the file
Printing the content of the file
Creating a list and appending the content of the file to it
"""
ans = []
with open("python.txt", "r", encoding="utf-8") as file:
    re_file = file.read()
    print(re_file)
    ans.append(re_file)

print(ans)
