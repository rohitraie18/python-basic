#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
list=['a', 'b', 'c', 'b',]

copy_list=list.copy()
copy_list.reverse()

if(copy_list==list):
  print("palindrome")

else:
  print("Not palindrom")
 