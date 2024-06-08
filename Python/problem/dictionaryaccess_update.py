

d={"name":"john",'age':30,"city":"newyork"}


print(d)
d["name"]=input()
d["age"]=int(input())
d["city"]=input()

for i,j in d.items():

    print(i,j)