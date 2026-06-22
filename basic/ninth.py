# make a program to check whether the number 
# input by user is even or odd

# functions
# built in functions
# print()
# to reuse our logic 
# definition (def) 
# call
# code more readable and scalable


def evenhai(x):
    if(x%2==0):
        print('even')
    else:
        print('odd')



evenhai(8)

# parameter and argument


# make a function of sum

evenhai(9)


# def opoftwoplusfive():
#    print(2+5)


# call
# opoftwoplusfive()

# def is_even_or_odd():
#     num=int(input('Enter the number? '))
#     if num%2==0:
#         print('even')
#     else:
#         print('odd')



# is_even_or_odd()

# square_pattern()
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# def square_pattern():
#     i=1
#     while(i<=5):
#         j=1
#         while(j<=5):
#             print('*',end=' ')
#             j=j+1
#         print()
#         i=i+1

# square_pattern()

# right_angle_pattern()
# *
# * *
# * * *
# * * * *
# * * * * *

# reverse a number
# 123->321


# parameter ,arguments

# parameter-> the value which is passed to function definition
# argument-> the actual value which will be passed to function during call


# def is_even_or_odd(num):
#     if num%2==0:
#         print('even')
#     else:
#         print('odd')


# num=int(input('Enter the number? '))
# is_even_or_odd(num)

# return

# def mul(a,b):
#      return a*b

# print(mul(9,8))


# reusable
# +,-,*,/
# make sum fn,sub fn, mul fn, div fn 
# calculate program should be reusable 


def sum(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    if num2==0:
        return 'Infinity'
    else:
        return num1/num2

def calc():
    num1=float(input('enter number first: '))
    num2=float(input('enter number second: '))
    op=input('Enter the operator')

    if op=='+':
        print(sum(num1,num2))
    elif op=='-':
        print(sub(num1,num2))
    elif op=='*':
        print(mul(num1,num2))
    elif op=='/':
        print(div(num1,num2))
    else:
        print("Enter a valid operator")
        
calc()







