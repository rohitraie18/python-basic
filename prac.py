'''
# Code here
#a=int(input("Enter any number"))

#if (a<2):
 #   print("Neither prime nor composite")

#elif(a)

# Function to check if a number is prime
x=int(input("Enter ant number :"))
    # Numbers less than 2 are not prime
if (x < 2):
     print("Neither prime nor composite")
    
elif(x ** 0.5) + 1):
    print("prime")
      #  if number % i == 0:
          #  return False
else:
    print("Not prime")
'''

n = int(input("Enter any number"))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}.")
