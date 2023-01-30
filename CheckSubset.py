number_of_test_cases = int(input())


for i in range(1,number_of_test_cases+1):
    number_of_set_A_elements = int(input())
    set_A_elements = set(map(int, input().split()))
    number_of_set_B_elements = int(input())
    set_B_elements = set(map(int, input().split()))
    if (set_A_elements.issubset(set_B_elements)):
        print(True)
    else:
        print(False)