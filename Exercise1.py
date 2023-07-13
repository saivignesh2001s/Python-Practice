'''Using if else condition only'''
print("Finding second max only using if else")
i:int=int(input("Enter the first number"))
j:int=int(input("Enter the second number"))
k:int=int(input("Enter the third number"))
l:int=int(input("Enter the fourth number"))
if((j<i and j>k and j>l) or(j>i and j<k and j>l) or (j>i and j>k and j<l)):
    print(j ,"is the second largest number")
elif((i<j and i>k and i>l) or(i>j and i<k and i>l) or (i>j and i>k and i<l)):
    print(i ,"is the second largest number")
elif((k<i and k>j and k>l) or(k>i and k<j and k>l) or (k>i and k>j and k<l)):
    print(k ,"is the second largest number")
else:
    print(l ,"is the second largest number")

'''Using list'''
k1=[i,j,k,l]
k1=sorted(k1,reverse=True)
print(k1[1])
