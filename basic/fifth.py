# control flow
# conditional statements if elif else

# if (5>5):
#    print('hello')
# else:
#    print('not hello')

# if (7>8):
#    print('ohho')
#    print(8+9)
# else:
#    print('woww')


# x=9
# y=4

# if (y>x):
#    print('this is a number',x)
# else:
#    print('not so cool guys')

# name=input('Enter your name: ')
# if(name=='rohit'):
#    print('trainer at madrid')
# else:
#    print('student at madrid')



# algorithms
# steps of instruction to achieve a spefic goal/task problem solve

# calculate area of rectangle take input from the user

# ek variable bnaunga length naam ka
# is variable mei input lena hai 
# ek variable breadth naam ka bnana hai
# isme input user se lena h
# fir type conversion krna hai taki arithemetic operation lg sake
# ek variable area ka bnana hai
# area ka formula use krenge
# result print krenge

# pseducode
# len=i/p--->type convert(int)
# bre=i/p--->type convert(int)
# area=len*bre
# o/p--->print()


# code develop
# length=int(input())
# breadth=int(input())
# area=length*breadth
# print(area)

# take input of age from the user and print whether he can vote in india or not

# age=int(input('Enter you age:? '))

# if (age>=18):
#     print('yes you can vote')
# else:
#     print('you can not vote')

## Problem 1: Age Eligibility and Type Conversion

# Ask the user to enter their birth year as a string. 
# Convert it to an integer and calculate their age (assume the current year is 2026). 
# Using comparison and logical operators, check if the person is both:
# 18 years or older
# Age less than or equal to 60
# Print the age and whether the person is in the “working age group”

# ip->18   op->working age g
# ip->17   op->non working
# ip->19   working
# ip-->   61 non working

# birthYear=int(input('Enter the your birth year? '))
# currentYear=2026
# age=currentYear-birthYear
# if (age>=18 and age<=60):
#     print('working age group')
# else:
#     print('non working')



## Problem 2: Shopping Bill with Discount

# Take the price and quantity of an item as input from the user. 
# Convert them to appropriate numeric types and calculate the total amount. 
# If the total amount is greater than 1000 *and* quantity is more than 5, apply a 10% discount. 
# Otherwise, print the normal total. Display final payable amount.

# hint:
#  20% of 400
#  20/100 * 400=80

# ip ,price=1000 qty=6 
price=int(input('Enter the price of each item? '))
qty=int(input('Enter the qty?: '))
totalBill=price*qty
if(price>=1000 and qty>5):
    discount=(10/100)*totalBill
    grandTotal=totalBill-discount
    print('Hurray your Grand Total is:',grandTotal)
else:
    print('sorry ',totalBill)


# Problem 3: Student Percentage and Pass/Fail Decision

# Take marks of three subjects as input (in string form).
#  Convert them into integers, calculate total and percentage using arithmetic operators.
#  Using comparison and logical operators, print whether the student has:
#  Passed (percentage ≥ 40 *and* each subject mark ≥ 33)
#  Failed otherwise
#  Also print the percentage
# hint
# percent=obtainedM/totalM*100



# i/p->25,35,65  let 100,100,100
# perc=125/300*100=41.6----->op=fail

# marks1=int(input('Enter the marks of first sub: '))
# marks2=int(input('Enter the marks of second sub: '))
# marks3=int(input('Enter the marks of third sub: '))

# obtainedMarks=marks1+marks2+marks3
# totalMarks=300

# percentage=obtainedMarks/totalMarks*100

# if(percentage>40 and marks1>33 and marks2>33 and marks3>33):
#     print('Pass',percentage)
# else:
#     print('Fail',percentage)


# a,b program->5,7--->7 is maximum


# a=int(input())
# b=int(input())
# if(a>b):
#     print(a,'is max')
# else:
#     print(b,'is max')


## Problem 4: Number Comparison with Arithmetic Result

# Ask the user to input two numbers. 
# Perform arithmetic operations (addition and multiplication). 
# Then compare:
#  Check if the sum is greater than the product *or* if both numbers are equal
#  Print appropriate messages using logical and comparison operators.



# num1=int(input())
# num2=int(input())
# addition=num1+num2
# mul=num1*num2

# if (addition>mul):
#     print('addition is greater')
# elif (addition<mul):
#     print('mul is greater')
# else:
#     print('both are equal')




## Problem 5: BMI Category Checker

# Ask the user to input their weight  and height .
#  Convert inputs to floats and calculate BMI using the formula:
# BMI = weight / (height * height)
# Using comparison and logical operators, print whether the person is:

# * Underweight (BMI < 18.5)
# * Normal (BMI between 18.5 and 24.9)
# * Overweight (BMI ≥ 25)
#   Also print the calculated BMI.




## Problem 6: Loan Eligibility

# Ask the user to input their monthly income and age. 
# Convert to integers. Using arithmetic, comparison, and logical operators determine if the user is eligible for a loan:
# Conditions:
#  Age between 21 and 60
#  Income greater than or equal to 25000
#  Print whether the person is eligible or not.


## Problem 7: Calculator with Condition Check

# Take two numbers as floats and an operator (+, -, *, /) as input.
#  Perform the corresponding arithmetic operation. 
# Before division, check using comparison operators that the second number is not zero.
#  Use logical operators where needed and print the result.



# num1=float(input())
# num2=float(input())
# op=input()

# if(op=='+'):
#     print(num1+num2)
# elif(op=='-'):
#     print(num1-num2)
# elif(op=='*'):
#     print(num1*num2)
# else:
#     if(num2!=0):
#       print(num1/num2)
#     else:
#         print('division not possible')





## Problem 8: Electricity Bill Calculator

# Ask the user to enter the number of units consumed as a string and convert it into an integer. 
# Calculate total bill:

#  First 100 units → 5 per unit
#  Next 100 units → 7 per unit
#  Remaining units → 10 per unit
#  After calculating the bill, if the total bill is more than 1500 *or* units are more than 250, add a surcharge of 5%.
#  Print total units, bill amount, and final amount after surcharge if applicable.






units=float(input('Enter the units: '))
# 180
totalBill=0

if(units<=100):
    totalBill=5*100
    print('Your bill is:',totalBill)
elif(units>100 and units<=200):
    afterHunderd=units-100
    totalBill=5*100+afterHunderd*7
    print('Your bill is:',totalBill)
else:
    afterTwoHundred=units-200
    totalBill=5*100+7*100+afterTwoHundred*10
    if(units>250 or totalBill>1500):
        surcharge=5/100*totalBill
        grandTotal=totalBill+surcharge
        print('Your bill is:',grandTotal)
    else:
        print('Your bill is:',totalBill)



## Additional New Problems

## Problem 9: Salary Hike and Tax Check

# Ask the user to enter their current salary (float) and performance rating (out of 5). 
# If rating is greater than or equal to 4 and salary is less than 80000, increase salary by 15%;
#  otherwise increase by 5%.
#  Then check using comparison and logical operators whether the new salary is taxable (greater than 50000). 
# Print old salary, new salary, and taxability status.
# ip->50000 rating=4 op=57500
# ip->80000 op=84000

# salary=float(input('enter the salary: '))
# rating=int(input('Enter the rating: '))

# hike=0
# totalSalary=0

# if(salary<80000 and rating>=4):
#     hike=15/100*salary
#     totalSalary=salary+hike
#     if(totalSalary>50000):
#         print('Taxable',salary,totalSalary)
#     else:
#         print('Non Taxable',salary,totalSalary)
# else:
#     hike=5/100*salary
#     totalSalary=salary+hike
#     if(totalSalary>50000):
#         print('Taxable',salary,totalSalary)
#     else:
#         print('Non Taxable',salary,totalSalary)





### Problem 10: Voting Booth Validator

# Take age and city name as input. Convert age to integer.
#  Using logical operators, verify that the person is at least 18 and does not live in a restricted city named "TestCity".
#  Print whether they can vote in the local booth. 
# Also print how many years are left if they are underage (use arithmetic operator).
# 43 and jaiput test=deli-->does not vote
# 23 and delhi  vote

# 17 delhi-->no 1
# 23 jaipur-->no 
# 34 delhi-->yes

# age=int(input())
# city=input()
# testCity='delhi'
# if(age>=18 and city==testCity):
#     print('You can vote locally')
# else:
#     if(age<18):
#      print('You can not vote',18-age)
#     else:
#       print('You cant vote')
    




### Problem 11: Triangle Type Finder

# Take three sides of a triangle as input (convert to floats). 
# First check if a valid triangle can be formed using comparison and logical operators
#  (sum of any two sides greater than third).
#  If valid, determine whether it is equilateral, isosceles, or scalene.
#  Also print the perimeter using arithmetic operators.

# algo
# take input side three
# check if it is triangle or not
#       scalne iso equi
# not a triangle

# make this code optimise
# side1=float(input('Enter side 1: '))
# side2=float(input('Enter side 2: '))
# side3=float(input('Enter side 3: '))


# if(((side1+side2>side3)or(side2+side3>side1)or(side3+side2>side1))and(side1!=0 and side2!=0 and side3!=0)):
#     print('Valid triangle')
#     if(side3==side2 and side1==side3):
#         print('Equilateral')
#     elif(side1==side2 or side2==side3 or side1==side3):
#         print('Isoscales')
#     else:
#         print('Scalene')
# else:
#     print('Not a valid triangle')


### Problem 12: Mobile Data Usage Bill

# Ask the user to input total data used in GB (float). 
# Convert if required. Calculate the base bill at 50 per GB. 
# If usage is greater than 10 GB and less than or equal to 25 GB, give 8% discount;
# if greater than 25 GB, give 12% discount. 
# Also add 18% tax if final amount is greater than 1000 using logical operators. Print usage and final bill.


data=float(input('Enter the data '))
totalBill=0
discount=0
if (data>10 and data<=25):
    totalBill=data*50
    discount=8/100*totalBill
    finalBill=totalBill-discount
    if(totalBill>1000):
        gst=18/100*totalBill
        gstBill=finalBill+gst
        print('bill:',gstBill)
    else:
        print('bill:',finalBill)
elif(data>25):
    totalBill=data*50
    discount=12/100*totalBill
    finalBill=totalBill-discount
    gst=18/100*totalBill
    gstBill=finalBill+gst
    print('bill',gstBill)
else:
    totalBill=data*50
    print('bill:',totalBill)

















### Problem 13: Temperature Converter and Weather Check

# Take temperature input in Celsius as a string, convert it to float,
#  and convert it to Fahrenheit using arithmetic operators.
#  Using comparison and logical operators, print whether the weather is cold (≤ 15), pleasant (16–30), or hot (> 30). 
# Also print both Celsius and Fahrenheit values.
# °F = (°C x 1.8) + 32 








### Problem 14: Password Strength Checker

# Ask the user to input password length (integer) and whether it contains special characters ("yes"/"no").
#  Using logical and comparison operators, determine if password is Strong (length ≥ 8 and has special characters), 
# Medium (length ≥ 6 or has special characters), or Weak otherwise. Print the strength category.

### Problem 15: Profit or Loss with Percentage

# Ask the user to input cost price and selling price (floats). 
# Calculate profit or loss amount and percentage using arithmetic operators.
#  Using comparison operators, print whether it is profit, loss, or no profit-no loss.
#  Also check logically if profit percentage is more than 20% and print a message "High Profit" if true.

### Problem 16: Attendance Eligibility for Exam

# Take total classes and attended classes as integers. Calculate attendance percentage. 
# Using comparison and logical operators,
#  check if attendance is at least 75% and the student does not have any medical leave flag set to "no" or "yes". 
# If attendance < 75 but medical leave is "yes", still allow. Print eligibility and attendance percentage.