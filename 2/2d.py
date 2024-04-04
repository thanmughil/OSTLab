dup = money = int(round(float(input("Enter the amount : ")),0))

denomination = {500 : 0, 200 : 0, 100 : 0, 50 : 0, 20 : 0, 10 : 0, 5 : 0, 2 : 0, 1 : 0}

for d in denomination.keys():
    denomination[d] = money//d
    money %= d

print(f"Rs. {dup}:")
for  k, v in denomination.items():
    if v != 0:
        print(f"\tRs. {k} x {v}")