print("second lecture")

#string
str1='this is a string'
str2="this is a string"
str3="""this is a string"""
print(str1)
print(str2)
print(str3)

str1="I am Rohit. \t I am from Solu."  #\t-tab
print(str1)

#concatenation
a="hello"
b="world"
print(a+b)

#length of str
str1="hello"
len1=len(str1)    #print(len(str1))
print(len1)

str2="world"
len2=len(str2)
print(len2)

final_str = str1 + " " + str2
print(len(final_str))

#Indexing  index-position
str = "kanku school"
chr = str[6]       #print(str[6])
print(chr)

#slicing
str = "Helloworld"
a = str[1 : 5]
print(a)
print(str[5: 11]) #print(str[5: len(str)])  print(str[5:])
print(str[5:])
print(str[:5]) #[0:5]

#negative index
a="Apple"
print(a[-4 : -2]) 
 
#string function
a ="i am a coder am."  
print(a.endswith("der."))
print(a.capitalize())
print(a.replace("coder","student"))
print(a.find("m"))
print(a.count("am"))

#conditional statements (if, elif, else)
"""age=18
if(age >= 18):
    print("can vote")

age=int(input("Enter age :"))
if(age>=18):
    print("can vote")
elif(age<18):
    print("not eligible")
"""
"""
 #result in greading system
marks=float(input("Enter your marks :"))
if(marks >=90 and marks <=100):
   print("Your grade is: A+")

elif(marks >=80 and marks <90):
   print("Your grade is : A")

elif(marks >=70 and marks <80):
   print("Your grade is : B+")

elif(marks >=60 and marks <70):
   print("Your grade is : B")

elif(marks >=50 and marks <60):
   print("Your grade is : C+")

elif(marks >=40 and marks <50):
   print("Your grade is : C")

elif(marks >=30 and marks <40):
   print("Your grade is : D+")

elif(marks <30):
    print("Your grade is : NG")
"""

"""
age=int(input("Enter your age :"))
if(age>=18):
   print("Can vote.")
   if(age>=70):
      print("Not possible.")
elif(age<18):
   print("Not eligible")
"""


age=int(input("Enter your age :"))

if(age >=18):
      print("can vote and drive")

      if(age >=70):
         print("Not possible")

elif(age <18):
    print("Not eligible!!")



