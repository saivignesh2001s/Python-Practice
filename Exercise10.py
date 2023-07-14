k=int(input("Enter the length of the two lists"))
L1=[]
L2=[]
p=set()
[L1.append(int(input(f"Enter the {i} number in the first list"))) for i in range(k)]
[L2.append(int(input(f"Enter the {i} number in the second list"))) for i in range(k)]
print(L1)
print(L2)
k2=set([(t1,t2) for (t1,t2) in zip(L1,L2)])
print("The set is",k2)
