head=input("enter character that represents the starting delimeter")
tail=input("enter character that represents the ending  delimeter")
st=input("enter the character to be stuffed")
res=head
for i in st:
    if i==head or i==tail:
        res=res+i+i
    else:
        res=res+i
res=res+tail
print("frame after character stuffing:",res)