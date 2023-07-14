k=int(input("Enter the list of numbers you want to enter"))
L2=[]
for i in range(k):
    k1=int(input(f"Enter the {i} numbers"))
    L2.append(k1)
if(len(set(L2))==len(L2)):
    print("True")
else:
    print("False")
