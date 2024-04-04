step = int(input("Enter the step value : "))
file1 = open("out4c.txt","w+")
for i in range(0,26,step):
    file1.write(f"{chr(i+65)} ")

file1.seek(0)
text = file1.read()
print(text)