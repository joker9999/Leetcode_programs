"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

#def plusOne(self, digits: List[int]) -> List[int]:

digits= [1,8]
num= len(digits)
op=[]
sum= 0
for i in digits:
    sum+= i**(num-1)
    num-=1
sum +=1
sum_s= str(sum)
print(sum_s)
for j in range(len(digits)):
    op.append(sum_s[j])
print(op)
