text = input("enter text: ")
seen = ""
duplicates = ""

for char in text:
    if char in seen:
        if char not in duplicates:
            duplicates += char
    else:
        seen += char

print(duplicates)