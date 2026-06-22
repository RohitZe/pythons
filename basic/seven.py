# loop ->repetition
# while

# i=0
# while (i<5):
#     print('naitik')
#     i=i+1

# naitik 5
# print 1 to 10 using loop
# print all even numbers from 1 to 10 using loop
# print all odd numbers from 1 to 10 using loop
# user will input any number you have to print its table


# nested loop
# while ke andar ek or while
# star pattern


# print('name',end=' ')
# print('rohit')


# pattern-1
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *



# m-1
# print('* * * * *')
# print('* * * * *')
# print('* * * * *')
# print('* * * * *')
# print('* * * * *')

#m-2
# i=0
# while i<5:
#     print('* * * * *')
#     i=i+1


# m-3
# nested loop
# matrix method -rows cols

# pattern-1
# 1 2 3 4 5
# * * * * *  row=1
# * * * * *  row=2
# * * * * *  row=3
# * * * * *  row=4
# * * * * *  row=5




# upar vali while will print the rows
# niche vali while will print the cols


# i=1
# while (i<=5):
#     j=1
#     while(j<=5):
#         print('*',end=' ')
#         j=j+1
#     print()
#     i=i+1

# Problem 1
# Print the following pattern:
# *
# * *
# * * *
# * * * *
# * * * * *

# max no of rows and cols involved
# formual making
# using observation

# i=1,j=print('*')->ek bar
# i=2 ,j=print('**')->do bar
# i=3,j=print('***') ->teen bar
# i=4 ,j=print('****')->char bar

# if(j<=i) 1,j=1,2,3,4,5 (1<=1)
# i=2 ,j=1,2     
# i=3  j=1,2,3
# i=4 j=1,2,3,4
# i=5 j=1,2,3,4,5 


# i=1
# while(i<=5):
#     j=1
#     while(j<=5):
#       if(j<=i):
#          print('*',end=' ')
#       j=j+1
#     print()
#     i=i+1



# Problem 2
# Print the following pattern:
# * * * * *
# * * * *
# * * *
# * *
# *


# observation
# i=1,j=1,2,3,4,5  j<=5-i+1=j<=6-i
# i=2,j=1,2,3,4    
# i=3.j=1,2,3


# i=1
# while(i<=5):
#     j=1
#     while(j<=5):
#       if(j<=6-i):
#          print('*',end=' ')
#       j=j+1
#     print()
#     i=i+1


# Problem 3
# Print the following pattern:
# 1
# 1 2
# 1 2 3 
# 1 2 3 4
# 1 2 3 4 5

# max->cols=5,rows=5
# i=1,j=1
# i=2,j=1,2
# i=3,j=1,2,3
# i=4,j=1,2,3,4


# i=1
# while(i<=5):
#     j=1
#     while(j<=5):
#       if(j<=i):
#          print(j,end=' ')
#       j=j+1
#     print()
#     i=i+1


# Problem 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5



i=1
while(i<=5):
    j=1
    while(j<=5):
      if(j<=i):
         print(i,end=' ')
      j=j+1
    print()
    i=i+1






# Problem 6
# 1
# 2 3
# 4 5 6
# 7 8 9 10


# Problem 7
# * * * * *
#   * * * *
#     * * *
#       * *
#         *









