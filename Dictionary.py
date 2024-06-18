#It include key and Meaning
#eg: key,value

dict1={

    "Name":"Abdul Hameed",
    "Email":"ah_val@yahoo.com",
    "Phone":123456

}
a=dict1["Name"]
dict1["Name"]="Babu"
print(dict1)

for x in dict1:
    print(x)
    print(dict1[x])
for x,y in dict1.items():
    print(x,y)
dict1["age"]=35
print(dict1)
dict1.pop("age")
print(dict1)