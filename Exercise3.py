List1=[]

def sum1(args):
    sum11=0
    for i in args:
        sum11+=i
    print('The sum of all the numbers in', List1 ,"is",sum11)
def avg(args):
    sum1=0
    count=0
    for i in args:
        sum1+=i
        count=count+1
    avg1=sum11/count
    print('The avg of all numbers in',List1,"is",avg1)
    
def maxi(args):
   print('The max of all numbers in',List1,"is",max(args))
def mini(args):
    print('The max of all numbers in',List1,"is",min(args))

k=True
while k:
    k1=input("Enter a number")
    if(k1.lower()=="exit"):
        k=False
        break
    try:
        k1=int(k1)
        List1.append(k1)
    except:
        print("Enter the valid number")
print(tuple(List1))
dict1={
    1:sum1,
    2:avg,
    3:maxi,
    4:mini}
for i in dict1:
    print(tuple(List1))
    dict1[i](tuple(List1))
