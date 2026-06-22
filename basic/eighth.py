# Print the following pattern:
# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

# i=1
# while(i<=5):
#     j=1
#     while(j<=5):
#       if(j<=i):
#          print(6-j,end=' ')
#       j=j+1
#     print()
#     i=i+1

# Problem 6
# 1
# 2 3
# 4 5 6
# 7 8 9 10

# i=1
# x=1
# while(i<=4):
#     j=1
#     while(j<=4):
#         if(j<=i):
#             print(x,end=' ')
#             x=x+1
#         j=j+1
#     print()
#     i=i+1


# HCF/GCD

# 6 9
# 1 1
# 2 
# 3 3
# _ _
# 6 
#   9

# 24 36
# 1   1
# 2   2
# 3   3
# 4   4
# 6   6
# 8   
#     9
# 12  12
#     18
# 24  36

# hcf=12



# n=24
# m=36
# i=1
# hcf=0
# while (i<=n):
#     if(n%i==0 and m%i==0):
#      hcf=i
#     i=i+1

# print('HCF is',hcf)

# lcm
# 12 36
# 24 72
# 36 108
# 48 144
# 60 180
# 72 216
# 36

# break->intentionaly jb loop se bahr aana ho


# n=12
# m=36
# i=m
# lcm=0
# while (i<=n):
#     if(n%i==0 and m%i==0):
#      hcf=i
#     i=i+1

# print('HCF is',hcf)


# lcm
n=12
m=8
i=m
lcm=0
while (i<=(n*m)):
    if(i%n==0 and i%m==0):
     lcm=i
     break
    i=i+1

print('LCM is',lcm)
