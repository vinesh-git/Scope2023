list=['hello','sita','this','auto']
s=[]
v=['a','e','i','o','u']
for i in list:
    if i[0] in v:
        s.append(i)
print(s)