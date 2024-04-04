num = int(input("Enter a number : "))

def prime(num):
    for i in range(2,(num//2)+1):
        if num%i == 0:
            return -1
    return num

primeCount = 0
for i in range(2,num+1):
    if prime(i) != -1:
        primeCount += 1
print(primeCount)