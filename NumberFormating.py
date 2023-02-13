def print_formatted(number):
    # your code goes here
    lenght = len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(lenght),end=' ')
        print(oct(i)[2:].rjust(lenght),end=' ')
        print(hex(i)[2:].upper().rjust(lenght), end=' ')
        print(bin(i)[2:].rjust(lenght))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)