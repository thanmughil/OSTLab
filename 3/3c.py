ip = [(i,i+1,i+2) for i in range(5)]

result = [sum(i) for i in ip]
print("Sum of tuple items :",result)