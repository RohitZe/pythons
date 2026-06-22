# list
# data structure
# it can store different values of different data types in ordered way
# indexing
# nums=[1,2,3,5,7,8,9,0,0,123,4,5,4,5,7,7,98]

# first element middle element last element
# firstIndex=0
# middleIndex=len(nums)//2
# lastIndex=len(nums)-1
# print(nums[firstIndex])
# print(nums[middleIndex])
# print(nums[lastIndex])

# different data type
# bums=[1,2.09,'rohit',True]

# print(bums[0])
# print(bums[2])

# traverse this list with while and for in loop

# for x in bums:
#     print(x)

# i=0
# while i<len(bums):
#     print(bums[i])
#     i=i+1


# nums=[1,2,3,4,5,6,7,8]
# using while loop
# for loop 
# print the alternate number starting from 1
# print all the even numbers from the nums(list)
# print all the odd numbers from the nums(list)
# add all the even numbers in the nums(list)


# nums=[1,2,113,499999,5,6,7,-8,56,76,87,564,9999]
# maxi=-99999999

# i=0
# while i<len(nums):
#     if maxi<nums[i]:
#         maxi=nums[i]
# #     i=i+1

# print(maxi)

# mini=99999999

# i=0
# while i<len(nums):
#     if mini>nums[i]:
#         mini=nums[i]
#     i=i+1

# print(mini)


# i=0
# sum=0
# while i<len(nums):
#     if(nums[i]%2==0):
#      sum=sum+nums[i]
#     i=i+1

# print(sum)
# for x in nums:
#     if x%2==0:
#         sum=sum+x


# for x in nums:
#     if x%2==0:
#         sum=sum+x


# print(min(nums))

# print(sum)
# find the largest number from the list 

# i=0
# find the smallest number from the list


# nums=[1,2,113,499999,5,6,7,-8,56,76,87,564,9999]

# bums=[1,2,3,4,5,6,0,45,-2]
# def minima(bums):
#     i=0
#     mini=99999999
#     while i<len(bums):
#         if mini>bums[i]:
#             mini=bums[i]
#         i=i+1
#     return mini

# print(minima(bums))


# inplace

# call by value ,call by refrence
# inplace ->orginal value list ki ko modify krdena
# rums=[1,2,4]


# def inplaced(rums):
#     rums[1]=10


# inplaced(rums)


# matrix
# row and cols
#          0  1  2
# nums=[0 [10,20,30],
#       1 [40,50,60],
#       2 [70,80,90]]


# print(nums[0][1])

nums=[[10,20,33],
      [40,55,60],
      [70,80,90]]

# print the whole nums using nested while loops
# i=0
# sum=0
# while(i<3):
#     j=0
#     while(j<3):
#         if(nums[i][j]%11==0):
#             sum=sum+nums[i][j]
#         j=j+1
#     i=i+1

# print(sum)


# calculate the sum of  numbers which are divisble by 11

# print the sum of all the rows

# i=0
# sumF=0
# sumS=0
# sumT=0
# sum=0
# while(i<3):
#     j=0
#     sum=0
#     while(j<3):
#         sum=sum+nums[j][i]
#         j=j+1 
#     print(sum)
#     i=i+1


# print the sum of all the cols
# print the sum of all the matrix(rows+cols)

# for i in range(3):
#    for j in range(3):
#        print(nums[i][j])


# def sum(a,b):
#     return a+b


# print(sum(2,3))




# nums=[
#      [
#      [10,20,30],
#      [40,50,60],
#      [70,80,90]
#      ],
#      [
#      [11,22,33],
#      [44,55,66],
#      [77,88,99]
#      ],
#     [
#      [100,102,103],
#      [104,104,108],
#      [77,88,99]
#      ]
#     ]


# # 60
# print(nums[0][1][2])
# # 55
# print(nums[1][1][1])
# # 102
# print(nums[2][0][1])
# # 108
# print(nums[2][1][2])

nums=[
     [
     [10,20,30],
     [40,50,60],
     [70,80,90]
     ],
     [
     [11,22,33],
     [44,55,66],
     [77,88,99]
     ],
    [
     [100,102,103],
     [104,104,108],
     [77,88,99]
     ]
    ]

i=0
while (i<3):
    j=0
    while(j<3):
        k=0
        while(k<3):
            print(nums[i][j][k],end=' ')
            k=k+1
        j=j+1
    i=i+1





