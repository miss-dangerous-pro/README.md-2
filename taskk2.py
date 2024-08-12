#structuring python programs
#one statement in one line
print('Welcome to Geeks for Geeks')  
# Multiple Statements per Line
a = 10; b = 20; c = b + a 

print(a); print(b); print(c) 
# Implicit Line Continuation
# list example
my_list = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]

print(my_list) 
# Example 2 
# The following code is also valid 
x = (
    1 + 2
    + 5 + 6
    + 10
)

print(x)
# Dictionary Example:
my_dict = {
    'one': 1,
    'two': 2,
    'three': 3
}

print(my_dict)
# Explicit Line Continuation
x = 1 + 2 + 3 + 4 + 5 \
    + 6 + 7 + 8 + 9 + 10

print(x)
