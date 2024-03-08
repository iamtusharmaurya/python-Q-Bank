# Python Program to Print All Odd Numbers in a Range

lower=int(input("enter the a number: "))

upper=int(input("enter the b number:"))

print("list of odd numbers")

for i in range(lower,upper+1):
    if(i%2 != 0):
        print(i)
        
        

        