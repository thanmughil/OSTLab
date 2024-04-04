file1 = open("./in.txt","r")
file2 = open("./out.txt","w")

file2.write(file1.read())

file1.close()
file2.close()