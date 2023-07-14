print("List and Dictionary")
Headings=["first_name","last_name","age"]
Person1=["Mark","Taylor",20]
Person2=["Emma","Jones",30]

k2=[]
for t1,t2,t3 in zip(Headings,Person1,Person2):
    k1=[]
    k1.extend((t2,t3))
    print(k1)
    k3=[]
    k3.extend((t1,k1))
    print(k3)
    k2.append(k3)
    
    
print(dict(k2))
