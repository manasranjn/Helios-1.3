# Conditional Statements
# Simple If
# if condition:
#     # code to execute if condition is true

# a = -10
# if a>0:
#     print("Number is positive")

# If-Else
# if condition:
#     # code to execute if condition is true
# else:
#     # code to execute if condition is false

# a = 0
# if a>0:
#     print("Number is positive")
# else:
#     print("Number is negative")

# Elif
# if condition1:
#     # code to execute if condition1 is true
# elif condition2:
#     # code to execute if condition2 is true
# else:
#     # code to execute if both condition1 and condition2 are false

# a = 0
# if a>0:
#     print("Number is positive")
# elif a<0:
#     print("Number is negative")
# else:   
#     print("Number is zero")

# Match Case
# match variable:
#     case value1:
#         # code to execute if variable matches value1
#     case value2:
#         # code to execute if variable matches value2
#     case value3:
#         # code to execute if variable matches value3
#     case _:
#         # code to execute if variable does not match any of the cases

a = 0
match a:
    case 0:
        print("Number is zero")
    case 1:
        print("Number is one")
    case _:
        print("Number is not zero or one")