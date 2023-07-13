k=input("Enter the string 1")
k1=input("Enter the string 2")
p=len(k)
p1=len(k1)
g=k[0]+k1[0]+k[p//2]+k1[p1//2]+k[p-1]+k1[p1-1]
print("The string formed from k and k1's first,mid and last character is ",g)
