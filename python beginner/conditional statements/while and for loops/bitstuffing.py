st=input("enter the frame:")
count=0
res=""
for i in st:
    if i==1 and count<5:
        res+=1
        count+=1
    elif i=='':
        pass
    else:
        res+=i
        count=0
    if count==5:
        res=res+0
        count=0
print("frame after bit stuffing:",res)