def print_rangoli(size):
    # your code goes here
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string = []
    for i in range(size):
        e = "-".join(alphabet[i:size])
        string.append((e[::-1]+e[1:]).center(4*size-3, "-"))
    print('\n'.join(string[:0:-1]+string))


if __name__ == '__main__':
    n = int(input()) 
    print_rangoli(n)