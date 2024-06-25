print("hello lecture 3")

marks=[90, 60.6, 70.1, 80]
print(type(marks))
print(marks[3])

student=["Rohit Rai", 77, "Delhi"]
print(student[0])
print(student[2])
student[0]="Rohan Sth"
print(student[0])

#list Slicing
marks=[10,30,55,77,11,100]
a=marks[0:5]
print(a)
print(marks[:6])
print(marks[:])
print(marks[-6:-1])

#list Methods( also sting )
list=[2,1,3]
"""
#list.append(5) #add the number [2,1,3,5]
#print(list)

list.sort() #ascending oredr [1,2,2]

list.sort(reverse=True) #descending order [3,2,1]

list.reverse() #for reserse [3,1,2]

list.insert(1,5) #[2,5,1,3]
print(list)


a=['a','c','d','b','f','e','h','g']
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a.insert(0,'A')
print(a)
"""

#list.remove(1)  #remove  [2,3]

list.pop(0)  #delete  [1,3]
print(list)

list.
