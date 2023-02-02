N = int(input())

lst = []

for i in range(N):

    method_inp = input().split(" ")
    method = method_inp[0]
    inp = method_inp[1:]

    if method == "insert":
        index = int(inp[0])
        number = int(inp[1])
        lst.insert(index, number)

    elif method == "remove":
        number = int(inp[0])
        lst.remove(number)

    elif method == "append":
        number = int(inp[0])
        lst.append(number)
    
    elif method == "sort":
        lst.sort()
    
    elif method == "pop":
        lst.pop()

    elif method == "reverse":
        lst.reverse()

    elif method == "print":
        print(lst)
