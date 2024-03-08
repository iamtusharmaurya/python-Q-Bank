n=121
temp=n
rev=0
while(n>0):
    dig=temp%10
    rev=rev*+dig
    temp=temp//10
if(temp==rev):
    print("number is pailaindrom")
else:
    print("number is not pailaindrom")    
    