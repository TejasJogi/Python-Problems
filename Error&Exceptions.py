
T = int(input())

for _ in range(T):
    a, b = input().split()

    if b == '0':
        try:
            print(int(a)//int(b))
        except ZeroDivisionError as e:
            print("Error Code:",e)

    elif type(b) == str:
        try:
            print(int(a)//int(b))
        except ValueError as e:
            print("Error Code:",e)
    else:
        print(int(a)//int(b))