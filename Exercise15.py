import csv
import random
with open("C:\\Users\\saivignesh.p\\OneDrive - Mphasis\\Documents\\python basics\\Python Exercise\\mnc.csv","r+") as cs:
     k=csv.reader(cs)
     L1=[]
     L2=[]
     for k1,i in enumerate(k):
         if k1==0:
             L2.append(i)
         elif i[0] in L1 and k1>=1:
              i[0]=random.randint(0,10000)
              L2.append(i)
              L1.append(i[0])
              print(i)
         else:
              L2.append(i)
              L1.append(i[0])
              print(i)
     cs.seek(0)
     k1=csv.writer(cs,lineterminator='\n')
     k1.writerows(L2)
     cs.seek(0)
     k1=csv.reader(cs)
     for i in k1:
         print(i)
              
with open("C:\\Users\\saivignesh.p\\OneDrive - Mphasis\\Documents\\python basics\\Python Exercise\\mnc.csv","r+") as cs:
     k=csv.DictReader(cs)
     L1=[]
     L2=[]
     for i in k:
         if i["CustomerId"] in L1:
             i["CustomerId"]=random.randint(0,10000)
             L1.append(i["CustomerId"])
             L2.append(i)
         else:
             L1.append(i["CustomerId"])
             L2.append(i)
     print(L1)
     print(L2)
     cs.seek(0)
     headers=["CustomerId","CustomerName"]
     k1=csv.DictWriter(cs,headers,lineterminator='\n')
     k1.writeheader()
     k1.writerows(L2)
     cs.seek(0)
     k1=csv.reader(cs)
     for i in k1:
         print(i)
        
