a={"Brand":"Vivo","Model":"Y27 5G","Price":25000}
print(a)
for i in a:
    print(i) #Methods of retriving value 

for i in a.keys():
    print(i)
for i in a:
    print(a[i])


for i in a.values():
    print(i)
b=a.copy()
print(b)
c=dict(a)
print(c)
