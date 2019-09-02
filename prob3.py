"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807."""


a=[2,4,6]
b=[5,6,4]


op=[]

def sum_list(a):
    sum=0
    x=0
    for i in a[:]:
        sum= i*(10**x)  + sum
        x=x+1
    return(sum)

sum_a= sum_list(a)
sum_b= sum_list(b)

sum= sum_a+sum_b
result= list(str(sum))
print(result)
for i in range(1,len(result)+1):
    op.append(result[-i])
print(op)
