k1=True
while k1:
    k=int(input("Enter the number of elements you want"))
    if(k>3):
        k1=False
    L1=[]
    for i in range(k):
        k0=int(input(f"Enter the {i} integer"))
        L1.append(k0)
    L2=L1[0:k//3]
    L3=L1[(k//3):2*(k//3)]
    L4=L1[2*(k//3):]
    print("The reverse of the list l2 is",L2[::-1])
    print("The reverse of the list l3 is",L3[::-1])
    print("The reverse of the list l4 is",L4[::-1])
    L5=[]
    L6=[]
    [L5.extend(i) for i in (L2[::-1],L3[::-1],L4[::-1])]
    print("List extended using L2,L3,L4 is",L5)
    L6.extend((L2[::-1],L3[::-1],L4[::-1]))
    print("Combined list of l1,l2,l3 is",L6)

    
