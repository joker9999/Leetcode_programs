"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
"""
s= (input("Enter the numbers: "))
a= (s).split()
target= str(14)

def loop(a,target):
    counter=0
    for i in a:
        if i==target:
            break
        else:
            counter+=1
    return counter

if loop(a,target)== len(a):
    a.append(target)
    a.sort(key=int)
    print(loop(a,target))
else:
    print(loop(a,target))
