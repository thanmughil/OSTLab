ip = input("Enter the original string : ")
temp = "@###"
str1 = input("Enter the string to be replaced : ")
str2 = input("Enter string to replace with : ")

print(f"Modified String : {ip.replace(str1,temp).replace(str2,str1).replace(temp,str2)}")