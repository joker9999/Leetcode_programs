"""Given a 32-bit signed integer, reverse digits of an integer"""

"""
class Solution:
    def reverse(self, x: int) -> int:
"""
x = 1
y= str(x)
z= len(y)
char= str()
if z==1:
    char= y
elif y[0]=="-" and y[-1]=="0":
    char="-"
    for i in range(2,z):
        char= char + y[-i]
elif y[0]=="-":
    char="-"
    for i in range(1,z):
        char= char + y[-i]
elif y[-1]=="0":
    for i in range(2,z+1):
        char= char + y[-i]
else:
    for i in range(1,z+1):
        char= char + y[-i]

print(char)
