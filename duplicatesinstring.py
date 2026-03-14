<<<<<<< HEAD
text = input("enter text: ")
seen = ""
duplicates = ""

for char in text:
    if char in seen:
        if char not in duplicates:
            duplicates += char
    else:
        seen += char

=======
text = input("enter text: ")
seen = ""
duplicates = ""

for char in text:
    if char in seen:
        if char not in duplicates:
            duplicates += char
    else:
        seen += char

>>>>>>> 6bff3f60cc967a09480ce1bafc968610e1e65067
print(duplicates)