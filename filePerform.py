file = open("demo.txt",'w')
file.write("this is for assignment")
print("file write finished")
file.close()

file = open("demo.txt",'r')
print(file.read())
print("file read finished")
file.close()