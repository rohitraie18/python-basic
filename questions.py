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

#8 WAP to check if a number entered by the user is odd or even.
number=float(input("Enter ant number :"))
if(number %2==0):
    print("This number is even")
else:
    print("This number is odd")

#9 WAP to check if a number entered by the user is odd or even or positive or negative.
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
#10 WAP to find the greatest of 3 numbers entered by the user.
a=int(input("Enter 1st number :"))
b=int(input("Enter 2nd number :"))
c=int(input("Enter 3rd number :"))

if(a>b and a>c):
    print(a,"is greater number")

elif(b>a and b>c):
    print(b,"is greater number")

elif(c>a and c>b):
    print(c,"is greater number")

#11 WAP to check if a number is a multiple of 7 or not.
a=int(input("Enter any number :"))

if(a%7==0):
    print("This number is multiple of 7")

else:
    print("This number is not multiple of 7")

#12 WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
"""
movies=[]
mov=input("Enter first movie name :")
mov1=input("Enter second movie name :")
mov2=input("Enter third movie name :")
movies.append(mov)
movies.append(mov1)
movies.append(mov2)
print(movies)
"""

movies=[]
movies.append(input("Enter 1st movie :"))
movies.append(input("Enter 2nd movie :"))
movies.append(input("Enter 3rd movie :"))
print(movies)

#13WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
list=[1,2,1]
a=list.copy()
a.reverse()

if(list==a):
    print("Palindrome")

else:
    print("Not Palindrome") 




#14 WAP to count the number of students with the “A” grade in the following tuple.
#[”C”,“D”,“A”,“A”,“B”,“B”,“A”]
list=("A", "B", "A", "C", "A")
a=list.count("A")  #print(list.count("A"))
print(a)

#15 Store the above values in a list & sort them from “A” to “D”
list=["A", "C", "D", "B", "A"]
list.sort()
print(list)
