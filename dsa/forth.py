# logical data structure
# stack data structure
# LIFO
# last in first out

# nums=[10,20,30]
# nums.append(40)
# nums.append(50)
# nums.append(60)

# # pop()

# nums.pop()
# nums.pop()
# print(nums)

# len

# nums=[2,3,5,7,8,9,2,2,98]

# def lenx(nums):
#     cnt=0
#     for x in nums:
#         cnt=cnt+1
#     return cnt

# print(len(nums))
# print(lenx(nums))

# shallow copy vs deep copy
# bums=nums.copy()
# print(bums)

# cnt2=nums.count(2)
# print(cnt2)

# linear search algorithm

# nums=[2,3,5,7,8,9,2,2,98]

# def linear_search(nums,a):
#     for x in nums:
#         if x==a:
#             return True
#     return False

# print(linear_search(nums,65))

# def custom_count(nums,a):
#     cnt=0
#     for x in nums:
#         if x==a:
#             cnt=cnt+1
#     return cnt


# print(nums.count(2))
# print(custom_count(nums,2))

# make index custom function


# 87
# 98
# nums=[2,3,5,7,8,9,2,2,98]

# reverse
# nums=[98,2,2,9,8,7,5,3,2]

# core logic
# i=0
# while (i<len(nums)):
#   if(nums[i]==98):
#      print(i)
#   i=i+1

# def indexi(nums,a):
#     i=0
#     while(i<len(nums)):
#         if(nums[i]==a):
#             return i
#         i=i+1
#     return 'Type Error'

# print(indexi(nums,3))
# print(nums.index(67))
# print(nums.reverse())
# print(nums)

# two pointer approach
nums=[10,20,30,40,50,60,70,80,90]

# start=0
# end=len(nums)-1

# print(nums)
# print(nums[start])
# print(nums[end])

# nums[start],nums[end]=nums[end],nums[start]
# print(nums)

# a=1
# b=2
# a,b=b,a
# print(a,b)


def custom_reverse(nums):
    start=0
    end=len(nums)-1
    while(start<end):
        nums[start],nums[end]=nums[end],nums[start]
        start=start+1
        end=end-1


nums.reverse()
custom_reverse(nums)

print(nums)











# make reverse custom function




