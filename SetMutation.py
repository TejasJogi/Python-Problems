elements_in_A = int(input())
A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    Method_And_Count = input()

    split = Method_And_Count.split()

    Method = split[0]
    Number_of_element = split[1]
   
    Otherset = set(map(int, input().split()))
    
    if Method == "intersection_update":
        A.intersection_update(Otherset)
    elif Method == "update":
        A.update(Otherset)
    elif Method == "symmetric_difference_update":
        A.symmetric_difference_update(Otherset)
    elif Method == "difference_update":
        A.difference_update(Otherset)

print(sum(A))