#print square from range

def square(n):
    for i in range(1, n): #if you want input from 1 to n
        s = i * i
        print(s)
        
n = int(input("Enter a number : "))
        
square(n)