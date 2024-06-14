"""
num=int(input("Enter any number :"))

if(num %2==0):
    print("This number is even")
    if(num>0):
        print("This number is positive")
    elif(num<0):
           print("This number is negative")

elif(num %2!=0):
    print("This number is odd")
    if(num>0):
        print("This number is positive")
    elif(num<0):
        print("This number is negative")
    
else:
     print("This number is zero")
     """

num=int(input("Enter any number :"))

if(num>0):
    print("This number is positive")
    if(num %2==0):
        print("This number is even")
    else:
        print("This number is odd")

elif(num<0):
    print("This number is negative")
    if(num%2==0):
        print("This number is even")
    else:
        print("This number is odd")

else:
    print("This number is zero")