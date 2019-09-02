"""Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]."""


lst=input("Enter the lis: ").split()
target= int(input("Enter the target: "))
index= list()
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        c= int(lst[i])+int(lst[j])
        if c==target:
            index.append([i,j])

print(index)
