
file1 = input("Full Path to File: ")

# f = open('c:\\scripts\\body', 'r')
f = open(file1, 'r')

file_contents = f.read()

print (file_contents)

f.close()