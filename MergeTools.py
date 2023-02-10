def merge_the_tools(string, k):
    # your code goes here 
    start = 0
    while(start < len(string)):
        wrap = string[start:start+k]
        substr = ""
        for i in wrap:
            if i not in substr:
                substr += i
        start += k
        print(substr)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)