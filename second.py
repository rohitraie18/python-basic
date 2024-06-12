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
 str = "I am a coder"
print(str.endswith("er"))

print("hhh")
