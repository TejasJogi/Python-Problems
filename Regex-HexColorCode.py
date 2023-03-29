# You are given N lines of CSS code. Your task is to print all valid Hex Color Codes, in order of their occurrence from top to bottom.

# CSS Code Pattern

# Selector
# {
# 	Property: Value;
# }
# Input Format

# The first line contains N, the number of code lines.
# The next N lines contains CSS Codes.

# Output Format

# Output the color codes with '#' symbols on separate lines.

# Sample Input

# 11
# #BED
# {
#     color: #FfFdF8; background-color:#aef;
#     font-size: 123px;
#     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
# }
# #Cab
# {
#     background-color: #ABC;
#     border: 2px dashed #fff;
# }   
# Sample Output

# #FfFdF8
# #aef
# #f9f9f9
# #fff
# #ABC
# #fff


import re

N=int(input())

for i in range(0,N):
    s=input()

    x=s.split()

    if len(x)>1  and  '{' not in x:
        x=re.findall(r'#[a-fA-F0-9]{3,6}',s)
        [print(i) for  i in x]