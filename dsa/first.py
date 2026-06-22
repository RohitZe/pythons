# what is data structure
# are storage for data so we can organize our data and use it easily (save delete update)
# why we need data structure
# when we want to store multiple data into single variable

# roll no-1001,103,89,98
# cities- store later use effectively

# data type, internally this execute as a string data structure
name="naitik"

# indexing
# mapping 0,1,2,4---(len-1)

# # print(name[0])
# firstIndex=0
# middleIndex=len(name)//2
# lastIndex=len(name)-1

# print(name[firstIndex])
# print(name[middleIndex])
# print(name[lastIndex])
# print the last charchter of the string
# calculate the length of the string 
# print the middle charcter of the string


# print calculate the vowels inside the name
# hint->a,e,i,o,u
# while or for
# print all elements of the name using while loop or for loop

i=0
cnt=0
while i<len(name):
    if (name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u'):
        cnt=cnt+1
    i=i+1

print(cnt)

for x in name:
    if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
        cnt=cnt+1
print(cnt)