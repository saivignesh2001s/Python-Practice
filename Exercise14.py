with open("C:\\Users\\saivignesh.p\\OneDrive - Mphasis\\Documents\\python basics\\Python Exercise\\good.txt") as f:
     k=f.read()
     countchar=0
     countnum=0
     countspl=0
     dict1={}
     for i in k:
         if(i.isdigit()):
             countnum+=1
         elif(i.isalpha()):
             countchar+=1
             if(i in dict1):
                 dict1[i]=dict1[i]+1
             else:
                 dict1[i]=1
         elif(i!=' ' and i!='\t' and i!='\n'):
             countspl+=1
             print(i)
     print("Number of characters symbols and numbers in text file",countnum+countspl+countchar)
     print("Number of characters",countchar)
     print("Number of numbers",countnum)
     print("Number of symbols",countspl)
     k4={key:value for key,value in sorted(dict1.items(),key=lambda ele:ele[0])}
     print("Alphabetically lexical order\n",k4)
     k3={key:value for key,value in sorted(dict1.items(),key=lambda ele:ele[1],reverse=True)}
     print("Descending order of counts",k3)
     
     
