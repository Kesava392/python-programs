<<<<<<< HEAD
#open and writing file
file=open("filehandling.py","w")
file.write("Name:Kesava\n")
file.write("Course:PYTHON\n")
file.close()
#reading the file
file=open("filehandling.py","r")
print(file.read())
file.close()
#appending new data
file=open("filehandling.py","a")
file.write("Status:Learning Python")
file.close()
#reading after appending new data
file=open("filehandling.py","r")
print(file.read())
file.close()

=======
#open and writing file
file=open("filehandling.py","w")
file.write("Name:Kesava\n")
file.write("Course:PYTHON\n")
file.close()
#reading the file
file=open("filehandling.py","r")
print(file.read())
file.close()
#appending new data
file=open("filehandling.py","a")
file.write("Status:Learning Python")
file.close()
#reading after appending new data
file=open("filehandling.py","r")
print(file.read())
file.close()

>>>>>>> 6bff3f60cc967a09480ce1bafc968610e1e65067
