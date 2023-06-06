"""Place the "PYTHON.txt" file in the same directory as this Python script.
 Run the script, and it will generate a new file "PYTHON1.txt" with 
 the extracted alphanumeric characters.
 """
with open("PYTHON.txt", "r", encoding="utf-8") as file_head:
    rec = file_head.read()

with open("PYTHON1.txt", "w", encoding="utf-8") as file_write:
    for a in rec:
        if not a.isdigit():
            print(a, end=' ')
            file_write.write(a)
