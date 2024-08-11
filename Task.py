# How to check if a string is a valid keyword or not?
import keyword

words = ["continue","break","string","three","Name","base","example","Number","global","local","lambda","for","while"]

for i in range (len(words)):
    if keyword.iskeyword(words[i]):
        print(words[i],"is a keyword in python")
    else:
        print(words[i],"is not a keyword in python")
#How to assign values to variables in Python and other languages
a=4
b=6
c=2
d=b*a+c
print(d)
# variables in one line 
a=b=c=9
print(a)
print(b)
print(c)
#How to print without newline in Python
print("hello!",end="")
print("orwa here!",end="")
print("whassup?","")
#Basic calculator program using Python
print("Select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()

if operation == "1":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print ("The sum is"+  str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("The diffrence is"+  str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("The product is"+  str(int(num1) * int(num2)))  
elif operation == "4":
    num1 = input("Enter first number:")
    num2 = input("Enter second number:")
    print("The result is"+  str(int(num1) / int(num2)))    
else:
    print("Invalid Entry")
    #Decision making
num = 20 

if num>0:
    print(num , "is positive")
elif num>10:
    print(num,"is greater than 10")
elif num==0:
    print(num,"is zero") 
else:
    print(num,"is negative")

    # local and global variables
# local are defined inside the function 
# global are defined outside the function 
x = 10 #global variable 
def my_function():
    y = 5 # local variable
    print(y)
my_function()
print(x)

# in order to change the value of global variable
x = 10 #global variable 
def my_function():
    global x
    x = 4
    y = 5 # local variable
    print(y)
my_function()
print(x)
