print("Hello questions")
#1 WAP to input two numbers and print their sum.
first=int(input("Enter 1st number :"))
second=float(input("Enter 2nd number :"))
sum=first+second
print("Sum=", sum)   #print(first+second)

#2 WAp to input side of a square and print its area.
L=float(input("Enter length of square:"))
area=L**2
print("area of square is :", area)

#3 Wap to input 2 floating numbers and print their average.
firstnum=float(input("Enter 1st number :"))
secondnum=float(input("Enter 2nd number :"))
a=firstnum+secondnum    #average=(firstnum + secondnum)/2
average=a//2
print("Total average=", average)

#4 Wap to input 2 int numbers a and b. Print True if a is greater or equal to b. If not print False.
a=int(input("Enter 1st num:"))
b=int(input("Enter 2nd num:"))
print(a>=b )

#5 WAP to input users first name and print its length.
name=input("Enter name:")
len1=len(name)
print(len1)

#6 WAP to find the occurrence of '$' in a string.
sentence="Hi I an $ a student $ hellow my $ friend $ We are $ a friend"
print("count number is :", sentence.count("$"))

#7 Input marks and print they are pass or fail using conditional statements.
marks=float(input("Enter your exam marks :"))
if(marks>=40):
    print("congratulations you are pass!!")
    if(marks>100):
        print("Not possible!!")
elif(marks<40):
    print("Sorry You are fail!!!")

