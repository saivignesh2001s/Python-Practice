lenl1=int(input("Enter the length of list1"))
lenl2=int(input("Enter the length of list2"))
L1=[]
L2=[]
for i in range(lenl1):
    k1=int(input(f"Enter the {i} th input for list1"))
    L1.append(k1)
for i in range(lenl2):
    k1=int(input(f"Enter the {i} th input for list2"))
    L2.append(k1)
ListA=list(set(L1))
print("The elements in L1 without repeating elements",ListA)
ListB=list(set(L2))
print("The elements in L2 without repeating elements",ListB)
ListC=list(set(ListA).intersection(set(ListB)))
print("The elements common to List A and List B is",ListC)
ListD=list((set(ListA).union(set(ListB))).difference(set(ListC)))
print("The elements present unique in the both list is",ListD)
ListD=sorted(ListD,reverse=True)
print("Descending order to print ListD is",ListD)
ListC=sorted(ListC)
print("Ascending order to print ListC is",ListC)
