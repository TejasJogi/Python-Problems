# Task

# Perform append, pop, popleft and appendleft methods on an empty deque d.

# Input Format

# The first line contains an integer N, the number of operations.
# The next N lines contains the space separated names of methods and their values.

# Constraints


# Output Format

# Print the space separated elements of deque d.

# Sample Input

# 6
# append 1
# append 2
# append 3
# appendleft 4
# pop
# popleft

# Sample Output

# 1 2


from collections import deque


N = int(input())

d = deque()

for _ in range(N):

    inp = input().split()


    if inp[0] == 'append':
        d.append(inp[1])

    elif inp[0] == 'appendleft':
        d.appendleft(inp[1])
        
    elif inp[0] == 'clear':
        d.clear(inp[1])  

    elif inp[0] == 'extend':
        d.extend(inp[1])

    elif inp[0] == 'extendleft':
        d.extendleft(inp[1])
    
    elif inp[0] == 'count':
        d.count(inp[1])
    
    elif inp[0] == 'pop':
        d.pop()
    
    elif inp[0] == 'popleft':
        d.popleft()
    
    elif inp[0] == 'remove':
        d.remove(inp[1])
    
    elif inp[0] == 'reverse':
        d.reverse()
    
    elif inp[0] == 'rotate':
        d.rotate(inp[1])

for i in d:
    print(i, end=' ')