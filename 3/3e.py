ip_list = []
data_type = [int,float,str,list,tuple]

for i in data_type:
    ip_list.append(i(input(f"Enter a {i} : ")))

print(ip_list)