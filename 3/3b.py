d1 = {i:i**2 for i in range(1,6)}
d2 = {i:i**2 for i in range(3,8)}

print("Matching Items:")
for key1 in d1.keys():
    if key1 in d2.keys() and d1[key1] == d2[key1]:
        print(f"{key1} : {d1[key1]}")