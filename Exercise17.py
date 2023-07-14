import csv
from decimal import Decimal
class BankAccount:
    BasicInterest=0.04
    def __init__(self):
        self._interest=0
    def CalculateInterest(self,amount_balance):
         #amount_balance=amount_balance[0:len(amount_balance)-8]
         #print(amount_balance)
         amount_balance=float(amount_balance)
         if(amount_balance<1000):
             return False
         else:
             self._interest=amount_balance*BankAccount.BasicInterest
             return self._interest
L1=[]
with open("C:\\Users\\saivignesh.p\\OneDrive - Mphasis\\Documents\\python basics\\Python Exercise\\CustomerAccountBalanceFile.csv") as cs:
     k=csv.reader(cs,delimiter=';')
     for i in k:
         L1.append(i)
         print(i)
dict1=[]
dict2=[]
for i,k in enumerate(L1):
     if(i>=1):
         k1=BankAccount()
         if(not(k1.CalculateInterest(k[1]))):
             dict11={}
             dict11["CustomerId"]=k[0]
             dict11["CurrentBalance"]=k[1]
             dict1.append(dict11)
         else:
             dict22={}
             dict22["CustomerId"]=k[0]
             dict22["InterestAmount"]=k1.CalculateInterest(k[1])
             dict2.append(dict22)

print(dict1)
print(dict2)
with open("C:\\Users\\saivignesh.p\\OneDrive - Mphasis\\Documents\\python basics\\Python Exercise\\DefaultCustomerFile.csv","w") as cs:
        headers=["CustomerId","CurrentBalance"]
        k=csv.DictWriter(cs,headers,lineterminator='\n')
        k.writeheader()
        k.writerows(dict1)

with open("C:\\Users\\saivignesh.p\\OneDrive - Mphasis\\Documents\\python basics\\Python Exercise\\InterestAmount.csv","w") as cs:
        headers=["CustomerId","InterestAmount"]
        k=csv.DictWriter(cs,headers,lineterminator='\n')
        k.writeheader()
        k.writerows(dict2)
