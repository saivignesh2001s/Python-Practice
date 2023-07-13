l=['abc', 'xyz', 'aba', '1221']
count=0
for i in l:
    if(len(i)>=2 and i[0]==i[len(i)-1]):
        count+=1
print("Strings with two or more characters or first and last characters are same",count)
