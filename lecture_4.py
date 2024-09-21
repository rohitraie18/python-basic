#Dictionary and set


dict = {
    "name" : "Ram",
    "class" : 12,
    "sub" : ["python", "java", "css"],
    "marks" : [90, 88, 94]
}
print(dict)
print(dict["name"])
print(dict["marks"])
print(dict["class"])
print(dict["sub"])


student = {
    "name" : "Roman",
    "subject" : {
        "phy" : 90,
        "chem" : 95,
        "math" : 97
    }
}
#print(student)
print(student["subject"])
print(student["subject"]["math"])

student = {
    "name" : "Roman",
    "subject" : {
        "phy" : 90,
        "chem" : 95,
        "math" : 97
    }
}

print(student.keys())
print(len(student))
print(list(student.keys()))
print(len(list(student.keys())))

print(student.values())

print(student.items)

print(student["name"])  #print(student.get("name"))


student.update({"city" : "KTM"}) 
print(student)


new = {"city" : "PKR"} #  student.update({"city" : "KTM"}) 
 student.update(new)    #print(student)
print(student)                       

collection = { 1,2,3,2, "Hello", "hello"}
print(collection)
print(type(collection))
print(len(collection))
