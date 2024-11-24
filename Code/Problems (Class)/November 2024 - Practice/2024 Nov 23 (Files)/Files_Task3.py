# Task 3: wap to read filename from user and then display that file data

fname = input("Enter file name with extension: ")

file = open(fname,'r')
data = file.read()
print(data)
file.close()