# set data structure
# unordered
# indexing mhi hoti
# unique data
# faster for find operation
# immutable



# st={1,2,2,3,4,5}
# print(st)

# print(st[0])

# in not in ->membership operator
# print(6 in st)


user={12,34,56,7,8,0}
ans={12,7,8,99,88,77}

marks=0
neg=1
for x in user:
    if (x in ans):
        marks=marks+4
    else:
        marks=marks-neg

print(marks)

