N, M = map(int, input().split())

h = '-'
f = '.|.'
welcome = 'WELCOME'

for i in range(1,N,2):       
    print(f.center(M, h))