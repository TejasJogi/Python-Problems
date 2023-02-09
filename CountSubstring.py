def count_substring(string, sub_string):
    sum = 0
    for i in range(len(string)):
        print(string[i:])
        sum += string[i:].startswith(sub_string)
    return sum


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

    