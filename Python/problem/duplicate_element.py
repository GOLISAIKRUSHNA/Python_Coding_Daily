

li=[10,20,30,20,40,10,50]

new=[]
for i in range(0,len(li)):
    for j in range(i+1,len(li)):

        if(li[i]==li[j]):
            # li.remove(li[j])
            # print(li)
            print("duplicate values:",li[j],end="" ) 

            
           
for x in li: 
    if(x not in new):
        new.append(x)

print("\nunique element are:",new)









