N, M = map(int, input().split())

h = '-'
f = '.|.'
welcome = 'WELCOME'

for i in range(1,N,2):       
    print((f*i).center(M, h))

print(welcome.center(M,h))

for i in range(1,N,2):       
    print((f*(N-i-1)).center(M, h))