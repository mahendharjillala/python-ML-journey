from nis import match


def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y

def div(x,y):
    return x/y



x=int(input("Enter First number: "))
y=int(input("Enter Second number: "))

operation=int(input("Select operation 1-> add,  2-> sub  , 3-> mul  , 4-> div ::: "))

if operation==1:
    print(add(x,y))
elif operation==2:
    print(sub(x,y))
elif operation==3:
    print(mul(x,y))
elif operation==4:
    if y == 0:
        print("Cannot divide by zero")
    else:
        print(div(x, y))
else:
    print("enter values within range")

#
# match operation:
#     case 1:
#         print(x + y)
#
#     case 2:
#         print(x - y)
#
#     case 3:
#         print(x * y)
#
#     case 4:
#         if y == 0:
#             print("Cannot divide by zero")
#         else:
#             print(x / y)
#
#     case _:
#         print("Enter values within range")
#
